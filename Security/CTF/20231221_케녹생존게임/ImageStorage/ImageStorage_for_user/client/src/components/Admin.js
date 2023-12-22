import React, { useState } from 'react';

const Admin = () => {
  const [token, setToken] = useState('');
  const [response, setResponse] = useState(null);

  const handleAdminAction = async () => {
    
    const response = await fetch('http://13.230.115.72:9000/admin?t='+token, {});
    setResponse(await response.json())
    
  };

  return (
    <div>
      <h2>admin page</h2>
      <input
        type="text"
        value={token}
        onChange={(e) => setToken(e.target.value)}
        placeholder="Token"
      />
      <button onClick={handleAdminAction}>verify</button>
      <div>
        {response && (
          <ul>
            {Object.entries(response).map(([key, value]) => (
              <li key={key}>
                <strong>{key}:</strong> {"Great!!"}
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
};

export default Admin;
