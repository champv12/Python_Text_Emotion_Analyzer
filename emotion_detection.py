import requests
import json

def emotion_detector(text_to_analyze):
    #parameters for API POST request
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    #posting input to API and receiving response 
    response = requests.post(url, json=input_json, headers=headers)
    print(response.text)

    #converting response to json
    response_dict = json.loads(response.text)

    #extracting required emotion scores 
    emotion_data = response_dict.get("emotionPredictions", [{}])[0].get("emotion", {})

    anger_score = emotion_data.get('anger', 0)
    disgust_score = emotion_data.get('disgust', 0)
    fear_score = emotion_data.get('fear', 0)
    joy_score = emotion_data.get('joy', 0)
    sadness_score = emotion_data.get('sadness', 0)
    #finding dominant emotion
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    } 
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    #returning results output
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    return result
