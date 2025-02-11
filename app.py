from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import cv2

app = Flask(__name__)

# Load the emotion detection model
model = tf.keras.models.load_model("emotion_model.h5")

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Emotion detection API is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        file = request.files["image"]
        img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
        img = cv2.resize(img, (48, 48))  # Resize to model input size
        img = img / 255.0  # Normalize
        img = np.expand_dims(img, axis=0)

        prediction = model.predict(img)
        emotion_label = np.argmax(prediction)  # Get the predicted class index

        return jsonify({"emotion": int(emotion_label)})

    except Exception as e:
        return jsonify({"error": str(e)})

# Required for Vercel
def handler(event, context):
    return app(event, context)
