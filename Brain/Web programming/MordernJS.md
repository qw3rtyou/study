# 모던JS 동작 원리
ES2016 이후의 JS문법

### 데이터 타입의 특징과 종류
기본형에는 Number String, Boolean, Null, Undefined
외에도 2015년에 추가된 Symbol, 2020년에 BigInt가 있다.

Symbol은 코드 내 유일한 값을 가진 변수 이름을 만들 때 사용하는데,
Symbol객체 괄호 안에 설명을 적어줄 수도 있음
이러한 Symbol값을 담게 된 변수는 고유한 변수가 됨
심지어 같은 설명을 넘겨줘도 다르게 나옴

```js
const symbolA = Symbol('this is Symbol');
const symbolB = Symbol('this is Symbol');

console.log(symbolA === symbolB); // false
```

BigInt는 아주 큰 정수를 표혆하기 위해 나온 데이터 타입인데,
자바스크립트에서 안전한 정수 표현의 한계는 9000조 정도까지이다.
이 때, 이보다 더 큰 정수를 표현하고 싶다면 BigInt를 사용하면 된다.
BigInt 타입의 값은 일반 정수 마지막에 알파벳 n을 붙이거나 BinInt라는 함수를 사용하면 됨

```js
3n * 2; // TypeError
3n * 2n; // 6n
Number(3n) * 2; // 6
```


### typeof 연산자
typeof 연산자를 통해 자료형을 알아낼 수 있다.

```js
typeof 'Codeit'; // string
typeof Symbol(); // symbol
typeof {}; // object
typeof []; // object
typeof true; // boolean
typeof(false); // boolean
typeof(123); // number
typeof(NaN); // number
typeof(456n); // bigint
typeof(undefined); // undefined
```

다음과 같은 특이한 결과도 있다.

```js
typeof null; // object

function sayHi() {
console.log('Hi!?');
}

typeof sayHi; // function
```


### 불린으로 평가되는 값
조건이 필요한 맥락에서 JS는 자동으로 조건문이 아니더라도
불린값으로 형변환한다.

다음은 불린으로 평가되는 값(Falsy)이다. 이 이외에는 전부 true(Truthy)다.
`false, null, undefined, NaN, 0, ''`


### AND와 OR의 연산 방식
JS는 AND나 OR 연산을 할 때, Falsy나 Truthy한 값이 아니라,
그냥 피연산자 그대로를 반환하는 경우가 있다.

	null && undefined       //null
	0 || true           //true
	'0' && NaN          //NaN
	{} || 123           //{}

참고로 AND가 OR보다 우선순위가 높다.


### null 병합연산자(??)
물음표 두 개(??)를 사용해서 null 혹은 undefined 값을 가려내는 연산자 

```js
const example1 = null ?? 'I'; // I
const example2 = undefined ?? 'love'; // love
const example3 = 'Python' ?? 'JavaScript'; // Python

console.log(example1, example2, example3); // I love Python
```


### 변수와 스코프
변수 선언 키워드가 var에서 let,const 로 바뀜

var의 문제는 3가지 정도가 있는데,
hoisting(선언하기도 전에 사용가능함), 중복선언가능, scope가 대표적이다.
참고로 let은 scope를 코드블럭({})으로 구분하기 때문에
지역변수를 만들기 편하다.



# 함수 다루기
### 함수를 만드는 방법
함수 선언이 있고, 변수에 할당하는 방법(함수 표현식)이 있다.
정확히는 함수표현을 값처럼 사용하는 것을 함수 표현식이라고 한다.

```js
const printHi = function () {       //함수 표현식
	console.log('Hi!');
};

function sayHi() {          //함수 선언
	console.log('Hi!');
}
```


### 이름이 있는 함수 표현식
함수 표현식으로 함수를 만들 때, 이름을 붙여 줄 수 있는데,
Named Function Expression(기명 함수 표현식)이라고 한다.

이름이 없는 함수를 변수에 할당할 때는 변수의 name 프로퍼티는 변수 이름 그 자체를 문자열로 가지게 된다

```js
const sayHi = function () {
console.log('Hi');
};

console.log(sayHi.name); // sayHi
```

반면, 함수에 이름을 붙여주게 되면, name 속성은 함수 이름을 문자열로 갖게 됨

