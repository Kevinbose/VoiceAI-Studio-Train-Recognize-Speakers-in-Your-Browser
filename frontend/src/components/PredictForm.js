// File: frontend/src/components/PredictForm.jsx
import React, { useState } from "react";
import axios from "axios";

function PredictForm({ uploaded, setUploadData, setUploaded }) {
  const [video, setVideo] = useState(null);
  const [predictions, setPredictions] = useState([]);
  const [message, setMessage] = useState("");

  const handlePredict = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("video", video);

    try {
      const res = await axios.post("http://localhost:5000/api/upload-video", formData);
      setPredictions(res.data);
      setMessage("Prediction complete.");
      setUploaded();
    } catch (err) {
      setMessage("Prediction failed. Please try again.");
    }
  };

  return (
    <div className="predict-form">
      <form onSubmit={handlePredict}>
        <input
          type="file"
          accept="video/*"
          onChange={(e) => setVideo(e.target.files[0])}
          required
        />
        <button type="submit">Upload & Predict</button>
      </form>

      {message && <p className="message">{message}</p>}

      {predictions.length > 0 && (
        <div className="results">
          <h3>Predicted Speakers:</h3>
          <ul>
            {predictions.map((item, idx) => (
              <li key={idx}>
                <strong>{item.time}</strong> - {item.name}
                {item.image && (
                  <img
                    src={`http://localhost:5000/images/${item.image}`}
                    alt={item.name}
                    style={{ width: "50px", marginLeft: "10px" }}
                  />
                )}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default PredictForm;
