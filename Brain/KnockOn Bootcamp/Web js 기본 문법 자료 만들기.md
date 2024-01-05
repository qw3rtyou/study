# 자바스크립트 기본 문법

<aside> 💡 이번에 공부할 내용은 다음과 같습니다.

1. 자바스크립트의 기본 문법
2. 변수 선언과 데이터 타입
3. 함수 정의와 호출
4. 객체와 배열의 사용 방법
5. 자주 사용하는 내장 함수들

자바스크립트는 웹 페이지를 동적으로 만들어주는 스크립팅 언어입니다. 웹 브라우저 내에서 다양한 기능을 실행할 수 있으며, 이벤트 처리, 데이터 저장, DOM 조작 등을 가능하게 해줍니다.

변수는 let, const 키워드를 사용하여 선언할 수 있으며, 데이터 타입은 동적으로 결정됩니다. 함수는 function 키워드로 정의할 수 있습니다.

객체와 배열은 데이터를 구조화하는 데 사용되며, 다양한 내장 메소드를 통해 관리할 수 있습니다.

이미 JS를 공부해 보신 분들은 Arrow Function, spread 구문, Optional Chaining 과 같이 모던 JS 문법이나 비동기 관련 문법에 대해서도 공부해보셔도 좋습니다. 특히, Arrow Function은 정말 많이 사용하기 때문에 도전 문제에서도 사용되었습니다.

</aside>

---

```javascript
// 다음을 이해해 봅시다.
let message = "Hello, World!";  
const pi = 3.14;              
let isActive = true;           
let user = {                   
    name: "Hong Gil-dong",
    age: 25
};
let colors = ["red", "green", "blue"]; 

function greet(name) {
    console.log("Hello, " + name + "!");
}

greet("Anna");  
```

---

```javascript
// 다음을 이해해 봅시다.
let student = {
    name: "Kim Yoon-sung",
    major: "Computer Science",
    getIntroduction: function() {
        console.log("My name is " + this.name + " and I study " + this.major + ".");
    }
};

student.getIntroduction();

let numbers = [1, 2, 3, 4, 5];
numbers.push(6);
console.log(numbers);
```

---

```javascript
// 다양한 내장함수를 이해해봅시다.
setTimeout(function() {
    console.log("3초가 지났어요!");
}, 3000);

let count = 0;
let intervalId = setInterval(function() {
    count++;
    console.log(count + "초마다 메시지가 출력됩니다.");
    if (count >= 5) {
        clearInterval(intervalId);
    }
}, 1000);

let fruits = ["apple", "banana", "cherry"];
fruits.forEach(function(fruit) {
    console.log(fruit);
});

let numbers = [1, 2, 3, 4, 5];
let doubledNumbers = numbers.map(function(number) {
    return number * 2;
});
console.log(doubledNumbers);  // [2, 4, 6, 8, 10]

let evenNumbers = numbers.filter(function(number) {
    return number % 2 === 0;
});
console.log(evenNumbers);  // [2, 4]
```

---

<aside> 🔥 다음과 같은 내용에 도전해봅시다.

1. var, let과 const의 차이점 이해하기
2. Arrow Function 이해하기
3. 룰렛 게임 완성하기

</aside>

```js
<!DOCTYPE html>
<html>
  <head>
    <title>Roulette Game</title>
    <script></script>
  </head>
  <body>
    <div id="roulette">1</div>
    <button id="stopButton">정지</button>

    <script>
      const values = [1, 2, 3, 4, 5, 6];

      const rouletteDisplay = document.getElementById("roulette");

      let intervalId = null;

      let currentIndex = 0;

      function startRoulette() {
        intervalId = //interval 설정하기
      }

      document.getElementById("stopButton").addEventListener("click", () => {
        clearInterval(intervalId);

        alert("선택된 숫자: " + values[currentIndex]);
      });

      startRoulette();
    </script>
  </body>
</html>

```