```js
const sayHi = function printHiInConsole() {
console.log('Hi');
};

console.log(sayHi.name); // printHiInConsole
```

재귀함수처럼 함수 내에서 함수를 가리켜야만 할 때에는 기명 함수 표현식이 좋음
아래 예시에서 기명 함수 표현식으로 안했는데 countdown이 바뀐다면 type에러가 뜰것이다.

```js
let countdown = function printCountdown(n) {
console.log(n);
if (n === 0) {
	console.log('End!');
} else {
	printCountdown(n - 1);
}
};

let myFunction = countdown;

countdown = null;

myFunction(5); // 정상적으로 동작
```


### 즉시 실행 함수(Immediately Invoked Function Expression)
줄여서 IIFE라고 부름
함수 자체에 괄호를 감싸고 그 뒤에 함수를 실행하는 소괄호를 한 번 더 붙여주는 방식
이러면 함수가 선언된 순간 바로 실행됨 

```js
(function () {
	console.log('Hi!');
})();
```

한 가지 주의할 점은 즉시 실행 함수는 함수에 이름을 지어주더라도 외부에서 재사용할 수 없다
그래서 일반적으로는 이름이 없는 익명 함수를 사용

주로 프로그램 초기화 기능이나

```js
(function init() {
	// 프로그램이 실행 될 때 기본적으로 동작할 코드들..
})();
```

재사용이 필요 없는, 일회성 동작을 구성할 때 활용

```js
const firstName = Young;
const lastName = Kang;

const greetingMessage = (function () {
const fullName = `${firstName} ${lastName} `;

return `Hi! My name is ${fullName}`;
})();
```


### 값으로서의 함수
함수는 근본적으로 객체다 
그래서 함수의 매개변수 리턴값 등에 사용될 수 있다.

```js
function getPrintHi() {     //함수를 리턴하는 함수를 고차함수라고함
	return function() {
		console.log('hi');
	};
};

const sayHi = getPrintHi();

sayHi();
getPrintHi()();
```

또 객체 property나 배열의 요소 등으로 사용될 수도 있고 변수에 할당될 수도 있다.
다른 함수의 파라미터에 전달되는 함수를 콜백함수라고 한다.

이러한 특징을 갖는 함수를 프로그래밍 언어에서는 1급함수라고 한다.


### Parameter
argument vs parameter
인자와 파라미터는 분명 다름
인자는 함수 호출부에서 값을 넘길 때 사용하고
파라미터는 함수 구현부에서 넘겨진 값을 받는 부분임

기본값
함수에 인자값을 넘겨주지 않으면 함수는 undefined를 자동으로 넣는다.
초기값을 설정해주면 위 문제를 해결해 줄 수 있다.

```js
function greeting(name='구자용'){
	console.log(`Haloa, ${name}!`);
}

greeting();     //자동으로 초기값이 들어감
```

argument는 앞에서 부터 할당되기 때문에 
초기값을 설정해놓은 파라미터는 뒤에 있는 것이 좋다.

만약 이를 피하라고 싶다면

```js
function greeting(name='구자용', sex='male'){
	console.log(`Haloa, ${name}!`);
	console.log(male);
}

greeting(undefined,'female');     //자동으로 초기값이 들어감
```


### Arguments
##### arguments
전달되는 argument의 개수가 다양하다면
다음과 같이 arguments를 이용해 유동적으로 처리할 수 있다.

```js
function printArguments(){
	for (const arg of arguments){
		console.log(arg);
	}
}

printArguments(a,b,c,d,e)
printArguments(a,)
printArguments(a,b)
printArguments()
```

다만 arguments는 배열의 형태를 띄지만 배열의 method는 사용할 수 없는
유사배열이기 때문에 rest parameter가 합리적일 수도 있다.

##### Rest Parameter
위에 코드는 Rest parameter를 이용해 다음과 같이 수정할 수 있다.

```js
function printArguments(...args){
	for (const arg of args){
		console.log(arg);
	}
}

printArguments(a,b,c,d,e)
printArguments(a,)
printArguments(a,b)
printArguments()
```

args는 배열이기 때문에 배열의 method 모두 사용할 수 있다.

일반 parameter와 같이 사용할 수 있는데

