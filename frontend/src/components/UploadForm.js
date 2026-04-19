// File: frontend/src/components/UploadForm.jsx
import React, { useState } from "react";
import axios from "axios";

function UploadForm({ setUploadData, setUploaded }) {
  const [name, setName] = useState("");
  const [audio, setAudio] = useState(null);
  const [image, setImage] = useState(null);
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("name", name);
    formData.append("audio", audio);
    formData.append("image", image);

    try {
      const res = await axios.post("http://localhost:5000/api/upload-train", formData);
      setMessage(res.data.message);
      setUploadData({ name });  // store speaker name or some indicator
      setUploaded();
    } catch (err) {
      setMessage("Upload failed. Please try again.");
    }
  };

  return (
    <div className="upload-form">
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Speaker Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <input
          type="file"
          accept="audio/*"
          onChange={(e) => setAudio(e.target.files[0])}
          required
        />
        <input
          type="file"
          accept="image/*"
          onChange={(e) => setImage(e.target.files[0])}
          required
        />
        <button type="submit">Upload & Train</button>
      </form>
      {message && <p className="message">{message}</p>}
    </div>
  );
}

export default UploadForm;
