# File: backend/utils/extract.py
import numpy as np
import librosa

def extract_features(file_path, sr=22050, n_mfcc=13):
    y, sr = librosa.load(file_path, sr=sr, mono=True)
    
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    mfccs_mean = np.mean(mfccs, axis=1)

    stft = np.abs(librosa.stft(y))
    chroma = librosa.feature.chroma_stft(S=stft, sr=sr)
    chroma_mean = np.mean(chroma, axis=1)
    contrast = librosa.feature.spectral_contrast(S=stft, sr=sr)
    contrast_mean = np.mean(contrast, axis=1)
    tonnetz = librosa.feature.tonnetz(y=librosa.effects.harmonic(y), sr=sr)
    tonnetz_mean = np.mean(tonnetz, axis=1)

    return np.hstack([mfccs_mean, chroma_mean, contrast_mean, tonnetz_mean])

def extract_features_from_segment(y, sr=22050, n_mfcc=13):
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    mfccs_m = np.mean(mfccs, axis=1)

    stft = np.abs(librosa.stft(y))
    chroma_m = np.mean(librosa.feature.chroma_stft(S=stft, sr=sr), axis=1)
    contrast_m = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sr), axis=1)
    tonnetz_m = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(y), sr=sr), axis=1)

    return np.hstack([mfccs_m, chroma_m, contrast_m, tonnetz_m])