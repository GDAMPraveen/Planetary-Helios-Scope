# 🪐 Planetary & HelioScope: Solar Storm, Lunar Tidal & Lithospheric Intelligence Grid

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://share.streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Data Source: NOAA API](https://img.shields.io/badge/Data%20Source-NOAA%20SWPC-orange)](https://www.swpc.noaa.gov/)

A multi-domain, real-time astrophysics and geophysical observation dashboard built with Streamlit. Planetary & HelioScope bridges heliospheric space weather monitoring, lunar tidal dynamics, and tectonic stress modeling into a unified Earth–Space interaction intelligence system.

---

## 🚀 Expanded Multi-Domain Architecture

* **☀️ Live Heliospheric Telemetry**
  Real-time space weather monitoring via NOAA SWPC including:
  * Planetary K-index ($Kp$)
  * Solar wind velocity
  * Proton density fluctuations
  * Geomagnetic storm activity tracking

* **🌙 Lunar Tidal Force Tracker**
  High-precision lunar gravitational modeling system:
  * Earth–Moon distance variation
  * Lunar phase & illumination tracking
  * Tidal strain force estimation
  * Gravitational oceanic + lithospheric coupling

* **🌍 Tectonic Micro-Strain Evaluator**
  Lithospheric stress simulation and seismic risk estimation:
  * Fault-line stress accumulation modeling
  * Crustal loading pressure estimation
  * Tidal + solar influence coupling
  * Seismic risk probability index generation

* **🔗 Resonant Co-Efficiency Engine**
  Cross-domain correlation intelligence system:
  * Solar storm $\leftrightarrow$ geomagnetic disturbance correlation
  * Lunar tidal peaks $\leftrightarrow$ crustal stress variation mapping
  * Multi-system anomaly detection
  * Predictive hazard scoring logic

---

## 📊 Core Algorithmic Framework

### 📡 Heliospheric Metrics

**Radar Loss Equation:**
$$\text{Loss (dB)} = \left(\frac{\text{Velocity}}{125}\right) + (Kp \times 2.95)$$

**GPS Positional Error:**
$$\text{Error (m)} = (\text{Proton Density} \times 0.72) + (Kp \times 4.6)$$

---

### 🌙 Lunar Geodynamics Metrics

**Lunar Tidal Displacement Force:**
$$\text{Tidal Strain} = \left(\frac{384}{\text{Lunar Distance}}\right)^3 \times 2.2$$

**Lunar Illumination Effect:**
$$\text{Illumination Factor} = \frac{1 - \cos(\theta)}{2}$$

---

### 🌍 Tectonic Geodynamics Metrics

**Tectonic Slip Risk Vector:**
$$\text{Stress Index} = (\text{Fault Loading (MPa)} \times 0.45) + (\text{Tidal Strain} \times 3.1)$$

**Seismic Trigger Probability:**
$$P(\text{Seismic Event}) = \sigma(\text{Stress Index} + \text{Solar Perturbation Factor})$$

---

## 📦 File Layout Matrix

```text
├── app.py                  # Main Streamlit Dashboard Terminal
├── pages/
│   ├── solar.py            # Solar / Heliospheric Module
│   ├── lunar.py            # Lunar Tidal Intelligence Module
│   ├── tectonic.py         # Lithospheric Stress Module
│
├── models/
│   ├── seismic_model.pkl   # ML prediction model
│
├── assets/
│   ├── solar.jpg
│   ├── solar.mp4
│   ├── lunar.jpeg
│   ├── lunar.mp4
│   ├── tectonic.jpg
│
├── requirements.txt
└── README.md
