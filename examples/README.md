# TemporalVoiceSDK — Examples

This directory contains example applications that demonstrate how to integrate the `TemporalVoiceSDK` into different types of applications.

---

## 📦 Examples Overview

### 1. Streamlit Integration (`streamlit_integration.py`)

A Streamlit web application for interactive voice analysis and visualization.

**Features:**
- Upload and play audio files
- Analyze voice patterns using `VoiceAnalyzer`
- Generate radar visualizations using `VoiceVisualizer`
- Toggle dark/light themes
- Extract audio features in real-time

**Run with:**
```bash
pip install temporalvoicesdk streamlit
streamlit run streamlit_integration.py
```

---

### 2. Flask API Integration (`flask_integration.py`)

A simple Flask web API showing how to serve the SDK via HTTP.

**Features:**
- REST endpoints for voice analysis
- Single file and batch processing
- Dynamic radar chart generation
- Minimal frontend for quick testing

**Run with:**
```bash
pip install temporalvoicesdk flask flask-cors
python flask_integration.py
```

> Open your browser at: http://localhost:5000

---

## 🛠 Customization Ideas

### For Streamlit

- Add login/auth to store user analysis history
- Connect to a database to store voice metrics
- Customize layout and branding for production

### For Flask API

- Add JWT or API key-based authentication
- Deploy with gunicorn or uvicorn + nginx
- Add logging, monitoring, and database layers

---

## 🔌 Other Integration Targets

You can integrate this SDK into many environments:

| App Type              | Integration Notes |
|-----------------------|-------------------|
| **Desktop (PyQt, Tkinter)** | Build GUI-based voice tools |
| **Command Line Tools** | Use in batch processing or automation |
| **Backend Services**   | Serve as microservice or middleware |
| **Jupyter Notebooks**  | Interactive data science exploration |

---

## 📚 Resources

- Main SDK Documentation: [README.md in root](../README.md)
- Licensing and usage tiers: [LICENSE](../LICENSE)
- API Reference: See inline code comments and docstrings
- SDK Source: [TemporalVoiceSDK on GitHub](https://github.com/TemporalAITech/TemporalVoiceSDK)

---

© 2023–2025 Temporal AI Technologies Inc. All Rights Reserved.
