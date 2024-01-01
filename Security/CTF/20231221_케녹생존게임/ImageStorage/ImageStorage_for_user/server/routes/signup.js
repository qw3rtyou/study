const express = require('express');
const { addUser, checkIfUserExists } = require('./db');
const router = express.Router();

router.post('/', (req, res) => {
  const { username, password } = req.body;

  if (username.includes('admin')) {
    return res.status(403).json({ error: '관리자는 회원으로 가입할 수 없습니다.' });
  }

  // 기존에 같은 사용자명이 있는지 확인
  if (checkIfUserExists(username)) {
    return res.status(400).json({ error: '이미 존재하는 사용자입니다.' });
  }

  // 회원가입 성공 시 사용자 정보를 저장
  addUser(username,password);
  res.json({ message: '회원가입이 완료되었습니다.' });
});

module.exports = router;
