const express = require('express');
const router = express.Router();
const fs = require('fs');
const path = require('path');

const banList = ['flag'];
function isStringBanned(input) {
  return banList.some(bannedWord => input.includes(bannedWord));
}

const { promisify } = require('util');
const readFileAsync = promisify(fs.readFile);

router.post('/', async (req, res) => {
  try {
    const { filename } = req.body;
    if(isStringBanned(filename)){
        res.status(401).json({error: "Permission denied"});
    }
    const imagePath = path.join(__dirname, '../image', filename);
    const image = await readFileAsync(imagePath, 'base64');
    res.json({ image });
  } catch (error) {
    if (error.code === 'EACCES') {
      res.status(401).json({error: "Permission denied"});
    }
    res.status(404).json({ error: "404 not found"});
  }
});

module.exports = router;
