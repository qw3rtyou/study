import React, { useState } from 'react';

const FileInput = () => {
  
  const [filename, setFilename] = useState('');
  const [image, setImage] = useState('');

  const handleFileUpload = async () => {
    try {
      const response = await fetch('http://localhost:9000/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ filename })
        
      });
      const data = await response.json();
      setImage(`data:image/png;base64,${data.image}`);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h2>Image Archive</h2>
      <input
        type="text"
        value={filename}
        onChange={(e) => setFilename(e.target.value)}
        placeholder="filename"
      />
      <button onClick={handleFileUpload}>request</button>
      {image && <img src={image} alt="Uploaded" />}
    </div>
  );
};

export default FileInput;