```js
function printArguments(fisrt, second, ...args){
	console.log("1번째"+fisrt)
	console.log("2번째"+second)
	
	for (const arg of args){
		console.log(arg);
	}
}

printArguments(a,b,c,d,e)
```

...args는 할당된 나머지 인자들을 배열로 담는다.
일반적으로 rest parameter는 가장 마지막에 사용하는 것이 좋다.


### Arrow Function
함수 선언을 간편하게 하기 위해 나옴
function 키워드를 없애고 parameter랑 중괄호 사이에 => 를 넣어주면 됨
다음 두 함수는 같은 함수 선언이다.

```js
const getTwice = function (number){
	return number * 2;
};

const getTwice = (number) => {
	return number * 2;
};
```

함수 실제 구현부가 return 만 있을 때, 중괄호를 생략하고, return을 없앨 수 있고,

`const getTwice = (number) => number * 2;`

파라미터가 하나인 경우에 파라미터를 감싸는 소괄호를 생략할 수 있다.

`const getTwice = number => number * 2;`

만약 리턴값이 객체인 경우에는 다음과 같이 소괄호를 감싸줘야한다.
왜냐하면 중괄호를 객체의 중괄호가 아닌 함수의 중괄호로 인식하기 때문

`const getInfo = () => ({name:'구자용',sex:'male'});`


### this
함수를 호출한 객체를 가리킴

Arrow function의 this는 호출한 객체 이전 객체를 가리키기 때문에
일반적인 객체의 메소드를 만들 때에는 Arrow function 보다는 일반 method가 좋다.



# 자바스크림트의 문법과 표현
### 문장과 표현식
##### 문장(statements)
어떤 동작이 일어나도록 작성된 최소한의 코드 덩어리
선언문, 할당문, 조건문, 반복문 등등

```js
let x;
-----
x = 3;
-------

if (x < 5) {
	console.log('x는 5보다 작다');
} else {
	console.log('x는 5와 같거나 크다');
}
-------

for (let i = 0; i < 5; i++) {
	console.log(i);
}
-----
```

##### 표현식
결과적으로 하나의 값이 되는 모든 코드
마지막 네 줄처럼 선언된 변수를 호출하거나, 객체의 프로퍼티에 접근하는 것도 결국에는 하나의 값

	5
	'string'

	5+7
	true&&false

	typeof info // object
	title // JavaScript
	info.name // '구자용'
	numbers[3] // undefined

##### 표현식이면서 문장, 문장이면서 표현식
표현식은 보통 문장의 일부로 쓰이지만, 그 자체로 문장일 수도 있음

```js
// 할당 연산자는 값을 할당하는 동작도 하지만, 할당한 값을 그대로 가지는 표현식이다.
title = 'JavaScript'; // JavaScript

// 함수 호출은 함수를 실행하는 동작도 하지만, 실행한 함수의 리턴 값을 가지는 표현식이다.
sayHi(); // sayHi 함수의 리턴 값

// console.log 메소드는 콘솔에 아규먼트를 출력하는 동작도 하지만, undefined 값을 가지는 표현식이다.
console.log('hi'); // undefined
```

##### 표현식인 문장 vs 표현식이 아닌 문장
이 둘을 구분하는 방법은
구분하고자 하는 문장을 변수에 할당해 보는 것이다.

예를들어 for문을 변수에 할당하려고 하면 오류가 나올 것이다.

자바스크립트에서 특별한 경우를 제외하면 일반적으로 표현식인 문장은 세미콜론으로, 
표현식이 아닌 문장은 문장 자체의 코드 블록(중괄호)로 그 문장의 범위가 구분된다.


##### 조건을 다루는 표현식
조건을 통해 분기할 때, if, switch 그리고 조건 연산자(conditional operator)가 사용된다.
피연산자가 3개라서 삼항 연산자(ternary operator)라고도 불림

`score>90 ? '합격' : '불합격';`


### spread 구문
배열에서 주로 사용되고
배열로 합쳐진 요소들로 펼칠 때 사용하는 문법
배열 앞에 ...를 붙이면 됨

```js
const number = [1,2,3];

console.log(number)     //[1,2,3]
console.log(...number)      //1,2,3
```

