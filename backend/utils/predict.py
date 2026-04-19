# File: backend/utils/predict.py
import os
import numpy as np
import pandas as pd
import joblib
import librosa
from moviepy.video.io.VideoFileClip import VideoFileClip
from .extract import extract_features_from_segment

SR = 22050
IMAGE_DIR = os.path.join(os.path.dirname(__file__), '..', 'images')
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'model.pkl')
ENCODER_PATH = os.path.join(os.path.dirname(__file__), '..', 'encoder.pkl')
TEMP_AUDIO = os.path.join(os.path.dirname(__file__), '..', 'temp_audio.wav')


def format_time(seconds: float) -> str:
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hrs:02d}:{mins:02d}:{secs:02d}"


def extract_audio_from_video(video_path, audio_output_path=TEMP_AUDIO):
    with VideoFileClip(video_path) as clip:
        clip.audio.write_audiofile(audio_output_path)
    return audio_output_path


def split_audio(audio_path, segment_length=1.0, sample_rate=SR):
    y, sr = librosa.load(audio_path, sr=sample_rate, mono=True)
    seg_samps = int(segment_length * sr)
    segments = []
    for start in range(0, len(y), seg_samps):
        end = start + seg_samps
        if end <= len(y):
            seg = y[start:end]
            t0 = start / sr
            segments.append((seg, t0))
    return segments


def predict_speakers(video_path):
    clf = joblib.load(MODEL_PATH)
    le = joblib.load(ENCODER_PATH)

    audio_path = extract_audio_from_video(video_path)
    segments = split_audio(audio_path)

    rows = []
    for seg, t0 in segments:
        feat = extract_features_from_segment(seg)
        pred = clf.predict([feat])[0]
        name = le.inverse_transform([pred])[0]
        image_path = f"images/{name}.jpg"

        t1 = t0 + 1.0
        interval = f"{format_time(t0)} --> {format_time(t1)}"

        rows.append({
            "time": interval,
            "name": name,
            "image": image_path
        })

    df = pd.DataFrame(rows)
    mapping_path = os.path.join(os.path.dirname(__file__), '..', 'mapping.csv')
    df.to_csv(mapping_path, index=False)
    print(f"Predictions saved to mapping.csv")
    return df