import React, { useState } from 'react';
import '../index.css';
const Signup = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [msg, setMsg] = useState('');

  const handleSignup = async () => {
    try {
      const response = await fetch('http://localhost:9000/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
      });
      const data = await response.json();
      setMsg(data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h2>SignUp</h2>
      <input
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Username"
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="password"
      />
      <button onClick={handleSignup}>회원가입</button>
      {msg && (
          <ul>
            {Object.entries(msg).map(([key, value]) => (
              <li key={key}>
                <strong>{key}:</strong> {JSON.stringify(value)}
              </li>
            ))}
          </ul>
        )}
    </div>
  );
};

export default Signup;
