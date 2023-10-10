import requests,json

def emotion_detector(text_to_analyze):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj , headers= header)
    formatted_text = json.loads(response.text)
    
    if response.status_code == 400:
        return {"anger":'None' , "disgust": 'None', "fear": 'None', "joy" : 'None', "sadness": 'None', "dominant_emotion":'None'}
        
    else:
        set_of_emotions = formatted_text['emotionPredictions'][0]['emotion']
        maxScore = -1  
        for key,value in set_of_emotions.items():
            if(value > maxScore):
                maxScore = value
                dominant_emotion = key
        set_of_emotions.update({'dominant_emotion': dominant_emotion})

    return set_of_emotions
    
