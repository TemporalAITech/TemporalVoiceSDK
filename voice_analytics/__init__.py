# Copyright (c) 2023–2025 Temporal AI Technologies Inc. All rights reserved.
# Proprietary and Confidential. Subject to license terms.
# Contact: Support@temporalaitechnologies.com

"""
Voice Analytics Package

A package for advanced voice pattern recognition and visualization.
"""

from voice_analytics.processor import VoiceAnalyzer
from voice_analytics.visualizer import VoiceVisualizer
from voice_analytics.models import VoicePattern, TrainingResult, AudioFeatures

__version__ = '0.1.0'
__all__ = [
    'VoiceAnalyzer',
    'VoiceVisualizer',
    'VoicePattern',
    'TrainingResult',
    'AudioFeatures',
]