rest parameter와 비슷하게 생겼지만 반대의 기능을 함

배열은 참조형이기 때문에 배열을 복사할 때 주소값이 넘겨진다.
따라서 배열을 복사하려면 slice()를 사용해야하지만
다음과 같이 spread 문법을 사용해도 된다.

```js
const list=number.slice();
const list=[...number];
```
	
또, 이런 식으로 spread된 요소 이외에도 추가할 수도 있고,
두 개 이상의 배열을 합칠 수도 있다.

```js
const list=[...number, 4, 5];
const list=[...number, ..list];
//const list=list.concat(number) 와 같음
```

배열의 argument로도 사용할 수 있다.

`printArguments(...number);`

spread된 문법을 객체로 만들면 인덱스를 키로하는 객체가 만들어 진다.

객체도 spread 문법 사용가능함

```js
const latte = {
	esspresso: '30ml',
	milk: '150ml'
};

const cafeMocha = {
	...latte,
	chocolate: '20ml',
}

console.log(latte); // {esspresso: "30ml", milk: "150ml"}
console.log(cafeMocha); // {esspresso: "30ml", milk: "150ml", chocolate: "20ml"}
```

배열을 Spread 하면 새로운 배열을 만들거나 함수의 아규먼트로 쓸 수 있었지만, 
객체로는 새로운 배열을 만들거나 함수의 아규먼트로 사용할 수는 없다
따라서 객체를 spread할 때는 반드시 객체를 표현하는 중괄호 안에서 활용해야 한다


### 모던한 프로퍼티 표기법
객체의 활용할 변수의 이름과 property name이 같다면 하나만 작성하는 표현 가능

```js
const name='구자용';
const birth='2000';
const job='student';

const user={
	name,
	birth,
	job,
};
```

객체의 메소드 또한 이름이 겹친다면 하나만 작성할 수 있고
객체 내에서 선언한 메소드는 콜론과 fucntion 키워드를 생략할 수 있다.

```js
function getAge() {
	const date = new Date();
	return date.getFullYear() - this.birth + 1;
}

const user = {
	getAge,
	name: '구자용',
	birth: 2000,
};

const user = {
	name: '구자용',
	birth: 2000,
	getAge() {
		const date = new Date();
		return date.getFullYear() - this.birth + 1;
	},
};
```

객체 내에서 선언되는 변수 이름을 대괄호를 작성해 표현식으로 나타낼 수 있다.
이를 계산된 속성명(computed property name)이라고 한다.

```js
const propertyName = 'birth';
const getJob = () => 'job';

const codeit = {
	['Full' + 'Name']: '구자용',
	[propertyName]: 2000,
	[getJob()]: 'student',
};
```


### 옵셔널 체이닝(Optional Chaining)
객체를 활용해서 데이터를 표현하다 보면 중첩된 객체를 작성하게 될 일이 빈번하다.
그러나 없는 요소를 접근하려고 하면 오류가 나기 때문에 주의를 요한다.
이럴 때 사용할 만한 방법 2가지가 있다

```js
function printCatName(user) {       //AND 연산자 사용하기
	console.log(user.cat && user.cat.name);
}

function printCatName(user) {       //Optional Chaining 사용하기
	console.log(user.cat?.name);
}

function printCatName(user) {       //위 Optional Chaining랑 완전히 같음
	console.log((user.cat === null || user.cat === undefined) ? undefined : user.cat.name);
}
```


### Destructuring(구조 분해)
배열과 객체에 대해서 Destructuring을 할 수 있는데,
각각이 적용되는 방식이 다르다.

##### 배열 Destructuring
아래는 배열을 Destructuring하는 방법이다.

```js
const rank=[a,b,c,d];

const [first,second,third,fourth]=rank;
const [first,...rest]=rank;
const [first,second,third,fourth,fifth]=rank;       //fifth는 undefined
const [first,second,third,fourth,fifth=null]=rank;
```

이를 이용해서 두 개의 변수를 서로 교환하는 방법을 쉽게 구현할 수 있다.

```js
let a=1;
let b=2;

[a,b]=[b,a];
```

##### 객체 Destructuring
객체는 배열과는 조금 다르다.

