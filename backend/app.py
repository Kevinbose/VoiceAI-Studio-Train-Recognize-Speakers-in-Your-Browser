from flask import Flask, request, jsonify, send_file, send_from_directory
from flask_cors import CORS
import os
import shutil
from werkzeug.utils import secure_filename
from utils.train import train_model
from utils.predict import predict_speakers

app = Flask(__name__)
CORS(app)

# Directories
UPLOAD_DATA_DIR = os.path.join("data")
UPLOAD_IMG_DIR = os.path.join("images")
MAPPING_CSV = os.path.join("mapping.csv")
VIDEO_TEMP_PATH = os.path.join("temp_video.mp4")

# Ensure required directories exist
os.makedirs(UPLOAD_DATA_DIR, exist_ok=True)
os.makedirs(UPLOAD_IMG_DIR, exist_ok=True)

# Route to serve images from the images folder
@app.route("/images/<path:filename>")
def serve_images(filename):
    return send_from_directory(UPLOAD_IMG_DIR, filename)

@app.route("/api/upload-train", methods=["POST"])
def upload_and_train():
    name = request.form.get("name")
    audio_file = request.files.get("audio")
    image_file = request.files.get("image")

    if not (name and audio_file and image_file):
        return jsonify({"error": "Missing data"}), 400

    speaker_dir = os.path.join(UPLOAD_DATA_DIR, name)
    os.makedirs(speaker_dir, exist_ok=True)

    audio_path = os.path.join(speaker_dir, secure_filename(audio_file.filename))
    image_path = os.path.join(UPLOAD_IMG_DIR, f"{name}.jpg")

    audio_file.save(audio_path)
    image_file.save(image_path)

    train_model()

    return jsonify({"message": "Training successful for new speaker."})

@app.route("/api/upload-video", methods=["POST"])
def upload_video():
    video_file = request.files.get("video")

    if not video_file:
        return jsonify({"error": "No video provided"}), 400

    video_file.save(VIDEO_TEMP_PATH)

    df = predict_speakers(VIDEO_TEMP_PATH)

    return jsonify(df.to_dict(orient="records"))

@app.route("/api/mapping", methods=["GET"])
def download_mapping():
    if os.path.exists(MAPPING_CSV):
        return send_file(MAPPING_CSV, as_attachment=True)
    return jsonify({"error": "No mapping available"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)
