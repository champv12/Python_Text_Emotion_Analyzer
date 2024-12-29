import requests
import json

def emotion_detector(text_to_analyze):
    # Parameters for API POST request
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    # Posting input to API and receiving response
    response = requests.post(url, json=input_json, headers=headers)
    
    if response.status_code == 200:
        # Converting response to JSON
        response_dict = response.json()
        
        # Extracting required emotion scores
        emotion_data = response_dict.get("emotionPredictions", [{}])[0].get("emotion", {})
        anger_score = emotion_data.get('anger', 0)
        disgust_score = emotion_data.get('disgust', 0)
        fear_score = emotion_data.get('fear', 0)
        joy_score = emotion_data.get('joy', 0)
        sadness_score = emotion_data.get('sadness', 0)
        
        # Finding dominant emotion
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Returning results output
        result = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 400:
        # Handling invalid input
        result = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        # General error handling
        result = {
            'error': f"Unexpected error: {response.status_code}",
            'details': response.text
        }
    
    return result