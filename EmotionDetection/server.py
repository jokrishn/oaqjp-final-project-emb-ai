"""
Flask server for the Emotion Detector application.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
 """
 Render the main page.
 """
 return render_template("index.html")


@app.route("/emotionDetector")
def sent_detector():
 """
 Analyze text and return emotion detection results.
 """
 text_to_analyze = request.args.get("textToAnalyze")

 response = emotion_detector(text_to_analyze)

 if response["dominant_emotion"] is None:
 return "Invalid text! Please try again!"

 return (
 "For the given statement, the system response is "
 f"'anger': {response['anger']}, "
