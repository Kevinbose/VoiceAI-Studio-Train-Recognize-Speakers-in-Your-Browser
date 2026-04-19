# Voice Recognition Web Platform

## Overview

This project is a full-stack voice recognition platform that allows users to upload audio samples, train speaker models, and predict speaker identities. It is designed for research, demonstration, and as a foundation for advanced voice-based applications.

---

## Table of Contents
- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Directory Structure](#directory-structure)
- [Backend Details](#backend-details)
- [Frontend Details](#frontend-details)
- [Data Organization](#data-organization)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- Upload audio samples for multiple users
- Train custom speaker recognition models
- Predict speaker identity from uploaded audio
- Modular backend utilities for feature extraction, training, and prediction
- Organized storage for audio, data, and images
- Modern, responsive React.js frontend

---

## Architecture

- **Frontend:** React.js SPA for user interaction, file uploads, and displaying results
- **Backend:** Python Flask API for audio processing, model training, and prediction
- **Data Storage:** Organized folders for audio, user data, and images

---

## Tech Stack

- **Frontend:**
  - React.js (JavaScript)
  - CSS (App.css, style.css)
  - HTML5 (public/index.html)
- **Backend:**
  - Python 3.x
  - Flask
  - Numpy, Scipy, Scikit-learn (assumed for ML tasks)
  - Custom utilities (extract.py, train.py, predict.py)
- **Other:**
  - GitHub Actions (recommended for CI/CD)
  - Modern browser support

---

## Directory Structure

```
audio/                  # Uploaded audio files
backend/
  app.py                # Flask API server
  data/
    advaith/            # User-specific audio data
    kevin/
    shubham/
  images/               # Backend-generated images (e.g., plots)
  utils/
    extract.py          # Feature extraction logic
    predict.py          # Speaker prediction logic
    train.py            # Model training logic
frontend/
  package.json          # Frontend dependencies
  public/
    index.html          # Main HTML entry
    ...
  src/
    App.js              # Main React app
    components/         # React components
      DisplayMapping.js
      Home.js
      PredictForm.js
      UploadForm.js
    ...
images/                 # Project images/assets
```

---

## Backend Details

- **app.py:** Main Flask server, exposes API endpoints for upload, train, and predict.
- **utils/extract.py:** Extracts features (MFCC, etc.) from audio files.
- **utils/train.py:** Trains speaker recognition models using extracted features.
- **utils/predict.py:** Predicts speaker identity from new audio samples.
- **data/:** Stores user-specific audio and processed data.
- **images/:** Stores generated plots or model visualizations.

---

## Frontend Details

- **React.js SPA** with components for:
  - Home page
  - Uploading audio files
  - Training models
  - Predicting speakers
  - Displaying results and mappings
- **Styling:** App.css, style.css, index.css
- **Testing:** App.test.js, setupTests.js

---

## Data Organization

- **audio/:** Raw uploaded audio files
- **backend/data/:** Processed and organized by user
- **backend/images/:** Visualizations, model plots
- **frontend/public/:** Static assets for the web app

---

## Setup & Installation

### Prerequisites
- Python 3.x
- Node.js & npm
- (Recommended) Virtual environment for Python

### Backend Setup
1. Navigate to `backend/`
2. Install dependencies:
   ```bash
   pip install flask numpy scipy scikit-learn
   ```
3. Run the Flask server:
   ```bash
   python app.py
   ```

### Frontend Setup
1. Navigate to `frontend/`
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the React app:
   ```bash
   npm start
   ```

### Directory Preparation
- Ensure `audio/`, `backend/data/`, and `backend/images/` exist and are writable.

---

## Usage

1. **Upload Audio:** Use the web interface to upload audio samples for different users.
2. **Train Model:** Trigger model training from the frontend; backend processes and saves the model.
3. **Predict Speaker:** Upload a new audio sample to predict the speaker identity.
4. **View Results:** Results and visualizations are displayed in the frontend.

---

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements
- Inspired by open-source voice recognition research
- Built with Flask and React.js
