import streamlit as st
import numpy as np
import pandas as pd
from voice_analytics import VoiceAnalyzer, VoiceVisualizer

# Page configuration
st.set_page_config(
    page_title="Voice Analytics Demo",
    page_icon="🎤",
    layout="wide"
)

# Add custom styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        color: #6236FF;
    }
    .subheader {
        font-size: 1.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
        color: #4A4A4A;
    }
    .card {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background-color: #FFFFFF;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='main-header'>Voice Analytics Integration</h1>", unsafe_allow_html=True)
st.markdown(
    "Upload audio files to analyze voice patterns and visualize the results. "
    "This demonstration shows how to integrate the Voice Analytics package into your Streamlit application."
)

# Initialize components
analyzer = VoiceAnalyzer()
visualizer = VoiceVisualizer()

# Create sidebar for settings
with st.sidebar:
    st.markdown("### Analysis Settings")
    
    theme_mode = st.radio(
        "Theme Mode",
        options=["Light", "Dark"],
        index=0
    )
    
    visualization_type = st.selectbox(
        "Visualization Type",
        options=["Radar Chart", "Dashboard", "Trends"],
        index=0
    )
    
    advanced_analysis = st.checkbox("Enable Advanced Analysis", value=True)

# Main content area - file upload and analysis
st.markdown("<h2 class='subheader'>Audio Analysis</h2>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

if uploaded_file is not None:
    # Display audio with custom styling
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Audio Player")
    st.audio(uploaded_file)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Analysis button
    analyze_button = st.button("Analyze Voice", key="analyze_btn")
    
    if analyze_button:
        with st.spinner("Analyzing audio..."):
            # Perform analysis
            metrics = analyzer.analyze_audio(uploaded_file)
            
            if 'error' in metrics:
                st.error(f"Analysis Error: {metrics['error']}")
            else:
                # Show metrics in a card
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                st.subheader("Analysis Results")
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Clarity", f"{metrics['clarity']:.2%}")
                
                with col2:
                    st.metric("Emotion", f"{metrics['emotion']:.2%}")
                
                with col3:
                    st.metric("Confidence", f"{metrics['confidence']:.2%}")
                
                # Display transcribed text
                if 'text' in metrics:
                    st.markdown("#### Transcribed Text:")
                    st.markdown(f"<div style='padding: 1rem; background-color: #F8F9FA; border-radius: 0.5rem;'>{metrics['text']}</div>", unsafe_allow_html=True)
                
                st.markdown("</div>", unsafe_allow_html=True)
                
                # Analyze voice patterns
                pattern_data = analyzer.analyze_voice_patterns(uploaded_file.getvalue())
                
                # Visualizations based on selected type
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                st.subheader("Visualizations")
                
                if visualization_type == "Radar Chart":
                    fig = visualizer.create_pattern_radar(
                        pattern_data,
                        title="Voice Pattern Analysis",
                        height=500
                    )
                    st.plotly_chart(fig, use_container_width=True)
                
                elif visualization_type == "Dashboard":
                    # Create a dashboard with the current metrics and some historical data
                    # For demo, we'll create some historical data
                    hist_metrics = {
                        'avg_clarity': metrics['clarity'],
                        'avg_emotion': metrics['emotion'],
                        'avg_confidence': metrics['confidence'],
                        'total_samples': 1,
                        'total_duration': metrics['duration']
                    }
                    
                    fig = visualizer.create_metrics_dashboard(
                        hist_metrics,
                        title="Voice Performance Dashboard",
                        height=600
                    )
                    st.plotly_chart(fig, use_container_width=True)
                
                elif visualization_type == "Trends":
                    # For demo, create historical data
                    history = []
                    for i in range(10):
                        history.append({
                            'clarity': np.random.uniform(0.5, 0.9),
                            'emotion': np.random.uniform(0.4, 0.8),
                            'confidence': np.random.uniform(0.6, 0.95),
                            'duration': np.random.uniform(1, 5),
                            'timestamp': pd.Timestamp.now() - pd.Timedelta(days=i)
                        })
                    
                    # Add current metrics
                    history.append(metrics)
                    
                    fig = visualizer.create_training_trends(
                        history,
                        title="Voice Metrics Trends",
                        height=400
                    )
                    st.plotly_chart(fig, use_container_width=True)
                
                st.markdown("</div>", unsafe_allow_html=True)
                
                # Advanced analysis section
                if advanced_analysis:
                    # Extract audio features
                    features = analyzer.extract_audio_features(uploaded_file.getvalue())
                    
                    st.markdown("<div class='card'>", unsafe_allow_html=True)
                    st.subheader("Advanced Audio Features")
                    
                    # Display features in a table
                    features_df = pd.DataFrame([features.to_dict()])
                    st.dataframe(features_df)
                    
                    st.markdown("</div>", unsafe_allow_html=True)
else:
    # Display placeholder content when no file is uploaded
    st.markdown(
        """
        <div style='padding: 3rem; background-color: #F8F9FA; border-radius: 0.5rem; text-align: center;'>
            <img src="https://raw.githubusercontent.com/streamlit/brandkit/master/variants/SVG/wave.svg" alt="Wave" style="width: 100px; margin-bottom: 1rem;">
            <h3>Upload an audio file to begin analysis</h3>
            <p>Supported formats: WAV, MP3</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

# Footer
st.markdown(
    """
    <div style='margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #EEEEEE; text-align: center; color: #888888; font-size: 0.8rem;'>
        Powered by Voice Analytics Package • © 2023-2025 Temporal AI Technologies Inc. • All Rights Reserved
    </div>
    """,
    unsafe_allow_html=True
)
