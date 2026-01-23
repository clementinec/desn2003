# DESN2003 Lecture Template & Checklist

A consistent structure for all weekly lectures to ensure students feel they're learning solid, connected content.

---

## Required Elements for Each Week

### 1. Opening (First 3-5 slides)

- [ ] **Title slide** with week number, topic title, and subtitle that hints at the "why"
- [ ] **Callback/Connection** to previous week (1 slide)
  - "Last week we learned X. Today we build on that by..."
  - Reinforces the throughline
- [ ] **Today's Roadmap** (1 slide)
  - 3-5 bullet points of what will be covered
  - Non-incremental so students see the full agenda
- [ ] **Learning Objectives** (can combine with roadmap or separate)
  - "By the end of this session, you will be able to..."
  - 3-4 concrete, actionable objectives

### 2. Content Sections

- [ ] **Colored section headers** (`{background-color="#HEXCODE"}`) to visually segment major topics
- [ ] **Callout boxes** for key concepts:
  - `.callout-note` for definitions/information
  - `.callout-tip` for practical advice
  - `.callout-warning` for common pitfalls
  - `.callout-important` for critical points
- [ ] **Two-column layouts** (`::: {.columns}`) for comparisons, parallel concepts
- [ ] **Concrete examples** tied to student context (design, Instagram throughline, their own research)
- [ ] **Visuals/diagrams** where appropriate (not just text)

### 3. Activities (At least one per session)

- [ ] **Clear instructions** with time allocation
- [ ] **Connection to concepts** just taught
- [ ] **Deliverable** - what should students produce or discuss?
- [ ] **Debrief slide** - what did we learn from this activity?

### 4. Throughline Connections

- [ ] Reference **student's own research project** at least once
  - "How does this apply to YOUR research question?"
  - "Think about your Doc X submission..."
- [ ] **Instagram example** or equivalent running case study where relevant
- [ ] Connect abstract concepts to **practical application**

### 5. Assessment Connection

- [ ] **Reminder of upcoming deadlines** (if within 2 weeks)
- [ ] **How today's content helps** with that assessment
- [ ] Clear **"What to do next"** for their project

### 6. Closing (Final 3-5 slides)

- [ ] **Key Takeaways** (1 slide)
  - 4-6 numbered points summarizing what they learned
  - Non-incremental so they see the full list
- [ ] **The Bridge** (1 slide)
  - "Today we learned X → Next week we'll learn Y"
  - Shows how content connects forward
- [ ] **Questions slide**
- [ ] **Optional: Preview of next week's topic**

---

## Visual Consistency Standards

### Color Palette for Section Headers
```
Primary sections:    #4ECDC4 (teal)
Activities:          #FFE66D (yellow)
Warnings/Challenges: #FF6B6B (coral)
Wrap-up/Synthesis:   #457B9D (slate blue)
Examples/Cases:      #A8DADC (light blue)
```

### Callout Usage
```markdown
::: {.callout-note icon=false}
## Title Here
Content for definitions, neutral information
:::

::: {.callout-tip icon=false}
## Pro Tip / Hint
Practical advice, helpful strategies
:::

::: {.callout-warning icon=false}
## Watch Out / Common Pitfall
Things to avoid, mistakes students make
:::

::: {.callout-important icon=false}
## Key Point / Critical
Must-know information, central concepts
:::
```

### Two-Column Layout
```markdown
::: {.columns}
::: {.column width="50%"}
**Left side content**
:::

::: {.column width="50%"}
**Right side content**
:::
:::
```

---

## Throughline: The Student Research Journey

Each week should connect to where students are in their research journey:

| Week | Topic | Student Journey Stage | Assessment Connection |
|------|-------|----------------------|----------------------|
| 1 | Why Research Matters | Spark curiosity, propose ideas | — |
| 2 | Research Frameworks | Validate the gap | Doc 0 intro |
| 3 | Literature Review | Map the landscape | Doc 0 due Week 4 |
| 4 | Research Questions | Frame the question | Doc 0 feedback |
| 5 | Methods I | Plan data collection | Doc 0.1 prep |
| 6 | Methods II | Refine methodology | Doc 0.1 due Week 6 |
| 7 | Analysis | Prepare for evidence | — |
| 8 | Writing | Prof Discovery Presentations | Presentations |
| 9 | Synthesis | Prof Discovery cont'd | Prof Discovery Docs |
| 10 | Data Visualization | Finalize evidence | Doc 0.2 due |
| 11 | Workshop | Final integration | Doc 1 due |
| 12 | Presentations | Present & evaluate | Peer Evaluation |

---

## Quality Checklist (Before Finalizing)

- [ ] Does the week have a clear "one big idea"?
- [ ] Can a student articulate what they learned in one sentence?
- [ ] Is there at least one hands-on activity?
- [ ] Are there explicit connections to their own research?
- [ ] Do the takeaways match the stated objectives?
- [ ] Is the visual structure consistent with other weeks?
- [ ] Is the assessment connection clear (if applicable)?
