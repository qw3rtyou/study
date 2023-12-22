import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { createRoot } from 'react-dom';

import './index.css';
import FileInput from './components/Fileinput';
import Login from './components/Login';
import Signup from './components/Signup';
import Admin from './components/Admin';

const root = document.getElementById('root');
const reactRoot = createRoot(root);

reactRoot.render(
  <Router>
    <Routes>
      <Route exact path="/" element={<FileInput />} />
      <Route path="/login" element={<Login />} />
      <Route path="/signup" element={<Signup />} />
      <Route path="/admin" element={<Admin />} />
    </Routes>
  </Router>
);