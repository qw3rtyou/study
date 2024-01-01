import React, { useState } from 'react';
import '../index.css';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [logIn,setLogIn]=useState(false);

  const handleLogin = async () => {
    try {
      const response = await fetch('http://localhost:9000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
      });
      const data = await response.json();

      if (data.token) {
        localStorage.setItem('token', data.token);
        setLogIn(true);
      }
      else{

      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h2>Login</h2>
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
      {logIn?(
        <>
        <p>로그인에 성공하였습니다.</p>
        </>
      ):(
        <>
      <button onClick={handleLogin}>로그인</button>
      </>
      )}
    </div>
  );
};

export default Login;