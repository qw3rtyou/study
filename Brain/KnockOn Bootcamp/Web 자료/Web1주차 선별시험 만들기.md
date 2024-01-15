- HTML 태그
- HTML 문서의 구조
- CSS의 기본적인 문법과 속성들
- JS의 객체와 배열의 사용 방법
- JS의 자주 사용하는 내장 함수들
- JS의 변수 선언과 데이터 타입

---
**1. HTML 기본 구조와 태그 사용에 관한 설명으로 옳은 것은?**
```html
<!DOCTYPE html>
<html>
<head>
    <title>title</title>
</head>
<body>
    <h1>h1</h1>
    <p>p</p>
    <a href="https://www.example.com">href</a>
    <img src="image.jpg" alt="image">
</body>
</html>
```

- [x]  `<!DOCTYPE html>`: HTML5 문서의 형식을 선언한다.
- [ ]  `<title>title</title>`: h1 태그처럼 페이지 가장 상단에 제목을 표시한다.
- [ ]  `<a href="https://www.example.com">`: 이미지를 클릭하여 `https://www.example.com`으로 이동한다.
- [x]  `<img src="image.jpg" alt="웹 개발 이미지">`: `image.jpg` 파일을 웹 페이지에 표시하고, 이미지가 로드되지 않을 때 "웹 개발 이미지"라는 텍스트를 표시한다.

**답 : 1, 2, 4**

1. `<!DOCTYPE html>`: 이 선언은 웹 브라우저에게 문서가 HTML5 표준을 따른다는 것을 알려줍니다.
2. `<title>title</title>`: `<title>` 태그는 웹 브라우저의 탭에 나타날 페이지 제목을 지정합니다.
3. `<a href="https://www.example.com">`: 이 태그는 하이퍼링크를 생성하고, 사용자가 클릭하면 `https://www.example.com`으로 이동합니다. 그러나 이미지의 대한 태그가 아니므로 이미지에 대한 언급은 부적절합니다.
4. `<img src="image.jpg" alt="image">`: `<img>` 태그는 웹 페이지에 이미지를 표시하며, `alt` 속성은 이미지가 로드되지 않을 때 표시되는 대체 텍스트입니다.

---

**2. CSS 선택자에 대한 설명으로 옳은 것은?**
```css
#container > .item:first-child {
    background-color: #f0f0f0;
    border-left: 5px solid #333;
}

.item + .item {
    margin-top: -10px;
}
```

- [ ]  `#container > .item:first-child`: `#container`의 모든 자식 `.item` 요소에 스타일을 적용한다.
- [x]  `border-left: 5px solid #333;`: 선택된 요소의 왼쪽 테두리에 5픽셀 너비의 검은색 실선을 추가한다.
- [ ]  `.item + .item`: 모든 `.item` 클래스를 가진 요소에 마진을 적용한다.
- [x]  `background-color: #f0f0f0;`: 선택된 요소의 배경 색상을 설정한다.

**답 : 2, 4**

1. `#container > .item:first-child`: 이 선택자는 `#container` 요소의 첫 번째 자식 `.item` 클래스를 가진 요소에만 스타일을 적용합니다.
2. `border-left: 5px solid #333;`: 이 속성은 선택된 요소의 왼쪽 테두리에 5픽셀 너비의 검은색 실선을 추가합니다.
3. `.item + .item`: 이 선택자는 `.item` 클래스를 가진 요소 바로 다음에 오는 `.item` 클래스를 가진 형제 요소에 스타일을 적용합니다.
4. `background-color: #f0f0f0;`: 이 속성은 선택된 요소의 배경 색상을 설정합니다.

---

**3. 객체와 배열 사용법에 대한 설명으로 옳은 것은?**
```javascript
let data = {
    users: [
        { id: 1, name: "홍길동", active: true },
        { id: 2, name: "김철수", active: false }
    ],
    getUser(id) {
        return this.users.find(user => user.id === id);
    }
};

let firstUser = data.users[0];
```

- [x]  `data.getUser(1)`: `id`가 1인 사용자 객체를 반환한다.
- [ ]  `let firstUser = data.users[0];`: `data.users` 배열의 첫 번째 요소를 `firstUser` 변수에 할당한다.
- [ ]  `data.users.find`: `find` 메소드는 모든 사용자를 배열로 반환한다.
- [ ]  `data.users[1].active`: `id`가 1인 사용자의 `active` 상태를 반환한다.

**답 : 1, 2**

1. `data.getUser(1)`: 이 메소드는 `data` 객체의 `users` 배열에서 `id`가 1인 사용자 객체를 찾아 반환합니다.
2. `let firstUser = data.users[0];`: 이 구문은 `data.users` 배열의 첫 번째 요소를 `firstUser` 변수에 할당합니다.
3. `data.users.find`: `find` 메소드는 제공된 테스트 함수를 만족하는 첫 번째 요소를 반환합니다, 모든 요소를 반환하지 않습니다.
4. `data.users[1].active`: 배열의 인덱스는 0부터 시작하므로 `data.users[1]`은 `id`가 2인 두 번째 사용자의 객체입니다.

