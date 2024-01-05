# HTML, CSS, JS

<aside> 💡 이번에 배울 내용은 다음과 같습니다.

1. HTML, CSS, JS의 기본 개념, 용도, 사용방법, 관계 등등
2. 웹 페이지 제작에 필요한 기본적인 HTML 태그들
3. 스타일링을 위한 CSS의 기본적인 문법과 속성들
4. 웹 페이지의 동적 기능을 위한 JS의 기본적인 문법과 함수들

HTML, CSS, JS는 웹 페이지 제작의 가장 기본이 되는 요소들입니다. HTML로 웹 페이지의 구조를 만들고, CSS로 웹 페이지를 꾸며주며, JS로 웹 페이지에 동적인 기능을 추가할 수 있습니다.

웹 해킹을 배우기 위해서는 이 세 가지 요소를 잘 이해하고 있어야 합니다.

</aside>

---

```html
<!-- 다음을 이해해 봅시다 -->
<!DOCTYPE html>
<html>
<head>
    <style>
        body {background-color: powderblue;}
        h1   {color: blue;}
        p    {color: red;}
    </style>
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>
<button onclick="changeColor()">Change color</button>

<script>
function changeColor() {
  document.body.style.backgroundColor = "yellow";
}
</script>

</body>
</html>
```

---


```html
<!-- 다음을 이해해 봅시다 -->
<!DOCTYPE html>
<html>
<body>

<h2>JavaScript Arrays</h2>

<p id="demo"></p>

<script>
var cars = ["Saab", "Volvo", "BMW"];
document.getElementById("demo").innerHTML = cars;
</script>

</body>
</html>
```

---

<aside> 🔥 도전해봅시다.

1. 자신을 소개하는 페이지를 작성해 봅시다(형식 자유)
2. 간단한 계산기 페이지를 만들어 봅시다.

</aside>
![[Pasted image 20240105091827.png]]