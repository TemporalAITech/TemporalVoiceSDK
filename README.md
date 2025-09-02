# Voice Analytics Package

Copyright (c) 2023-2025 Temporal AI Technologies Inc. All Rights Reserved.
Proprietary and Confidential. Subject to license terms.

## Overview

A comprehensive Python package for advanced voice pattern recognition and visualization. This package provides tools for analyzing voice recordings, extracting features, and generating interactive visualizations for voice data.

## Features

- Process audio files to extract voice patterns and features
- Analyze speech clarity, emotion, and confidence
- Generate interactive visualizations of voice patterns
- Track training progress with comprehensive metrics
- Easily integrate with other applications

## Installation

```bash
pip install voice-analytics
```

## Quick Start

### Basic Voice Analysis

```python
from voice_analytics import VoiceAnalyzer
import io

# Initialize the analyzer
analyzer = VoiceAnalyzer()

# Analyze an audio file
with open('sample.wav', 'rb') as audio_file:
    metrics = analyzer.analyze_audio(audio_file)
    
print(metrics)
```

### Visualize Voice Patterns

```python
from voice_analytics import VoiceAnalyzer, VoiceVisualizer
import plotly.io as pio

# Initialize the analyzer and visualizer
analyzer = VoiceAnalyzer()
visualizer = VoiceVisualizer()

# Analyze voice patterns from audio
with open('sample.wav', 'rb') as audio_file:
    # Get raw audio data
    audio_data = audio_file.read()
    
    # Analyze patterns
    patterns = analyzer.analyze_voice_patterns(audio_data)
    
    # Create radar chart
    fig = visualizer.create_pattern_radar(patterns, title="Voice Pattern Analysis")
    
    # Display the chart (or save it)
    pio.write_html(fig, 'voice_patterns.html')
```

### Create a Metrics Dashboard

```python
from voice_analytics import VoiceAnalyzer, VoiceVisualizer
import plotly.io as pio

# Initialize components
analyzer = VoiceAnalyzer()
visualizer = VoiceVisualizer(dark_mode=True)  # Use dark theme

# Analyze multiple audio samples
for audio_file in ['sample1.wav', 'sample2.wav', 'sample3.wav']:
    with open(audio_file, 'rb') as f:
        analyzer.analyze_audio(f)

# Get aggregate metrics
metrics = analyzer.get_training_metrics()

# Create a comprehensive dashboard
dashboard = visualizer.create_metrics_dashboard(metrics, title="Voice Performance")

# Save the dashboard
pio.write_html(dashboard, 'voice_dashboard.html')
```

## Integration with Streamlit

```python
import streamlit as st
from voice_analytics import VoiceAnalyzer, VoiceVisualizer

# Initialize components
analyzer = VoiceAnalyzer()
visualizer = VoiceVisualizer()

# File upload in Streamlit
uploaded_file = st.file_uploader("Upload audio sample", type=['wav', 'mp3'])

if uploaded_file:
    # Display audio player
    st.audio(uploaded_file)
    
    # Analyze audio
    metrics = analyzer.analyze_audio(uploaded_file)
    
    # Display metrics
    st.write("Analysis Results:", metrics)
    
    # Display visualizations
    if metrics and 'error' not in metrics:
        # Create pattern visualization
        patterns = analyzer.analyze_voice_patterns(uploaded_file.getvalue())
        fig_radar = visualizer.create_pattern_radar(patterns, title="Voice Pattern Analysis")
        st.plotly_chart(fig_radar, use_container_width=True)
        
        # Display transcribed text
        if 'text' in metrics:
            st.subheader("Transcribed Text")
            st.write(metrics['text'])
```

## License

This software is licensed under a proprietary license. See the LICENSE file for details.
