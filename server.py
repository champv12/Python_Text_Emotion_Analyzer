#importing packages
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#initiating flask app
app = Flask("Emotion Detection")

#running application
@app.route('/emotionDetector')
def emo_dectector():
    #retrieving input
    emotion_to_detect = request.args.get('textToAnalyze')
    
    #running emotion_detector and storing result
    result = emotion_detector(emotion_to_detect)
    
    #extracting emotions from result
    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']

    #returning result
    return f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}. The dominant emotion is {dominant_emotion}"

#rendering html 
@app.route("/")
def render_index_page():
    return render_template('index.html')

#running application on localhost:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)