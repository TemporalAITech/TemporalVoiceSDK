from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="voice-analytics",
    version="0.1.0",
    author="Temporal AI Technologies Inc.",
    author_email="info@temporalai.com",
    description="A package for advanced voice pattern recognition and visualization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/temporalai/voice-analytics",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.19.0",
        "pandas>=1.1.0",
        "plotly>=4.14.0",
        "SpeechRecognition>=3.8.0",
        "scikit-learn>=0.24.0",
    ],
)
