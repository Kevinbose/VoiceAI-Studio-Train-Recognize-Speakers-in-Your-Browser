// File: frontend/src/App.jsx
import React, { useState } from 'react';
import './App.css';
import UploadForm from './components/UploadForm';
import PredictForm from './components/PredictForm';

const App = () => {
  const [uploadData, setUploadData] = useState(null);
  const [uploaded, setUploaded] = useState(false);

  const toggleUploaded = () => {
    setUploaded(!uploaded);
  };

  return (
    <div className="app-container">
      <h1 className="title">Voice Recognition</h1>

      <div className="card">
        <h2>Upload Audio and Image for Training</h2>
        <UploadForm setUploadData={setUploadData} uploaded={uploaded} setUploaded={toggleUploaded} />
      </div>

      {uploaded && (
        <div className="card">
          <h2>Upload a Video for Prediction</h2>
          <PredictForm uploaded={uploaded} setUploadData={setUploadData} setUploaded={toggleUploaded} />
        </div>
      )}
    </div>
  );
};

export default App;
