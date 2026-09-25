import requests
import json

def emotion_detector(text_to_analyze):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } } # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header) # Send a POST request to the API with the text and headers

    if response.status_code == 200:
       # If the response status code is 200, parse the JSON response
        formatted_response = response.json() # Change to response.json() to handle non-str
        emotion_predictions_root = formatted_response.get("emotionPredictions")
        emotion_predictions_first = emotion_predictions_root[0]
        emotion_scores = emotion_predictions_first.get("emotion")

        anger_score = emotion_scores.get("anger")
        disgust_score = emotion_scores.get("disgust")
        fear_score = emotion_scores.get("fear")
        joy_score = emotion_scores.get("joy")
        sadness_score = emotion_scores.get("sadness")

        dominant_emotion_score = max(emotion_scores, key=emotion_scores.get)

    # If the response status code is 400, set to None
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None

        dominant_emotion_score = None

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion_score
    }
