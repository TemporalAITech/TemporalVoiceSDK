# Voice Analytics Package Examples

This directory contains example applications demonstrating how to integrate the Voice Analytics package into various application types.

## Examples Overview

### 1. Streamlit Integration (`streamlit_integration.py`)

A Streamlit web application that demonstrates how to use Voice Analytics for interactive voice analysis and visualization.

#### Features:
- Audio file upload and playback
- Voice pattern analysis with interactive visualizations
- Customizable visualization types
- Advanced audio feature extraction
- Themed interface

#### Running the Example:
```bash
# Install required packages
pip install voice-analytics streamlit

# Run the Streamlit app
streamlit run streamlit_integration.py
```

### 2. Flask API Integration (`flask_integration.py`)

A Flask web API that demonstrates how to use Voice Analytics in a backend service.

#### Features:
- REST API endpoints for voice analysis
- Single file and batch processing
- Interactive visualization generation
- Simple web interface for testing

#### Running the Example:
```bash
# Install required packages
pip install voice-analytics flask

# Create templates directory if it doesn't exist
mkdir -p templates

# Copy the index.html file to the templates directory
cp templates/index.html templates/

# Run the Flask app
python flask_integration.py
```

Then open your browser to http://localhost:5000 to see the interface.

## Customizing the Examples

These examples are designed to be starting points for your own applications. Here are some ways you might want to customize them:

### Streamlit Example Customization:
- Add authentication and user profiles to save analysis history
- Integrate with your own database to store and retrieve voice metrics
- Customize the visualization styles and layout
- Add more advanced voice processing options

### Flask API Customization:
- Add authentication and API keys for production use
- Implement user accounts and data persistence
- Extend with additional visualization endpoints
- Deploy to a production server with WSGI

## Integration with Other Applications

The Voice Analytics package can be integrated into various application types:

1. **Desktop Applications:**
   - Use with PyQt or Tkinter for standalone desktop apps
   - Integrate with other Python GUI frameworks

2. **Command Line Tools:**
   - Create CLI tools for batch processing audio files
   - Include in automation scripts and pipelines

3. **Backend Services:**
   - Use as a microservice for voice processing
   - Integrate with other APIs and services

4. **Data Science Notebooks:**
   - Use in Jupyter notebooks for interactive analysis
   - Combine with other data science libraries

## Additional Resources

- See the main package README for complete API documentation
- Refer to the inline code comments for implementation details
- Check the package GitHub repository for updates and new examples
