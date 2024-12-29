"""
Emotion Detection Flask Application
This module implements a Flask app to analyze emotions from a given text using
an external emotion detection library.
"""

# Importing packages
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiating Flask app
app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def emo_detector():
    """
    Analyze emotions from the given text using the emotion_detector function.
    """
    # Retrieving input
    emotion_to_detect = request.args.get('textToAnalyze')
    # Check for empty or invalid text
    if not emotion_to_detect or not emotion_to_detect.strip():
        return "Invalid text! Please try again.", 400

    # Running emotion_detector and storing result
    result = emotion_detector(emotion_to_detect)
    # Handle case where dominant_emotion is None
    if result.get('dominant_emotion') is None:
        return "Invalid text! Please try again.", 400

    # Extracting emotions from result
    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']

    # Returning result
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Render the index HTML page for the application.
    """
    return render_template('index.html')

# Running application on localhost:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
