# =========================================================
# IMPORTS
# =========================================================

import streamlit as st
import base64
import requests
import plotly.graph_objects as go
import numpy as np

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Solar Storm Intelligence",
    page_icon="☀️",
    layout="wide"
)

# =========================================================
# LOAD BACKGROUND IMAGE
# =========================================================

def get_base64(file_path):

    with open(file_path, "rb") as f:
        data = f.read()

    return base64.b64encode(data).decode()

solar_bg = get_base64("assets/solar.jpg")
# =========================================================
# LIVE NOAA DATA
# =========================================================

try:

    kp_url = "https://services.swpc.noaa.gov/json/planetary_k_index_1m.json"

    kp_data = requests.get(kp_url).json()

    latest_kp = float(kp_data[-1]["kp"])

except:

    latest_kp = 3.0

try:

    solar_url = "https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json"

    solar_data = requests.get(solar_url).json()

    latest_row = solar_data[-1]

    live_density = float(latest_row[1])
    live_speed = float(latest_row[2])

except:

    live_density = 8
    live_speed = 450

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

/* Background */

.stApp {{

    background:
    linear-gradient(
        rgba(0,0,0,0.55),
        rgba(0,0,0,0.80)
    ),
    url("data:image/jpeg;base64,{solar_bg}");

    background-size: cover;

    background-position: center;

    background-repeat: no-repeat;

    background-attachment: fixed;

    color: white;
}}

/* Spacing */

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
        0 0 10px #ff7b00,
        0 0 30px #ff3c00,
        0 0 60px #ffae00;
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

    background: rgba(20,8,0,0.65);

    border-radius: 24px;

    padding: 28px;

    border: 1px solid rgba(255,140,0,0.18);

    backdrop-filter: blur(12px);

    box-shadow:
        0 0 25px rgba(255,120,0,0.18);
}}

/* Metrics */

