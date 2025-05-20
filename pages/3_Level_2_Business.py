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
    <span class="custom-topbar-title">Level 2 Business Diploma Grade Calculator</span>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="main-content-canvas">', unsafe_allow_html=True)

st.markdown("""
<div style="display: flex; flex-direction: column; align-items: center;">
    <div class="section-box">
        Level 2 Business Diploma Grade Calculator
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
    "Business Purpose": 30,
    "Business Organizations": 30,
    "Financial Forecasting For Business": 30,
    "The Marketing Plan": 30,
    "People In Organizations": 30,
    "Business Online": 30,
    "Starting A Small Business": 60,
    "Working In Teams": 60,
    "Promoting And Branding In Retail Workplace": 30,
    "Running A Small Business": 60,
    "Running A Small Business (cont.)": 60,
    "The Importance Of Enterprise And Entrepreneurship": 30,
    "Social Enterprise": 30,
}

# Points per 10 GLH for Level 2 Business
points_per_10_glh = {
    "U": 0,
    "P": 4,
    "M": 6,
    "D": 8,
}

grade_options = ["U", "P", "M", "D"]

total_points = 0
unit_points_list = []  # To store points per unit for visualization
unit_grades = {}

for unit, glh in units.items():
    grade = st.selectbox(f"{unit} ({glh} GLH)", grade_options, index=0, key=unit)
    unit_grades[unit] = grade
    unit_points = points_per_10_glh[grade] * (glh / 10)
    total_points += unit_points
    unit_points_list.append({"Unit": unit, "Points": unit_points, "Grade": grade})

st.markdown(f"""
<div class="section-subbox" style="margin-top:30px;">
    <span style="font-size:1.3rem;">Total Points: <b style="color:#8a206f;">{int(total_points)}</b></span>
</div>
""", unsafe_allow_html=True)

# Grade thresholds for Level 2 Business (same as Level 2 Computing)
grade_thresholds = {
    "DD": 372,
    "D*D": 366,
    "DD (lower)": 360,
    "DM": 318,
    "MM": 276,
    "MP": 234,
    "PP": 192,
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
elif predicted_grade in ["PP", "MP", "MM"]:
    st.warning("Pass")
elif predicted_grade in ["DM", "D*D", "DD"]:
    st.info("Merit / Distinction")
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
        upgraded_points = total_points - (points_per_10_glh[current_grade] * (glh / 10)) + (points_per_10_glh[next_grade] * (glh / 10))
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
                      scale=alt.Scale(domain=[0, 12, 18, 24, 48],
                                      range=["#ece0f2", "#c47bc8", "#8a206f", "#6a1653", "#4c0f3a"]),
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
