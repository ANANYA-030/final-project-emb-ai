'''
Import Flask , render_template, request form flask
Import emotion_detector 
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Instantiate app
app = Flask("Emotion Analyzer")

@app.route("/emotionDetector")
def sent_analyzer():
    '''Gets the text to be analyzed and returns analyzed emotions'''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] == 'None':
        return "Invalid text! Please try again!."
    return f"For the given statement, the system response is {response}"

@app.route("/")
def render_index_page():
    '''Renders the index.html'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
