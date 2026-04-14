from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import seaborn as sns
from wordcloud import STOPWORDS, WordCloud


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
OUT_DIR = DATA_DIR / "week10_figures"

PALETTE = {"GenAI": "#2A9D8F", "Traditional": "#E76F51"}
RECOMMEND_PALETTE = {"Yes": "#2A9D8F", "No": "#E76F51"}
REGION_TO_COUNTRY = {
    "Africa": ("Nigeria", "NGA"),
    "Asia": ("India", "IND"),
    "Europe": ("Germany", "DEU"),
    "North America": ("United States", "USA"),
    "South America": ("Brazil", "BRA"),
}


def load_data() -> tuple[pd.DataFrame, list[dict[str, str]]]:
    survey_df = pd.read_csv(DATA_DIR / "survey_data.csv")
    transcripts = json.loads((DATA_DIR / "transcripts.json").read_text(encoding="utf-8"))

    survey_df["CommentLength"] = survey_df["Comment"].str.split().str.len()
    survey_df["PositiveRecommend"] = survey_df["Recommend"].eq("Yes").astype(int)
    survey_df["SatisfactionBand"] = pd.cut(
        survey_df["Satisfaction"],
        bins=[0, 2, 3, 5],
        labels=["Low (1-2)", "Medium (3)", "High (4-5)"],
        include_lowest=True,
    )
    survey_df["Country"] = survey_df["Region"].map(lambda value: REGION_TO_COUNTRY[value][0])
    survey_df["ISO3"] = survey_df["Region"].map(lambda value: REGION_TO_COUNTRY[value][1])

    return survey_df, transcripts


def setup_style() -> None:
    sns.set_theme(style="whitegrid", context="talk")
    plt.rcParams["axes.spines.top"] = False
    plt.rcParams["axes.spines.right"] = False
    OUT_DIR.mkdir(parents=True, exist_ok=True)


