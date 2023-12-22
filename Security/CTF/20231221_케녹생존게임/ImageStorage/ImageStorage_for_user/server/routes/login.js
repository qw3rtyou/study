const express = require('express');
const jwt = require('jsonwebtoken');
const { findUserByUsername } = require('./db');
const router = express.Router();
const key = "Hi_hello!"

router.post('/', async (req, res) => {
  try {
    const { username, password } = req.body;
    const user = findUserByUsername(username);
    if (!user) {
      return res.status(401).json({ error: '유저 정보가 없습니다.' });
    }
    if (!(password == user.password)) {
      return res.status(401).json({ error: '패스워드가 일치하지 않습니다.' });
    }
    console.log({ id: user.username })
    const token = jwt.sign({ id: user.username },key);
    res.json({ token });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