[data-testid="metric-container"] {{

    background: rgba(0,0,0,0.30);

    border-radius: 14px;

    border: 1px solid rgba(255,140,0,0.15);

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

☀️ SOLAR STORM INTELLIGENCE GRID

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sub-title">

Monitoring Heliospheric Plasma Dynamics,
Geomagnetic Disturbances and Satellite Disruption Systems

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
        color:#ffb347;
        margin-bottom:15px;
    ">
    ☀️ Solar Monitoring AI
    </h2>

    <p style="
        line-height:1.9;
        color:#f1f2f6;
    ">

    Real-time heliospheric monitoring system
    powered using NOAA space weather feeds,
    AI analytics and plasma prediction models.

    Features include:

    • Solar Wind Monitoring  
    • Proton Density Analytics  
    • Kp Geomagnetic Index  
    • Radar Disruption Detection  
    • GPS Instability Analytics  

    </p>

    </div>
    """, unsafe_allow_html=True)

with hero_right:

    st.video("assets/solar.mp4")
# =========================================================
# LIVE METRICS
# =========================================================

st.write("")

m1, m2, m3 = st.columns(3)

with m1:

    st.metric(
        "☀️ Live Solar Wind",
        f"{live_speed} km/s"
    )

with m2:

    st.metric(
        "🧲 Live Kp Index",
        latest_kp
    )

with m3:

    st.metric(
        "⚛️ Proton Density",
        f"{live_density} p/cm³"
    )
# =========================================================
# MAIN DASHBOARD
# =========================================================

st.write("")
st.write("")

left, right = st.columns([0.95,1.4])

# =========================================================
# HISTORICAL SOLAR EVENT CASE STUDIES
# =========================================================

st.write("")
st.write("")

st.markdown("""
<h2 style="
    color:white;
    text-align:center;
    margin-bottom:30px;
    text-shadow:
        0 0 10px #ff7b00,
        0 0 25px #ff3c00;
">
📚 Historical Solar Storm Case Studies
</h2>
""", unsafe_allow_html=True)

case1, case2 = st.columns(2)

# =========================================================
# CASE STUDY 1
# =========================================================

with case1:

    st.markdown("""
    <div class="data-card">

    <h3 style="
        color:#ffb347;
        margin-bottom:20px;
        font-size:1.7rem;
    ">
    ☀️ 1999 Geomagnetic Storm
    </h3>

    <p style="
        color:#f1f2f6;
        line-height:1.9;
        font-size:1rem;
    ">

    A strong geomagnetic disturbance affected
    satellite telemetry systems and radio
    communication channels across multiple regions.

    Observed Effects:

    • GPS navigation instability  
    • Radar propagation interference  
    • Auroral intensification  
    • Communication signal degradation  
    • Plasma density fluctuations  

    This event became a major scientific
    reference point in heliophysics monitoring.

    </p>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# CASE STUDY 2
# =========================================================

with case2:

    st.markdown("""
    <div class="data-card">

    <h3 style="
        color:#ff884d;
        margin-bottom:20px;
        font-size:1.7rem;
    ">
    🌞 2022 Solar Plasma Surge
    </h3>

    <p style="
        color:#f1f2f6;
        line-height:1.9;
        font-size:1rem;
    ">

    A powerful solar plasma ejection disrupted
    several low-earth orbit satellite systems
    during elevated geomagnetic activity.

    Scientific Impacts:

    • Increased atmospheric drag  
    • Satellite orbital instability  
    • Communication fluctuations  
    • Space weather alert escalation  
    • GPS positional anomalies  

    The event accelerated global research
    into AI-driven solar prediction systems.

    </p>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# LEFT PANEL
# =========================================================

with left:

    st.markdown('<div class="data-card">', unsafe_allow_html=True)

    st.subheader("🛰️ Telemetry Controls")

    solar_speed = st.slider(
        "Solar Wind Velocity",
        300, 900, int(live_speed)
    )

    proton_density = st.slider(
        "Proton Density",
        1, 50, int(live_density)
    )

    kp_index = st.slider(
        "Geomagnetic Kp Index",
        0, 9, int(latest_kp)
    )

    radar_loss = round(
        (solar_speed / 120) + (kp_index * 2.8),
        2
    )

    gps_error = round(
        (proton_density * 0.7) + (kp_index * 4.5),
        2
    )

    threat_level = "LOW"

    if kp_index >= 6:
        threat_level = "EXTREME"

    elif kp_index >= 4:
        threat_level = "HIGH"

    elif kp_index >= 2:
        threat_level = "MODERATE"

    st.write("")

    st.metric(
        "📡 Radar Signal Loss",
        f"{radar_loss} dB"
    )

    st.metric(
        "🛰️ GPS Position Error",
        f"{gps_error} m"
    )

    st.metric(
        "⚠️ Solar Threat",
        threat_level
    )

    st.markdown("</div>", unsafe_allow_html=True)
# =========================================================
# RIGHT GRAPH PANEL
# =========================================================

with right:

    st.markdown('<div class="data-card">', unsafe_allow_html=True)

    st.subheader("📈 Heliospheric Plasma Activity")

    x = np.arange(0, 24, 1)

    y = (
        np.sin(x / 3) * proton_density +
        solar_speed / 100 +
        kp_index
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

        height=500,

        margin=dict(
            l=20,
            r=20,
            t=30,
            b=20
        )
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

st.subheader("🤖 AI Space Weather Analysis")

if kp_index >= 6:

    ai_text = """
    Severe geomagnetic instability detected.

    High probability of:
    • GPS disruption
    • Satellite instability
    • Radar propagation errors
    • Communication fluctuations

    Immediate monitoring recommended.
    """

elif kp_index >= 4:

    ai_text = """
    Elevated solar activity detected.

    Moderate plasma fluctuations may affect:
    • Low orbit satellites
    • Polar communication
    • Navigation systems
    """

else:

    ai_text = """
    Stable heliospheric conditions detected.

    Minimal geomagnetic disturbances observed.
    Space weather environment currently stable.
    """

st.write(ai_text)

st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# ADVANCED AI THREAT ANALYSIS
# =========================================================

st.write("")
st.write("")

st.markdown("""
<div class="data-card">
""", unsafe_allow_html=True)

st.markdown("""
<h2 style="
    color:#ffd369;
    margin-bottom:20px;
">
🤖 AI Solar Threat Intelligence Engine
</h2>
""", unsafe_allow_html=True)

# =========================================================
# AI LOGIC
# =========================================================

solar_risk_score = (
    (solar_speed / 100)
    + (proton_density * 0.8)
    + (kp_index * 4)
)

solar_risk_score = round(solar_risk_score, 2)

if solar_risk_score >= 50:

    risk_status = "EXTREME"

    ai_message = """
    Severe heliospheric instability detected.

    AI analysis predicts elevated probability of:

    • Satellite communication disruption
    • High radar signal attenuation
    • GPS instability events
    • Magnetospheric turbulence
    • Plasma propagation anomalies

    Immediate scientific monitoring recommended.
    """

elif solar_risk_score >= 35:

    risk_status = "HIGH"

    ai_message = """
    Elevated solar activity detected.

    AI models indicate moderate geomagnetic
    fluctuations capable of affecting:

    • Navigation systems
    • Low orbit satellites
    • Polar communication systems
    • Radio propagation channels
    """

elif solar_risk_score >= 20:

    risk_status = "MODERATE"

    ai_message = """
    Moderate heliospheric plasma variation detected.

    Minor geomagnetic instability possible,
    but large-scale disruption probability
    remains limited.
    """

else:

    risk_status = "LOW"

    ai_message = """
    Stable solar conditions detected.

    Minimal geomagnetic disturbance observed.
    Space weather environment currently stable.
    """

# =========================================================
# DISPLAY METRICS
# =========================================================

m1, m2 = st.columns(2)

with m1:

    st.metric(
        "☀️ AI Solar Risk Score",
        solar_risk_score
    )

with m2:

    st.metric(
        "⚠️ Threat Classification",
        risk_status
    )

st.write("")

st.markdown(f"""
<div style="
    color:#f1f2f6;
    line-height:1.9;
    font-size:1rem;
">

{ai_message}

</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
# =========================================================
# LIVE NOAA STATUS BANNER
# =========================================================

st.write("")

if latest_kp >= 6:

    banner_color = "#ff2e63"
    banner_text = "EXTREME GEOMAGNETIC DISTURBANCE DETECTED"

elif latest_kp >= 4:

    banner_color = "#ff884d"
    banner_text = "HIGH SOLAR ACTIVITY OBSERVED"

elif latest_kp >= 2:

    banner_color = "#ffd369"
    banner_text = "MODERATE SOLAR FLUCTUATIONS ACTIVE"

else:

    banner_color = "#00e676"
    banner_text = "SOLAR CONDITIONS STABLE"

st.markdown(f"""
<div style="
    background:{banner_color};
    padding:18px;
    border-radius:18px;
    text-align:center;
    font-size:1.1rem;
    font-weight:bold;
    color:white;
    box-shadow:
        0 0 25px {banner_color};
">

🚨 {banner_text}

</div>
""", unsafe_allow_html=True)
# =========================================================
# AUTO REFRESH
# =========================================================

st.write("")

refresh = st.button("🔄 Refresh Live NOAA Data")

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

Solar Intelligence Monitoring Framework<br>

AI + Space Weather Analytics + Plasma Dynamics

</div>

""", unsafe_allow_html=True)
