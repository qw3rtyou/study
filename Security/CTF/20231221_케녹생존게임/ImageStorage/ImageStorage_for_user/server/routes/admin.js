const express = require('express');
const router = express.Router();
const jwt = require('jsonwebtoken');
const fs = require('fs');
const path = require('path');
const key = "Hi_hello!"

router.get('/', (req, res) => {
  try {
    const token = req.query.t; 
    const decoded = jwt.verify(token,key);
    if (decoded.id === 'admin') {
      //
    } else {
      res.status(403).json({ error: 'Permission denied' });
    }
  } catch (error) {
    res.status(403).json({error: 'Permission denied'});
  }
});

module.exports = router;