---

**4. 변수 선언 및 데이터 타입과 관련된 설명으로 옳은 것은?**
```javascript
const PI = 3.14159;
let result = PI * 2;

function checkType(value) {
    return typeof value;
}

let isNumber = checkType(PI);
let isVoid = checkType();
```

- [x]  `const PI = 3.14159;`: `PI` 상수에 소수 값을 할당한다.
- [ ]  `let result = PI * 2;`: `result` 변수는 항상 문자열 타입을 가진다.
- [x]  `let isNumber = checkType(PI);`: `isNumber` 변수에는 'number' 문자열이 할당된다.
- [x]  `let isVoid = checkType();`: `isVoid` 변수에는 'undefined' 문자열이 할당된다.

**답 : 1, 3, 4**

1. `const PI = 3.14159;`: 이 선언은 `PI`라는 이름의 상수를 선언하고, 3.14159라는 숫자 값을 할당합니다.
2. `let result = PI * 2;`: `result` 변수는 `PI`와 2를 곱한 결과를 저장하므로, 숫자 타입을 가질 수 있습니다.
3. `let isNumber = checkType(PI);`: `checkType` 함수는 인자의 데이터 타입을 문자열로 반환하므로, 'number'가 됩니다.
4. `let isVoid = checkType();`: 인자를 전달하지 않고 함수를 호출하면, 'undefined'가 반환됩니다.
---

**5. 함수 표현과 스코프에 관련된 설명으로 옳은 것은?**
```javascript
let x = 10;

function outer() {
    let y = 20;
    function inner() {
        let z = 30;
        return x + y + z;
    }
    return inner();
}

let result = outer();
```

- [x]  `let x = 10;`: 전역 변수 `x`를 선언하고 10을 할당한다.
- [x]  `function inner() {...}`: `inner` 함수는 `outer` 함수 내부에 중첩된 클로저 함수이다.
- [ ]  `let result = outer();`: `result` 변수에는 `outer` 함수의 로컬 변수 `y`가 할당된다.
- [ ]  `return x + y + z;`: `inner` 함수는 `y`를 접근할 수 없으므로  `x`, `y`, `z`의 합을 반환할 수 없다.

**답 : 1, 2,

1. `let x = 10;`: 이 선언은 전역 스코프에서 변수 `x`를 선언하고 그 값으로 10을 할당합니다.
2. `function inner() {...}`: `inner` 함수는 `outer` 함수의 내부에서 정의된 중첩된 함수로, 외부 함수의 변수에 접근할 수 있는 클로저입니다.
3. `let result = outer();`: `result` 변수에는 `outer` 함수를 호출함으로써 반환된 값이 할당되며, 이는 `inner` 함수에 의해 계산된 값입니다.
4. `return x + y + z;`: `inner` 함수는 클로저를 통해 `outer` 함수의 `y`와 전역 변수 `x`에 접근할 수 있으며, 자신의 로컬 변수 `z`와 함께 이들의 합을 반환합니다.

---

**6. 이벤트 처리와 관련된 설명으로 옳은 것은?**
```javascript
document.querySelector(".button").addEventListener("click", function(event) {
    event.preventDefault();
    console.log("버튼 클릭!");
});
```

- [x]  `document.querySelector(".button")`: 문서에서 클래스 이름이 `button`인 첫 번째 요소를 선택한다.
- [x]  `addEventListener("click", function(event) {...})`: 클릭 이벤트에 대한 이벤트 리스너를 추가한다.
- [x]  `event.preventDefault();`: 기본 이벤트 동작을 취소한다.
- [ ]  `console.log("버튼 클릭!");`: 클릭 이벤트가 발생할 때마다 메시지를 사용자에게 보여지는 페이지에 출력한다.

**답 : 1, 2, 3**

1. `document.querySelector(".button")`: 이 메서드는 클래스 이름이 `button`인 문서의 첫 번째 요소를 선택합니다.
2. `addEventListener("click", function(event) {...})`: 이 코드는 선택된 요소에 클릭 이벤트가 발생했을 때 실행될 콜백 함수를 등록합니다.
3. `event.preventDefault();`: 이 메서드는 이벤트의 기본 동작이 실행되지 않도록 취소합니다. 예를 들어, 링크가 클릭되었을 때 페이지가 다른 주소로 넘어가지 않게 하는 경우에 사용됩니다.
4. `console.log("버튼 클릭!");`: 이 코드는 클릭 이벤트가 발생할 때마다 "버튼 클릭!"이라는 메시지를 페이지가 아닌 콘솔에 기록합니다.