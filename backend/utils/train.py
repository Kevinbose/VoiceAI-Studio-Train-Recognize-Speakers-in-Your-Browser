# File: backend/utils/train.py
import os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib
from .extract import extract_features
from utils.predict import split_audio  # reuse your split logic
from utils.extract import extract_features_from_segment

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'model.pkl')
ENCODER_PATH = os.path.join(os.path.dirname(__file__), '..', 'encoder.pkl')


def create_train_csv(data_dir=DATA_DIR):
    records = []
    for speaker in os.listdir(data_dir):
        speaker_dir = os.path.join(data_dir, speaker)
        if os.path.isdir(speaker_dir):
            for fname in os.listdir(speaker_dir):
                if fname.lower().endswith(".mp3"):
                    path = os.path.join(speaker_dir, fname)
                    records.append((speaker, path))
    return pd.DataFrame(records, columns=["label", "filepath"])


def extract_and_save_features(df):
    feats, labels = [], []
    for _, row in df.iterrows():
        try:
            segments = split_audio(row['filepath'])  # get 1-second chunks
            for seg, _ in segments:
                feat = extract_features_from_segment(seg)
                feats.append(feat)
                labels.append(row['label'])
        except Exception as e:
            print(f"Error processing {row['filepath']}: {e}")
    return np.vstack(feats), np.array(labels)


def train_model():
    df_meta = create_train_csv()
    if df_meta.empty:
        print("No training data found.")
        return None, None

    X, y = extract_and_save_features(df_meta)
    if X.shape[0] < 2:
        print("Not enough samples to perform train/test split. Need at least 2 samples.")
        # Option 1: Skip splitting and train on the only sample (not recommended for production)
        # Option 2: Return an error so the user knows to add more data
        return None, None

    le = LabelEncoder().fit(y)
    y_enc = le.transform(y)

    # Split only if there are enough samples
    X_tr, X_te, y_tr, y_te = train_test_split(X, y_enc, test_size=0.2, random_state=42)

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_tr, y_tr)

    joblib.dump(clf, MODEL_PATH)
    joblib.dump(le, ENCODER_PATH)

    print("Model trained and saved.")
    return clf, le


if __name__ == '__main__':
    train_model()
