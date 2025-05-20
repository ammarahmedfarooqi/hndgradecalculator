import streamlit as st
import pandas as pd
import altair as alt

# --- Hide sidebar, hamburger, and set background ---
st.markdown("""
    <style>
    [data-testid="stSidebar"] {display: none !important;}
    [data-testid="collapsedControl"] {display: none !important;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
    }
    .custom-topbar {
        position: fixed;
        top: 0; left: 0; right: 0;
        height: 110px;
        background: #8a206f;
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 10000;
        box-shadow: 0 2px 18px rgba(0,0,0,0.10);
    }
    .custom-topbar-title {
        color: #fff;
        font-size: 34px;
        font-weight: 800;
        letter-spacing: 2px;
        text-align: center;
        width: 100%;
        line-height: 110px;
        margin: 0;
        padding: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        user-select: none;
    }
    .main-content-canvas {
        margin-top: 110px;
        min-height: calc(100vh - 110px);
        width: 100vw;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
    }
    .section-box {
        background: #13294b;
        color: #fff;
        font-size: 2.1rem;
        font-weight: 700;
        border-radius: 16px;
        padding: 18px 44px 18px 44px;
        margin-top: 32px;
        margin-bottom: 20px;
        box-shadow: 0 3px 12px rgba(19,41,75,0.10);
        text-align: center;
        display: inline-block;
        letter-spacing: 1px;
    }
    .section-subbox {
        background: #13294b;
        color: #fff;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 12px;
        padding: 12px 28px 12px 28px;
        margin: 0 0 30px 0;
        box-shadow: 0 2px 8px rgba(19,41,75,0.10);
        text-align: center;
        display: inline-block;
        letter-spacing: 1px;
    }
    /* Style selectboxes */
    div[data-baseweb="select"] > div {
        background: #8a206f !important;
        color: #fff !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
    }
    label.css-1c7y2kd {
        color: #8a206f !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
    }
    /* Style selectbox dropdowns */
    .css-1c7y2kd, .css-1p1mnbb {
        color: #8a206f !important;
        font-weight: 700 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- TOPBAR HTML ---
st.markdown("""
<div class="custom-topbar">
    <span class="custom-topbar-title">Level 3 Extended Business Diploma Grade Calculator</span>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="main-content-canvas">', unsafe_allow_html=True)

st.markdown("""
<div style="display: flex; flex-direction: column; align-items: center;">
    <div class="section-box">
        Level 3 Extended Business Diploma Grade Calculator
    </div>
    <div class="section-subbox">
        Select your grade for each unit:
    </div>
</div>
""", unsafe_allow_html=True)

# --- GRADE INFO TOOLTIP/EXPANDER ---
st.markdown("#### What do the grades mean? [ℹ️](#)", unsafe_allow_html=True)
with st.expander("Grade Info"):
    st.markdown("""
    - **U**: Unclassified (fail)
    - **P**: Pass
    - **M**: Merit
    - **D**: Distinction
    """)

# Units with Guided Learning Hours (GLH)
units = {
    "Exploring The Business": 90,
    "Research And Plan Marketing Campaign": 90,
    "Business Finance": 90,
    "Managing An Event": 90,
    "International Business": 90,
    "Principles Of Management": 60,
    "Business Decision Making": 60,
    "Human Resources": 120,
    "Team Building In Business": 60,
    "Recording Financial Transactions": 60,
    "Cost And Management Accounting": 60,
    "Visual Merchandising": 60,
    "Digital Marketing": 60,
    "Pitching for A New Business": 60,
    "Branding": 60,
    "Extra 60 GLH (if needed)": 60,
}

# Points per GLH for Level 3 Computing/Business
points_per_glh = {
    60: {"P": 6, "M": 10, "D": 16},
    90: {"P": 9, "M": 15, "D": 24},
    120: {"P": 12, "M": 20, "D": 32},
}

grade_options = ["U", "P", "M", "D"]

total_points = 0
unit_points_list = []
unit_grades = {}

for unit, glh in units.items():
    grade = st.selectbox(f"{unit} ({glh} GLH)", grade_options, index=0, key=unit)
    unit_grades[unit] = grade
    if grade == "U":
        unit_points = 0
    else:
        unit_points = points_per_glh[glh][grade]
    total_points += unit_points
    unit_points_list.append({"Unit": unit, "Points": unit_points, "Grade": grade})

st.markdown(f"""
<div class="section-subbox" style="margin-top:30px;">
    <span style="font-size:1.3rem;">Total Points: <b style="color:#8a206f;">{int(total_points)}</b></span>
</div>
""", unsafe_allow_html=True)

# Grade thresholds for Level 3 Business (same as Level 3 Computing)
grade_thresholds = {
    "DDD*": 270,
    "DDD": 252,
    "D*DD": 234,
    "DDD (lower)": 216,
    "DDM": 196,
    "DMM": 176,
    "MMM": 156,
    "MMP": 140,
    "MPP": 124,
    "PPP": 108,
    "U": 0,
}

# --- PROGRESS BAR TO NEXT GRADE ---
sorted_thresholds = sorted(grade_thresholds.items(), key=lambda x: x[1], reverse=True)
next_grade_points = None
next_grade_name = None
for name, threshold in sorted_thresholds:
    if threshold > total_points:
        next_grade_points = threshold
        next_grade_name = name
        break

if next_grade_points:
    points_to_next = int(next_grade_points - total_points)
    percent = min(int(total_points / next_grade_points * 100), 100)
    st.progress(percent, text=f"{points_to_next} points to next grade ({next_grade_name})")
else:
    st.progress(100, text="Maximum grade achieved!")

predicted_grade = "U"
for grade_name, threshold in sorted(grade_thresholds.items(), key=lambda x: x[1], reverse=True):
    if total_points >= threshold:
        predicted_grade = grade_name
        break

st.markdown(f"""
<div class="section-subbox" style="margin-top:0px;">
    <span style="font-size:1.2rem;">Predicted Overall Grade: <b style="color:#8a206f;">{predicted_grade}</b></span>
</div>
""", unsafe_allow_html=True)

if predicted_grade == "U":
    st.error("You need to resit the diploma.")
elif predicted_grade in ["PPP", "MPP", "MMP"]:
    st.warning("Pass")
elif predicted_grade in ["MMM", "DMM", "DDM"]:
    st.info("Merit")
else:
    st.success("Distinction")

# --- WHAT-IF SIMULATION: Highlight units that could bump your grade ---
whatif_units = []
if next_grade_points:
    for unit, glh in units.items():
        current_grade = unit_grades[unit]
        if current_grade == "D":
            continue  # Already max
        grade_index = grade_options.index(current_grade)
        next_grade = grade_options[grade_index + 1] if grade_index + 1 < len(grade_options) else current_grade
        if next_grade == current_grade:
            continue
        upgraded_points = total_points - (points_per_glh[glh][current_grade] if current_grade != "U" else 0) + (points_per_glh[glh][next_grade] if next_grade != "U" else 0)
        if upgraded_points >= next_grade_points:
            whatif_units.append(unit)

if whatif_units:
    st.info(f"If you improve any of these units by one grade, you'll reach the next overall grade ({next_grade_name}):\n\n" +
            "\n".join([f"- {u}" for u in whatif_units]))

# --- Visualization: Bar chart of points per unit (with correct separation and what-if highlight) ---
df = pd.DataFrame(unit_points_list)
unit_order = list(units.keys())
df['Unit'] = pd.Categorical(df['Unit'], categories=unit_order, ordered=True)
df['WhatIf'] = df['Unit'].apply(lambda u: u in whatif_units)

if df['Points'].sum() == 0:
    st.info("No points to display yet. Select grades above to see your progress!")
else:
    # Conditional color: gold for what-if, otherwise purple scale
    bar = alt.Chart(df, height=alt.Step(48)).mark_bar(
        size=28,
        cornerRadiusTopLeft=8,
        cornerRadiusTopRight=8
    ).encode(
        x=alt.X('Points', title='Points', axis=alt.Axis(labelFontSize=14, titleFontSize=16)),
        y=alt.Y('Unit', sort=unit_order, title='Unit', axis=alt.Axis(labelFontSize=14, titleFontSize=16)),
        color=alt.condition(
            alt.datum.WhatIf,
            alt.value('gold'),
            alt.Color('Points:Q',
                      scale=alt.Scale(domain=[0, 9, 12, 16, 20, 24, 32],
                                      range=["#ece0f2", "#c47bc8", "#8a206f", "#6a1653", "#4c0f3a", "#2d0821", "#1a0412"]),
                      legend=None)
        ),
        tooltip=[
            alt.Tooltip('Unit'),
            alt.Tooltip('Points', format='.0f'),
            alt.Tooltip('Grade'),
            alt.Tooltip('WhatIf', title='Upgrade this unit to reach next grade?')
        ]
    ).properties(
        title=alt.TitleParams(
            text='Points Earned per Unit',
            fontSize=20,
            font='Segoe UI',
            anchor='start',
            color='#8a206f'
        ),
        width=700
    ).configure_axis(
        grid=False
    ).configure_view(
        strokeWidth=0
    ).configure_title(
        fontSize=22,
        font='Segoe UI',
        anchor='start',
        color='#8a206f'
    )

    st.altair_chart(bar, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)
