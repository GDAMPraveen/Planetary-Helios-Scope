import streamlit as st
import base64

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Planetary Helioscope AI Engine",
    page_icon="🌌",
    layout="wide"
)

# =========================================================
# LOAD GIF
# =========================================================

def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

galaxy_gif = get_base64("assets/universe.gif")

# =========================================================
# MAIN CSS
# =========================================================

st.markdown(f"""
<style>

/* Hide Streamlit Default UI */

#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

header {{
    visibility: hidden;
}}

/* Main App */

.stApp {{
    background: #020611;
    overflow: hidden;
    color: white;
}}

/* Dark Overlay */

.stApp::after {{

    content: "";

    position: fixed;

    inset: 0;

    background:
    linear-gradient(
        rgba(0,0,0,0.45),
        rgba(0,0,0,0.72)
    );

    z-index: -50;
}}

/* Remove Top Padding */

.block-container {{
    padding-top: 1rem;
}}

/* Main Title */

.main-title {{

    font-size: 4.5rem;

    font-weight: 900;

    text-align: center;

    margin-top: 70px;

    margin-bottom: 15px;

    color: white;

    text-shadow:
        0 0 10px #00d4ff,
        0 0 25px #9b59b6,
        0 0 40px #00d4ff;
}}

/* Subtitle */

.sub-title {{

    text-align: center;

    font-size: 1.3rem;

    color: #dfe6e9;

    margin-bottom: 70px;

    line-height: 1.7;
}}

/* Portal Cards */

.portal-card {{

    background: rgba(10,15,30,0.52);

    border-radius: 24px;

    padding: 35px;

    border: 1px solid rgba(255,255,255,0.08);

    backdrop-filter: blur(6px);

    text-align: center;

    transition: 0.4s;

    box-shadow:
        0 8px 30px rgba(0,0,0,0.5);

    min-height: 330px;
}}

/* Hover Effects */

.portal-card:hover {{

    transform: translateY(-10px);

    border: 1px solid rgba(0,212,255,0.45);

    box-shadow:
        0 0 30px rgba(0,212,255,0.30);
}}

/* Card Title */

.card-title {{

    font-size: 1.5rem;

    font-weight: bold;

    margin-top: 15px;

    margin-bottom: 15px;
}}

/* Card Text */

.card-text {{

    color: #dcdde1;

    line-height: 1.8;

    font-size: 0.96rem;
}}

/* Buttons */

.stButton > button {{

    width: 100%;

    height: 52px;

    border-radius: 14px;

    border: none;

    font-size: 1rem;

    font-weight: bold;

    color: white;

    background:
    linear-gradient(
        90deg,
        #00d4ff,
        #6c5ce7
    );

    transition: 0.3s;
}}

/* Button Hover */

.stButton > button:hover {{

    transform: scale(1.03);

    box-shadow:
        0 0 20px rgba(0,212,255,0.55);
}}

</style>
""", unsafe_allow_html=True)

# =========================================================
# CINEMATIC UNIVERSE BACKGROUND
# =========================================================

st.markdown(
    f"""
    <style>

    /* Main Cosmic Background */

    .stApp {{

        background:
        radial-gradient(circle at center,
        #1d2142 0%,
        #11162f 30%,
        #090d1f 60%,
        #020611 100%);

        overflow: hidden;
    }}

    /* Animated Galaxy Layer */

    .gif-background {{

        position: fixed;

        top: 0;
        left: 0;

        width: 100vw;
        height: 100vh;

        display: flex;

        justify-content: center;
        align-items: center;

        overflow: hidden;

        z-index: -100;
    }}

    .gif-background img {{

        width: 210vw;

        height: 210vh;

        object-fit: fill;

        opacity: 0.92;

        filter:
            brightness(1.08)
            saturate(1.18)
            drop-shadow(0 0 50px #3b82f6)
            drop-shadow(0 0 100px #8b5cf6);
    }}

    /* Dark Universe Overlay */

    .stApp::after {{

        content: "";

        position: fixed;

        inset: 0;

        background:
        radial-gradient(
            circle at center,
            rgba(0,212,255,0.06),
            rgba(0,0,0,0.42) 45%,
            rgba(0,0,0,0.82) 100%
        );

        z-index: -50;
    }}

    /* Main Content Layer */

    .main {{
        position: relative;
        z-index: 1;
    }}

    div.block-container {{
        position: relative;
        z-index: 1;
    }}

    </style>

    <div class="gif-background">
        <img src="data:image/gif;base64,{galaxy_gif}">
    </div>

    """,
    unsafe_allow_html=True
)
# =========================================================
# HERO SECTION
# =========================================================

st.markdown("""
<div class="main-title">
🚀 PLANETARY HELIOSCOPE AI ENGINE
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sub-title">

Monitoring Solar Storms, Lunar Tides and Tectonic Systems<br>

Using Artificial Intelligence, Space Analytics and Scientific Modeling

</div>
""", unsafe_allow_html=True)

# =========================================================
# MODULE CARDS
# =========================================================

col1, col2, col3 = st.columns(3)

# =========================================================
# SOLAR CARD
# =========================================================

with col1:

    st.markdown("""
    <div class="portal-card">

    <h1 style="font-size:4rem;">☀️</h1>

    <div class="card-title">
    Solar Storm Intelligence
    </div>

    <div class="card-text">

    Monitor solar winds,
    geomagnetic disturbances,
    proton density,
    radar instability,
    and GPS disruption systems.

    </div>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("ENTER SOLAR GRID"):
        st.switch_page("pages/1_☀️_Solar.py")

# =========================================================
# LUNAR CARD
# =========================================================

with col2:

    st.markdown("""
    <div class="portal-card">

    <h1 style="font-size:4rem;">🌊</h1>

    <div class="card-title">
    Lunar Tidal Intelligence
    </div>

    <div class="card-text">

    Analyze moon driven tides,
    ocean deformation,
    coastal flooding,
    marine instability,
    and gravitational interactions.

    </div>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("ENTER TIDAL SYSTEM"):
        st.switch_page("pages/3_🌊_Lunar_Tides.py")
    

# =========================================================
# TECTONIC CARD
# =========================================================

with col3:

    st.markdown("""
    <div class="portal-card">

    <h1 style="font-size:4rem;">🌋</h1>

    <div class="card-title">
    Tectonic Plate Intelligence
    </div>

    <div class="card-text">

    Observe seismic stress,
    mantle fractures,
    tectonic movement,
    crustal shifts,
    and earthquake analytics.

    </div>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("ENTER TECTONIC CORE"):
        st.switch_page("pages/2_🌋_Tectonic_Plates.py")
    
# =========================================================
# FOOTER
# =========================================================

st.write("")
st.write("")
st.write("")

st.markdown("""
<div style='text-align:center;color:#b2bec3;font-size:0.95rem;'>

Planetary Helioscope Monitoring Framework<br>

AI + Machine Learning + Space Analytics

</div>
""", unsafe_allow_html=True)