def save_bar_histogram_example(survey_df: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    sns.countplot(
        data=survey_df,
        x="Group",
        hue="Recommend",
        palette=RECOMMEND_PALETTE,
        ax=axes[0],
    )
    axes[0].set_title("Bar Chart: Recommendation by Group")
    axes[0].set_xlabel("Learning Method")
    axes[0].set_ylabel("Number of Students")
    axes[0].legend(title="Recommend")

    sns.histplot(
        data=survey_df,
        x="Score",
        hue="Group",
        bins=8,
        multiple="layer",
        alpha=0.45,
        palette=PALETTE,
        ax=axes[1],
    )
    axes[1].set_title("Histogram: Score Distribution")
    axes[1].set_xlabel("Test Score")
    axes[1].set_ylabel("Number of Students")

    fig.tight_layout()
    fig.savefig(OUT_DIR / "bar_histogram_examples.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def save_boxplot_example(survey_df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(
        data=survey_df,
        x="Group",
        y="Score",
        hue="Group",
        dodge=False,
        palette=PALETTE,
        ax=ax,
    )
    if ax.legend_:
        ax.legend_.remove()
    ax.set_title("Test Score Distribution by Group")
    ax.set_xlabel("Learning Method")
    ax.set_ylabel("Test Score")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "box_plot_scores.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def save_heatmap_examples(survey_df: pd.DataFrame) -> None:
    crosstab = pd.crosstab(survey_df["Group"], survey_df["Recommend"])
    corr = survey_df[["Score", "Satisfaction", "CommentLength", "PositiveRecommend"]].corr()

    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    sns.heatmap(corr, annot=True, cmap="YlGnBu", vmin=-1, vmax=1, ax=axes[0])
    axes[0].set_title("Correlation Heatmap")

    sns.heatmap(crosstab, annot=True, fmt="d", cmap="mako", ax=axes[1])
    axes[1].set_title("Outcome Matrix: Group vs Recommend")
    axes[1].set_xlabel("Recommend")
    axes[1].set_ylabel("Group")

    fig.tight_layout()
    fig.savefig(OUT_DIR / "heatmap_examples.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def save_wordcloud_example(transcripts: list[dict[str, str]]) -> None:
    all_text = " ".join(entry["text"] for entry in transcripts)
    stopwords = STOPWORDS.union({"ai", "chatgpt", "using", "used", "tool", "tools"})
    wordcloud = WordCloud(
        width=1200,
        height=700,
        background_color="white",
        stopwords=stopwords,
        collocations=False,
    ).generate(all_text)

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    ax.set_title("Word Cloud of Interview Transcript Text")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "wordcloud_transcripts.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def save_treemap_example(survey_df: pd.DataFrame) -> None:
    region_group_counts = (
        survey_df.groupby(["Region", "Group"], as_index=False)
        .agg(Count=("ParticipantID", "count"), AverageScore=("Score", "mean"))
        .sort_values(["Region", "Group"])
    )

    labels = []
    parents = []
    values = []
    colors = []
    text = []

    for region, region_df in region_group_counts.groupby("Region"):
        labels.append(region)
        parents.append("")
        values.append(int(region_df["Count"].sum()))
        colors.append(float(region_df["AverageScore"].mean()))
        text.append(f"{int(region_df['Count'].sum())} students")

        for row in region_df.itertuples(index=False):
            labels.append(f"{row.Region} | {row.Group}")
            parents.append(row.Region)
            values.append(int(row.Count))
            colors.append(float(row.AverageScore))
            text.append(f"{row.Count} students<br>Avg score {row.AverageScore:.1f}")

    fig = go.Figure(
        go.Treemap(
            labels=labels,
            parents=parents,
            values=values,
            text=text,
            textinfo="label+text",
            marker=dict(colors=colors, colorscale="Tealrose", showscale=True),
            branchvalues="total",
            hovertemplate="%{label}<br>%{text}<extra></extra>",
        )
    )
    fig.update_layout(title="Treemap: Region and Group Counts", margin=dict(t=60, l=20, r=20, b=20))
    fig.write_image(OUT_DIR / "treemap_region_group.png", width=1200, height=700, scale=2)


def save_choropleth_example(survey_df: pd.DataFrame) -> None:
    region_map = (
        survey_df.groupby(["Region", "Country", "ISO3"], as_index=False)
        .agg(Participants=("ParticipantID", "count"), AverageScore=("Score", "mean"))
        .sort_values("Participants", ascending=False)
    )

    fig = go.Figure(
        go.Choropleth(
            locations=region_map["ISO3"],
            z=region_map["AverageScore"],
            text=region_map["Country"],
            customdata=region_map[["Region", "Participants"]],
            colorscale="Viridis",
            colorbar_title="Avg Score",
            marker_line_color="white",
            hovertemplate=(
                "%{text}<br>"
                "Region: %{customdata[0]}<br>"
                "Participants: %{customdata[1]}<br>"
                "Average score: %{z:.1f}<extra></extra>"
            ),
        )
    )
    fig.update_layout(
        title="Choropleth Demo: Region-Level Data Mapped to Representative Countries",
        geo=dict(showframe=False, showcoastlines=True, projection_type="natural earth"),
        margin=dict(t=60, l=20, r=20, b=20),
    )
    fig.write_image(OUT_DIR / "choropleth_representative_countries.png", width=1200, height=700, scale=2)


def save_sankey_example(survey_df: pd.DataFrame) -> None:
    sankey_df = (
        survey_df.groupby(["Group", "SatisfactionBand", "Recommend"], as_index=False, observed=False)
        .size()
        .rename(columns={"size": "Count"})
    )

    group_nodes = list(survey_df["Group"].drop_duplicates())
    band_nodes = list(survey_df["SatisfactionBand"].cat.categories)
    recommend_nodes = list(survey_df["Recommend"].drop_duplicates())
    labels = group_nodes + band_nodes + recommend_nodes
    index_map = {label: idx for idx, label in enumerate(labels)}

    source = []
    target = []
    value = []
    link_color = []

    for row in sankey_df.itertuples(index=False):
        source.append(index_map[row.Group])
        target.append(index_map[row.SatisfactionBand])
        value.append(row.Count)
        link_color.append("rgba(42, 157, 143, 0.35)" if row.Group == "GenAI" else "rgba(231, 111, 81, 0.35)")

        source.append(index_map[row.SatisfactionBand])
        target.append(index_map[row.Recommend])
        value.append(row.Count)
        link_color.append("rgba(69, 123, 157, 0.25)")

    node_colors = [
        "#2A9D8F",
        "#E76F51",
        "#8AB17D",
        "#E9C46A",
        "#457B9D",
        "#2A9D8F",
        "#E76F51",
    ]

    fig = go.Figure(
        data=[
            go.Sankey(
                arrangement="snap",
                node=dict(label=labels, pad=18, thickness=18, color=node_colors),
                link=dict(source=source, target=target, value=value, color=link_color),
            )
        ]
    )
    fig.update_layout(title_text="Sankey Diagram: Group -> Satisfaction Band -> Recommendation", font_size=16)
    fig.write_image(OUT_DIR / "sankey_group_satisfaction_recommend.png", width=1200, height=700, scale=2)


def main() -> None:
    survey_df, transcripts = load_data()
    setup_style()

    save_bar_histogram_example(survey_df)
    save_boxplot_example(survey_df)
    save_heatmap_examples(survey_df)
    save_wordcloud_example(transcripts)
    save_treemap_example(survey_df)
    save_choropleth_example(survey_df)
    save_sankey_example(survey_df)

    print(f"Generated Week 10 figures in {OUT_DIR}")


if __name__ == "__main__":
    main()
