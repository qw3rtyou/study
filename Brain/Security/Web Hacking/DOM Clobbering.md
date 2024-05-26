
# DOM
- 페이지의 콘텐츠 및 구조, 그리고 스타일이 자바스크립트 프로그램에 의해 수정되기 위해 사용

---
# DOM Clobbering
- Javascript에서의 DOM 처리 방식을 이용한 공격 기법
- Clobbering은 소프트웨어 공학에서 의도적,비의도적으로 특정 메모리나 레지스터를 완전히 덮어쓰는 현상을 의미
- DOM을 덮어쓴다는 의미

- 아래와 같은 태그가 있다고 할 때, document 뿐만 아니라 `window object`로도 가져올 수 있음
```html
<a id="CONFIG"></a>
```

```js
document.getElementById('CONFIG')
window.CONFIG
```


- HTML 태그 중 id 속성으로 명시된 Object는 window object에서도 호출이 가능
- 이를 이용한 공격이 DOM Clobbering

- 반드시 문서개체와 동일한 이름을 가진 경우만 되는 건 아니고, 같은 이름의 변수가 global scope에 있을 경우에도 overwirte가 발생

```html
<a id="testzz" href="/111">
<script>
  alert(window.testzz)
</script>
<!-- 결과는 111 -->
```


---
# form 태그
- 브라우저는 FORM의 elements 중 name 과 id 를 Form 의 property으로 처리함
- form.propertyname 이 이미 있는 상태에서 form 의 id나 name에 propertyname 이 들어가게 되면 form.propertyname 은 기존에 있던 propertyname기 아닌 getElementid (id,name) 처럼 사용됨

- 아래의 예시에선 `submit` 이라는 name property 때문에 `document.forms[0].submit()` 여기에서 함수가 오길 기대하고 있지만 실제로는 `<input type="submit" name="submit" />`이라는 input 태그 자체가 가게 됨
```html
<html>
  <form action="">
    <input type="text" value="aaa" />
    <input type="submit" name="submit" />
  </form>

  <script>
    document.forms[0].submit();
  </script>
</html>
```

```
Uncaught TypeError: document.forms[0].submit is not a function
```

- 즉 기존의 property - submit()가 덮어씌어진 것

---
# getElementById
- 위와 비슷함 
```html
<html>
  <body>
    <form name="getElementById"></form>
    <div id="intadd">hihi</div>
  </body>

  <script>
    document.getElementById("intadd");
  </script>
</html>
```


```
Uncaught TypeError: document.getElementById is not a function

document.getElementById
<form name=​"getElementById">​</form>​
```


# XSS와의 연계
```html
<html>
  <body>
    <form name="CHECKER">
      <input name="isadmin" />
    </form>
  </body>

  <script>
    window.CHECKER = window.CHECKER || {
      isadmin: false,
    };

    window.CONFIG = window.CONFIG || {
      secretkey: "strooongkeeey",
      isadmin: false,
    };

    if (window.CHECKER.isadmin || window.CONFIG.isadmin !== false) {
      document.write(window.CONFIG.secretkey);
    }
  </script>
</html>

```

- [String to Code Table](!https://image.slidesharecdn.com/domen-141018104435-conversion-gate02/75/in-the-dom-no-one-will-hear-you-scream-20-2048.jpg?cb=1666213160)
- a태그의 tostring은  href값을 반환함
- 그런데 a태그는 form태그의 속성값으로 사용할 수 없음
- 그래서 아래와 같이 HTML Collections를 사용해야 함

```html
<html>
  <body>
    <a id="CONFIG"></a>
    <a id="CONFIG" name="cmd" href="javascript:alert(secretkey)"></a>
  </body>

  <script>
    secretkey = "asdfasdf";
    window.CONFIG = window.CONFIG || {
      cmd: "1",
      isadmin: false,
    };

    if (window.CONFIG.isadmin !== false) {
      location.href = window.CONFIG.cmd;
    }
  </script>
</html>

```


즉 결론적으로 `location.href`를 바꾸는 부분과 window 객체를 사용중이면 js코드를 실행시키는 동작이 가능함


---
# REF
https://www.hahwul.com/cullinan/dom-clobbering/
https://intadd.tistory.com/143
