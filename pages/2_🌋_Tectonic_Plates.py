# =========================================================
# IMPORTS
# =========================================================

import streamlit as st
import base64
import requests
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Tectonic Plate Intelligence",
    page_icon="🌋",
    layout="wide"
)

# =========================================================
# LOAD BACKGROUND IMAGE
# =========================================================

def get_base64(file_path):

    with open(file_path, "rb") as f:
        data = f.read()

    return base64.b64encode(data).decode()

tectonic_bg = get_base64("assets/tectonic.jpg")

# =========================================================
# LIVE EARTHQUAKE DATA (USGS)
# =========================================================

try:

    usgs_url = """
    https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson
    """

    quake_data = requests.get(usgs_url).json()

    latest_quake = quake_data["features"][0]

    quake_mag = latest_quake["properties"]["mag"]

    quake_place = latest_quake["properties"]["place"]

    quake_time = latest_quake["properties"]["time"]

except:

    quake_mag = 4.5
    quake_place = "Pacific Plate Boundary"
    quake_time = "N/A"

# =========================================================
# CSS
# =========================================================

st.markdown(f"""
<style>

/* Hide Streamlit */

#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

header {{
    visibility: hidden;
}}

/* Main Background */

.stApp {{

    background:
    linear-gradient(
        rgba(0,0,0,0.58),
        rgba(0,0,0,0.84)
    ),
    url("data:image/jpeg;base64,{tectonic_bg}");

    background-size: cover;

    background-position: center;

    background-repeat: no-repeat;

    background-attachment: fixed;

    color: white;
}}

/* Layout */

.block-container {{

    padding-top: 1rem;

    padding-left: 3rem;

    padding-right: 3rem;
}}

/* Title */

.main-title {{

    font-size: 4rem;

    font-weight: 900;

    text-align: center;

    color: white;

    margin-top: 10px;

    text-shadow:
        0 0 10px #ff3c00,
        0 0 30px #ff5722,
        0 0 60px #ff9800;
}}

/* Subtitle */

.sub-title {{

    text-align: center;

    font-size: 1.1rem;

    color: #f1f2f6;

    margin-bottom: 35px;

    line-height: 1.7;
}}

/* Cards */

.data-card {{

    background: rgba(25,10,0,0.68);

    border-radius: 24px;

    padding: 28px;

    border: 1px solid rgba(255,120,0,0.18);

    backdrop-filter: blur(12px);

    box-shadow:
        0 0 25px rgba(255,100,0,0.18);
}}

/* Metrics */

[data-testid="metric-container"] {{

    background: rgba(0,0,0,0.28);

    border-radius: 14px;

    border: 1px solid rgba(255,120,0,0.15);

    padding: 14px;
}}

[data-testid="metric-container"] * {{
    color: white !important;
}}

/* Video */

.stVideo {{

    border-radius: 22px;

    overflow: hidden;

    border: 1px solid rgba(255,140,0,0.20);
}}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================

st.markdown("""
<div class="main-title">

🌋 TECTONIC PLATE INTELLIGENCE GRID

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sub-title">

Monitoring Crustal Dynamics,
Seismic Instability and Mantle Stress Propagation

</div>
""", unsafe_allow_html=True)

# =========================================================
# HERO SECTION
# =========================================================

hero_left, hero_right = st.columns([1.1,1])

with hero_left:

    st.markdown("""
    <div class="data-card">

    <h2 style="
        color:#ff884d;
        margin-bottom:15px;
    ">
    🌋 Seismic Monitoring AI
    </h2>

    <p style="
        line-height:1.9;
        color:#f1f2f6;
    ">

    AI-driven tectonic intelligence system
    monitoring global crustal instability,
    seismic stress propagation and plate movement.

    Features include:

    • Earthquake Magnitude Analytics  
    • Plate Boundary Monitoring  
    • Mantle Stress Detection  
    • Seismic Energy Tracking  
    • Fault Instability Modeling  

    </p>

    </div>
    """, unsafe_allow_html=True)

with hero_right:

    st.video("assets/tectonic.mp4")

# =========================================================
# LIVE METRICS
# =========================================================

st.write("")

m1, m2, m3 = st.columns(3)

with m1:

    st.metric(
        "🌍 Latest Magnitude",
        quake_mag
    )

with m2:

    st.metric(
        "📍 Active Region",
        quake_place[:25]
    )

with m3:

    st.metric(
        "⚡ Seismic Status",
        "ACTIVE"
    )

# =========================================================
# HISTORICAL CASE STUDIES
# =========================================================

st.write("")
st.write("")

case1, case2 = st.columns(2)

with case1:

    st.markdown("""
    <div class="data-card">

    <h3 style="
        color:#ffb347;
        margin-bottom:20px;
    ">
    🌏 2004 Indian Ocean Earthquake
    </h3>

    <p style="
        color:#f1f2f6;
        line-height:1.9;
    ">

    One of the deadliest tectonic events
    ever recorded.

    Major effects included:

    • Massive tsunami generation  
    • Crustal displacement  
    • Plate boundary rupture  
    • Oceanic stress propagation  
    • Global seismic wave transmission  

    Magnitude exceeded 9.0 on the Richter scale.

    </p>

    </div>
    """, unsafe_allow_html=True)

with case2:

    st.markdown("""
    <div class="data-card">

    <h3 style="
        color:#ff884d;
        margin-bottom:20px;
    ">
    🌋 2011 Japan Tectonic Event
    </h3>

    <p style="
        color:#f1f2f6;
        line-height:1.9;
    ">

    A catastrophic megathrust earthquake
    caused severe crustal displacement.

    Observed impacts:

    • Tsunami propagation  
    • Nuclear infrastructure risk  
    • Mantle instability  
    • Plate movement acceleration  
    • Seismic aftershock cascades  

    This event transformed global seismic analytics.

    </p>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# MAIN DASHBOARD
# =========================================================

st.write("")
st.write("")

left, right = st.columns([0.95,1.4])

# =========================================================
# LEFT PANEL
# =========================================================

with left:

    st.markdown('<div class="data-card">', unsafe_allow_html=True)

    st.subheader("🛰️ Seismic Controls")

    magnitude = st.slider(
        "Earthquake Magnitude",
        1.0, 10.0, float(quake_mag)
    )

    depth = st.slider(
        "Crustal Depth (km)",
        1, 700, 120
    )

    stress = st.slider(
        "Mantle Stress Index",
        1, 100, 42
    )

    seismic_energy = round(
        magnitude * stress * 1.8,
        2
    )

    rupture_risk = round(
        (magnitude * 8) + (stress / 2),
        2
    )

    danger = "LOW"

    if magnitude >= 8:
        danger = "EXTREME"

    elif magnitude >= 6:
        danger = "HIGH"

    elif magnitude >= 4:
        danger = "MODERATE"

    st.write("")

    st.metric(
        "⚡ Seismic Energy",
        seismic_energy
    )

    st.metric(
        "🌋 Rupture Risk",
        rupture_risk
    )

    st.metric(
        "🚨 Threat Level",
        danger
    )

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# GRAPH PANEL
# =========================================================

with right:

    st.markdown('<div class="data-card">', unsafe_allow_html=True)

    st.subheader("📈 Crustal Stress Propagation")

    x = np.arange(0, 24, 1)

    y = (
        np.sin(x / 2) * stress +
        magnitude * 8
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode='lines',
            fill='tozeroy',
            line=dict(width=4)
        )
    )

    fig.update_layout(

        paper_bgcolor='rgba(0,0,0,0)',

        plot_bgcolor='rgba(0,0,0,0)',

        font=dict(color='white'),

        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# AI ANALYSIS ENGINE
# =========================================================

st.write("")
st.write("")

st.markdown("""
<div class="data-card">
""", unsafe_allow_html=True)

st.subheader("🤖 AI Seismic Threat Analysis")

risk_score = round(
    (magnitude * 10) +
    (stress * 0.9) +
    (depth / 15),
    2
)

if risk_score >= 120:

    ai_text = """
    Extreme tectonic instability detected.

    AI models predict elevated probability of:

    • Major crustal rupture
    • High seismic wave propagation
    • Tsunami generation risk
    • Aftershock cascades
    • Mantle instability escalation
    """

elif risk_score >= 80:

    ai_text = """
    Significant tectonic stress detected.

    Moderate seismic instability may affect:

    • Plate boundaries
    • Urban seismic zones
    • Fault propagation regions
    """

else:

    ai_text = """
    Stable tectonic conditions observed.

    Minimal crustal instability currently detected.
    """

st.metric(
    "🌋 AI Seismic Risk Score",
    risk_score
)

st.write(ai_text)

st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# ALERT BANNER
# =========================================================

st.write("")

if magnitude >= 8:

    banner = "#ff1744"
    text = "EXTREME TECTONIC INSTABILITY DETECTED"

elif magnitude >= 6:

    banner = "#ff9100"
    text = "HIGH SEISMIC ACTIVITY OBSERVED"

else:

    banner = "#00c853"
    text = "TECTONIC CONDITIONS STABLE"

st.markdown(f"""
<div style="
    background:{banner};
    padding:18px;
    border-radius:18px;
    text-align:center;
    font-size:1.1rem;
    font-weight:bold;
    color:white;
    box-shadow:
        0 0 25px {banner};
">

🚨 {text}

</div>
""", unsafe_allow_html=True)

# =========================================================
# REFRESH BUTTON
# =========================================================

st.write("")

refresh = st.button("🔄 Refresh Live Seismic Data")

if refresh:

    st.rerun()

# =========================================================
# FOOTER
# =========================================================

st.write("")
st.write("")

st.markdown("""

<div style="
text-align:center;
color:#dfe6e9;
font-size:0.95rem;
padding-bottom:20px;
">

Tectonic Intelligence Monitoring Framework<br>

AI + Seismic Analytics + Crustal Dynamics

</div>

""", unsafe_allow_html=True)