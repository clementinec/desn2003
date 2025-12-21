# save as app.py and run with:  streamlit run app.py
import random
import streamlit as st

# st.set_page_config(page_title="Presentation Picker", page_icon="🎓")

st.set_page_config(
    page_title="Presentation Picker",
    page_icon="🎓",
    layout="wide",          # 👈 full-width layout (alternatives: "centered")
    initial_sidebar_state="collapsed",
)

# ---------- 1 · Data ---------------------------------------------------------
# Put your class list here once. (Index is the “number”.)
STUDENTS = ['Catherine Rose Au', 'Ka Ching Chan', 'Siqi Chen', 'Ying Qi Chen',
       'Ruos Garcia-Gil Mariana Constanza Da', 'Zhangjiayi Duan',
       'Xinran He', 'Ran Ju', 'Hyeonseo Kim', 'Minseo Kim',
       'Seohyeon Kim', 'Yunxiu Li', 'Charlotte Liu', 'Alana L N Lo',
       'I Ciao Tonia Pao', 'Krish Paras Patel', 'Alden Robert Schaaf',
       'Zheyu Shu', 'Sze Ching Wong', 'Zichen Xiao',
       'Sabina Yegemberdiyeva', 'Yizhuo Zhang', 'Tan Siu Zheng',
       'Nyein Aye Zin']

# ---------- 2 · Session state -----------------------------------------------
# Keep track of who has already presented
if "presented" not in st.session_state:
    st.session_state.presented = []        # list of names

# Shortcut helpers
def remaining():
    return [s for s in STUDENTS if s not in st.session_state.presented]

# ---------- 3 · UI -----------------------------------------------------------
st.title("🎓 Pick your DESN2003 Presentation Champion")

# --- 3-A. Volunteer buttons --------------------------------------------------
st.subheader("Mark a volunteer")
cols = st.columns(3)  # lay buttons out in columns
for idx, name in enumerate(remaining(), start=1):
    # distribute buttons across the 3 columns
    col = cols[(idx - 1) % 3]
    if col.button(f"{idx}. {name}", key=f"vol_{name}"):
        st.session_state.presented.append(name)
        st.toast(f"{name} volunteered!", icon="✅")

st.divider()

# --- 3-B. Random draw --------------------------------------------------------
if st.button("🎲 Draw random student", use_container_width=True):
    pool = remaining()
    if pool:
        pick = random.choice(pool)
        st.session_state.presented.append(pick)
        st.success(f"Randomly selected **{pick}**")
    else:
        st.warning("Everyone has already presented. 🏁")

st.divider()

# --- 3-C. Report -------------------------------------------------------------
st.subheader("✅ Already presented")
if st.session_state.presented:
    for idx, name in enumerate(STUDENTS, start=1):
        if name in st.session_state.presented:
            st.markdown(f"**{idx}. {name}**")
else:
    st.info("No one has presented yet.")

# --- 3-D. Remaining count ----------------------------------------------------
st.caption(f"Students remaining: {len(remaining())} / {len(STUDENTS)}")