```js
const myBestArt = {     //기본 사용법
	title: '별이 빛나는 밤에',
	artist: '빈센트 반 고흐',
	year: 1889,
	medium: '유화',
};
const {title,artist,year,medium}=myBestArt;     //vaule가 들어감


const myBestSong = {        //rest parameter 사용하기
	title: '무릎',
	artist: '아이유(IU)',
	release: '2015.10.23.',
	lyrics: '모두 잠드는 밤에...'
};
const {title:songName,artist:singer,...rest}=myBestSong;        //rest는 객체임


const menu1 = { name: '아메리카노' };
const menu2 = { name: '바닐라 라떼', ice: true };
const menu3 = { name: '카페 모카', ice: false };

function printMenu(menu) {
	//  menu 파라미터로 전달되는 객체에 ice 프로퍼티가 없을 경우 기본값은 true여야 함
	const {name, ice=true} = {...menu};     

	console.log(`주문하신 메뉴는 '${ice ? '아이스' : '따뜻한'} ${name}'입니다.`);
}


const myBestArt = {
	title: '별이 빛나는 밤에',
	artist: '빈센트 반 고흐',
	year: 1889,
	medium: '유화',
	'picture num': '010101010'
};

const {title:name,artist,year,medium}=myBestArt;        //property이름을 새로운 이름의 변수로 선언함
const {title:name,'picture-num':num,...rest};       
//property이름이 띄어쓰기가 들어있다면 변수로 할당할 수 없기 때문에 이렇게 이름을 바꾸는게 필수일 수 있다.
```

##### 함수와 Destructuring
Destructuring 문법을 이용하면 중첩 객체 구조를 분해(Nested Obejct Destructuring)하는데 도움이 된다.

```js
const music = { title: '난치병', singer: '하림' };
printFavoritSong('동욱', music);

//아래 3개는 같은 결과값이 나온다.
function printFavoritSong(name, music) {
	console.log(`최근 '${name}'님이 즐겨듣는 노래는 '${music.singer}'의 '${music.title}'이라는 노래입니다.`);
}
function printFavoritSong(name, music) {
const { singer, title } = music;
	console.log(`최근 '${name}'님이 즐겨듣는 노래는 '${singer}'의 '${title}'이라는 노래입니다.`);
}
function printFavoritSong(name, { title, singer }) {
	console.log(`최근 '${name}'님이 즐겨듣는 노래는 '${singer}'의 '${title}'이라는 노래입니다.`);
}
```


### 에러와 에러 객체
에러는 발생한 이후 코드가 실행되지 않는다는 특징이 있다.

에러를 완벽하게 막는 건 불가능에 가까으므로, 에러를 다루는 건 중요하다.
주로 ReferenceError, TypeError, SyntaxError 와 같은 에러가 많고,
특히, SyntaxError 같은 경우는 컴파일 과정에서 에러를 잡기 때문에 실행 자체가 안된다.

이러한 에러를 의도적으로 발생시킬 수 있는데, 에러 객체는 이름과 메시지가 있어야 한다.

```js
const error = new TypeError('타입 에러발생');

console.log(error.name);
console.log(error.message);

throw error;
//이후 코드 실행 안함
```

SyntaxError 처럼 실행 자체를 안하는 애러를 제외하고, 
실행을 하는 에러에 대해서 예외(Exception) 이라고 하고 
이러한 예외를 처리하는 과정을 예외 처리(Exception Handling)라고 한다.


### try catch문
```js
try{
	const error = new TypeError('타입 에러발생');
	throw error;
} catch(err) {
	console.log(err.name);
	console.log(err.message);
	//진짜 에러처럼 나오게 하려면 아래처럼
	console.error(err.name);
	console.error(err.message);
}
```


### finally문
에러처리 끝내고 하고싶은 동작이 있을 수 있다.
finally문을 통해 해결할 수 있다.

```js
function printMembers(...members) {
	for (const member of members) {
		console.log(member);
	}
}

try {
	printMembers('영훈', '윤수', '동욱');
} catch (err) {
	alert('에러가 발생했습니다!');
	console.error(err);
} finally {
	const end = new Date();
	const msg = `코드 실행을 완료한 시각은 ${end.toLocaleString()}입니다.`;
	console.log(msg);
}
```



# 자바스크립트의 유용한 내부 기능
