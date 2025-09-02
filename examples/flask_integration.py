from flask import Flask, request, jsonify, render_template
import os
import tempfile
from voice_analytics import VoiceAnalyzer, VoiceVisualizer, VoicePattern

app = Flask(__name__)

# Initialize voice analytics components
analyzer = VoiceAnalyzer()
visualizer = VoiceVisualizer()

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze_audio():
    """API endpoint to analyze uploaded audio"""
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400
        
    audio_file = request.files['audio']
    if not audio_file.filename:
        return jsonify({"error": "No selected file"}), 400
    
    # Save uploaded file to temp directory
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, audio_file.filename)
    audio_file.save(temp_path)
    
    try:
        # Reopen the file for analysis
        with open(temp_path, 'rb') as f:
            # Perform analysis
            metrics = analyzer.analyze_audio(f)
            
            # If analysis succeeded, get voice patterns
            if 'error' not in metrics:
                with open(temp_path, 'rb') as f:
                    audio_data = f.read()
                    patterns = analyzer.analyze_voice_patterns(audio_data)
                    metrics['patterns'] = patterns
                    
                    # Extract audio features
                    features = analyzer.extract_audio_features(audio_data)
                    metrics['features'] = features.to_dict()
            
            return jsonify(metrics)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        # Clean up the temp file
        if os.path.exists(temp_path):
            os.remove(temp_path)

@app.route('/api/visualize', methods=['POST'])
def create_visualization():
    """API endpoint to generate visualizations from analysis data"""
    data = request.json
    
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    viz_type = data.get('type', 'radar')
    
    try:
        if viz_type == 'radar' and 'patterns' in data:
            patterns = data['patterns']
            fig = visualizer.create_pattern_radar(patterns, title="Voice Pattern Analysis")
            return jsonify({
                "visualization": fig.to_json()
            })
            
        elif viz_type == 'dashboard' and 'metrics' in data:
            metrics = data['metrics']
            fig = visualizer.create_metrics_dashboard(metrics, title="Voice Performance")
            return jsonify({
                "visualization": fig.to_json()
            })
            
        elif viz_type == 'trends' and 'history' in data:
            history = data['history']
            fig = visualizer.create_training_trends(history, title="Voice Metrics Trends")
            return jsonify({
                "visualization": fig.to_json()
            })
            
        else:
            return jsonify({"error": "Invalid visualization type or missing data"}), 400
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/batch-analyze', methods=['POST'])
def batch_analyze():
    """API endpoint to analyze multiple audio files"""
    if 'files' not in request.files:
        return jsonify({"error": "No audio files provided"}), 400
    
    files = request.files.getlist('files')
    if not files:
        return jsonify({"error": "No selected files"}), 400
    
    results = []
    
    for audio_file in files:
        if not audio_file.filename:
            continue
            
        # Save uploaded file to temp directory
        temp_dir = tempfile.gettempdir()
        temp_path = os.path.join(temp_dir, audio_file.filename)
        audio_file.save(temp_path)
        
        try:
            # Reopen the file for analysis
            with open(temp_path, 'rb') as f:
                # Perform analysis
                metrics = analyzer.analyze_audio(f)
                metrics['filename'] = audio_file.filename
                results.append(metrics)
                
        except Exception as e:
            results.append({
                "filename": audio_file.filename,
                "error": str(e)
            })
        finally:
            # Clean up the temp file
            if os.path.exists(temp_path):
                os.remove(temp_path)
    
    return jsonify({
        "batch_results": results,
        "total_processed": len(results),
        "success_count": len([r for r in results if 'error' not in r])
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
