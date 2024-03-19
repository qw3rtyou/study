---
sticker: lucide//file
---
# 객체
중괄호 안에 property-name, property-value을 적어주면 됨
```js
let man={
	name:'구자용';
	age:24;
	'girl friend':{
		name:'허정은';
		age:24;
	}
};
```

property-name은 문자열이더라도, 따음표를 생략할 수 있음
다만 띄어쓰기가 있다면 생략하면 안됨


### 생략가능 부분(ES6 이후)
- 함수 표현식의 :function 생략 가능
- 키와 값이 같은 경우 키 만으로 축약 가능

```js
const sayNode = function() {
	console.log('Node');
}
const obj = {
	sayJS: function() {
		console.log('JS');
	},
	sayNode: sayNode
}
obj.sayNode();
obj.sayJS();
```

```js
const sayNode = function() {
	console.log('Node');
}
const obj = {
	sayJS() {
		console.log('JS');
	},
	sayNode
}
obj.sayNode();
obj.sayJS();
```

### property 접근
점 표기법
무난하게 property에 접근할 때 사용하는 방법
그러나 띄어쓰기가 있는 property-name 이라면 접근할 수 없다.
```js
man.age     //24
man.girl friend         //오류!
```

대괄호 표기법
점 표기법보다는 대부분의 경우를 커버 함 
```js
man['girl friend']      //'구자용'
man['girl' + 'friend']      //'구자용'
```

없는 걸 접근하려 하면 undefined가 출력 됨

### property 수정 및 추가
접근한 후 새로운 값을 대입해주면 됨
기존에 없던 property라면 추가,
기존에 있던 property라면 수정된다.
delete 키워드를 사용하여 기존의 property를 삭제할 수도 있다.
```js
man.name='송준호';      //수정
man.sex='m';        //추가
delete man.sex;
console.log(man.sex)        //undefined
```


### property 존재 확인
in 키워드를 사용하여 존재를 확인할 수 있다.
```js
if('name' in man){
	console.log(name.man);
}
```

### 객체의 메소드
객체에는 매소드도 들어갈 수 있다.
이름은 이미 앞에 있으니까 생략 가능

```js
let man={
	sayHello: function () {
		console.log('haloa');
	}

	name:'구자용';
	age:24;
	'girl friend':{
		name:'허정은';
		age:24;
	}
};

man.sayHello();
man.[sayHello]();
```

### for in
반복문을 통해 객체를 돌릴 때 사용함, 객체의 프로퍼티를 돌림
```js
for(변수 in 객체){
	동작구문
};

for (let key in codeit){
	console.log(key)
	console.log(key[name])
}
```

for in 반복문은 프로퍼티를 순회하게 되는데
순회하는 순서는 정수형 프로퍼티 네임을 먼저 오름차순으로 정렬한 다음
나머지 프로퍼티들은 추가한 순서대로 정렬하게 된다. 
의도치 않은 결과에 주의해야함


### Date객체
시간을 나타낼 수 있는 객체
```js
console.log(new Date())
>> Fri Mar 31 2023 03:47:47 GMT+0900 (한국 표준시)
```

Date에 값을 넣어줘서 시간대를 설정할 수 있음
1970년 1월 1일 00:00:00 UTC 기준으로 설정됨
예를 들어, Date(1000) 는 기준보다 1000밀리초 뒤임
참고로 1000밀리초는 1초
그 외에도..
```js
Date('2017-06-21')  //날짜
Date('2017-06-21T05:12:13')     //날짜+시간
Date(yyyy,MM,DD,hh,mm,ss,ms)  //(yyyy,MM,DD,hh,mm,ss,ms) 
```

마지막 형식은 yyyy,MM은 생략 불가능하고
생략하게 되면 (yyyy,MM,1,0,0,0,0)로 초기화됨
MM는 0부터 시작하고, 나머지는 1부터 시작함 (MM=4라면 may)


Date.getTime()
1970년 1월 1일 00:00:00 UTC로부터 몇 밀리초가 지났는지 리턴
위에 설명한 내용을 타임스탬프라고함

두 시각의 차이를 출력하고 싶다면 getTime()을 통해서 차이를 구할 수 있다.


시간 get 메소드
시각 정보의 특정 부분 추출할 수 있다.

	getFullYear()
	getMonth()
	getDate()
	getHours()
	getMinutes()
	getSeconds()
	getMilliseconds()


시간 set 메소드
이미 생성된 Date객체의 정보를 수정할 수 있음

	setFullYear(year, [month], [date])
	setMonth(month, [date])
	setDate(date)
	setHours(hour, [min], [sec], [ms])
	setMinutes(min, [sec], [ms])
	setSeconds(sec, [ms])
	setMilliseconds(ms)
	setTime(milliseconds)(1970년 1월 1일 00:00:00 UTC부터 밀리초 이후를 나타내는 날짜를 설정)


간단하게 시간 정보 알아내기
간단하게 시간 정보를 표현하고 싶다면 아래와 같은 메소드를 활용

	let myDate = new Date();
	console.log(myDate.toLocaleDateString()); // myDate가 가진 날짜에 대한 정보 (년. 월. 일)
	console.log(myDate.toLocaleTimeString()); // myDate가 가진 시간에 대한 정보 (시:분:초)
	console.log(myDate.toLocaleString()); // myDate가 가진 날짜와 시간에 대한 정보 (년. 월. 일 시:분:초)


현재 시간 메소드
메소드가 호출된 시점의 타임스탬프를 반환
가독성, 성능적 측면에서 좋음
```js
let myDate = new Date();
console.log(Date.now() === myDate.getTime()); // true
```


자동 수정
범위를 벗어나는 값을 자동으로 수정함
```js
let myDate = new Date(1988, 0, 32); // 1988년 1월 32일은 없음
// 2월 1일로 자동고침 되는걸 확인
console.log(myDate) // Mon Feb 01 1988 00:00:00
```


Date객체의 형변환
Date객체를 다양한 형으로 변환해보면 다음과 같다.
```js
let myDate = new Date(2017, 4, 18);
console.log(typeof myDate); // object
console.log(String(myDate)); // Thu May 18 2017 00:00:00 GMT+0900 (Korean Standard Time)
console.log(Number(myDate)); // 1495033200000
console.log(Boolean(myDate)); // true
```

여기서 number객체의 값은 의미 없는 값이 아니라,
타임 스탬프이기 때문에 사칙연산에 용이하다.
```js
let myDate1 = new Date(2017, 4, 18);
let myDate2 = new Date(2017, 4, 19);
let timeDiff = myDate2 - myDate1;
console.log(timeDiff); // 86400000 (ms)
console.log(timeDiff / 1000); // 86400 (sec)
console.log(timeDiff / 1000 / 60) // 1440 (min)
console.log(timeDiff / 1000 / 60 / 60) // 24 (hour)
console.log(timeDiff / 1000 / 60 / 60 / 24) // 1 (date)
```


날짜를 표현하는 문자열
YYYY-MM-DDThh:mm:ss형식 말고도 날짜를 표현하는 다양한 방식의 문자열이 있음
```JS
let date1 = new Date('12/15/1999 05:25:30');
let date2 = new Date('December 15, 1999 05:25:30');
let date3 = new Date('Dec 15 1999 05:25:30');
```

그러나 브라우저나 로컬 환경에 따라 결과가 다를 수 있기 때문에
기존 쓰던 방법 추천



# 배열
그냥 파이썬 리스트랑 똑같이 사용하면 됨

	list=[1,2,3,4,5,6,7,8,9,10];

그러나 존재하지 않는 요소를 접근할 수 있음

	list[20];    //undefined

그래서 존재하지 않는 요소를 추가할 때 다음과 같이 할 수 있음

	list[20]=19;
	list[20];    //19

한편, 사이에 있는 값들은 자동으로 empty로 채워짐
실제 값을 출력해보면 undefined로 출력됨

	list[15];    //undefined

배열의 요소를 삭제하고 싶다면 delete를 사용하면 된다.

	delete list[20];
	list[20];       /undefined

그런데 이렇게 하면, 길이가 그대로 20짜리인 배열이 남는다.
즉 실제 데이터는 없지만, 배열의 크기는 줄어들지 않는다는 것이다.
이를 해결하려면 아래 나오는 배열 메소드를 사용하면 된다.


### 유용한 property, 메소드
배열 길이
배열의 길이를 출력한다. 
console에 배열을 출력하면 맨앞에 괄호에 숫자가 들어 있는 걸 볼 수 있는데, 
이는 배열의 길이가 자동으로 출력된 것이다.

	list.length;     //길이, 10

배열 자르기(삭제)
splice는 2개 이상의 무언가를 이어주는 의미의 단어이다.
배열의 특정 요소를 연속적으로 없애줄 수 있다.
3번째 파라미터로 전혀 다른 배열이랑도 이어줄 수 있다.

	list.splice(10);    //인덱스 10 이후 다 삭제, delete랑 다르게 길이가 10이 됨
	list.splice(1,2);       //인덱스 1부터 2개 요소 삭제
	list.splice(1,0,123,421,356);    //3개의 값을 1번 인덱스에 추가
	list.splice(4,1,999)    //4번 요소 수정

배열의 양 끝 추가 삭제
배열의 양끝 수정도 splice()로 할 수 있지만
더 효율적이고 직관적인 방법이 있다.

list.shift();       //첫 요소 삭제
list.pop();     //마지막 요소 삭제
list.unshift(111);     //첫 요소 추가
list.push(777);        //마지막 요소 추가

배열에서 특정 값 찾기
배열에서 특정 값의 인덱스를 찾고 싶을 수 있다.
없으면 -1을 리턴한다.

	list.indexOf(10);       //처음 나오는 10의 인덱스 출력
	list.lastIndexOf(10);       //뒤에서 부터 처음 나오는 10의 인덱스 출력
	
배열에서 특정 값 존재 확인
조건문에서 사용하면 좋다. 불린값을 리턴한다.

	if(list.includes(3)){
		console.log('3 exist');
	}

배열 뒤집기
배열의 순서를 반전시킨다.

	list.reverse();     //배열 순서 반전


### for of 
for of 문은 배열의 요소들을 순회한다.
for in 은 객체 순회하는데 좋고, for of 는 배열 돌리는데 좋다고 생각하면 된다.
for in 문으로 배열을 돌릴 수 있긴 한데, 
잘못하면 배열의 메소드나 예상치 못한 값이 나올 수 있으므로 for of를 쓰는게 좋다.

	for (let element of list){
		console.log(element);
	}



# 자료형 심화
### 다양한 숫자 표기법
큰 수를 지수 표기법으로 표기할 수 있다.

	1000000000===10e9       //true
	3.5e-3===0.0035         //true

다양한 진법 표현
	
	0xff            //16진수
	0xFF            //16진수
	0o377           //8진수
	0b111111111     //2진수


### 숫자형 메소드
소수점 고정 메소드
결과값이 string으로 바뀜

	let num=0.234;
	num.toFixed(3)      //3번째자리까지 출력

진법 변환 메소드
파라미터로 몇진법으로 바꿀건지 알려주면 됨

	num.toString(2)     //2진법 변환

만약 num 자리에다가 변수 대신 그냥 상수를 넣고 싶다면

	255..toString(2)
	(255).toString(2)

이런식으로 .. 을 사용해야 한다. 한번만 사용하면 소수점으로 인식하기 때문


### Math객체
다양한 연산을 쉽게 할 수 있음

	Math.abs(-10);              //10
	Math.max(2, -1, 4, 5, 0);       //5
	Math.min(2, -1, 4, 5, 0);       //-1
	Math.pow(2,3);          //8
	Math.sqrt(25);          //5
	Math.Round(2.5);        //3
	Math.floor(2.9);        //2
	Math.ceil(2.4);         //3
	Math.random();          //0.21458369059793236


### 문자열 심화
배열에서 사용하는 메소드를 문자열에서 사용할 수 있음

	let str='qwertyou'

	str.toUpperCase();      //QWERTYOU
	str.toLowerCase();      //qwertyou
	str.indexOf('e');       //3
	str.lastIndexOf('t');   //5
	str[3]          //r
	str.charAt[3]   //r
	str.length;     //8
	str.trim();     //공백제거
	str.slice();
	str.slice(3);
	str.slice(0,2);

	for (let letter of str) {       //배열에서 사용하는 for of 문도 사용 가능
		console.log(letter);
	}

차이점도 있는데, 가장 큰 차이점은 요소를 바꿀 수 있는지(mutable) 여부이다.


### 기본형과 참조형
Number String Boolean Null undefined까지가 기본형이고
Object는 참조형이다.(배열도 객체임)

이런 참조형은 객체를 대입연산자로 복사하려고 해도 주소가 복사되기 때문에
다음과 같은 객체 복사 함수를 사용해야 한다.

	복사된_객체=Object.assign({},복사하려는_객체);


# 프로토타입
JavaScript는 전통적인 클래스 기반 상속 대신 프로토타입 기반 상속을 사용하는 언어
하나의 객체에 대한 속성과 메서드를 담고 있는 정보가 프로토타입임
이때, 다른 객체가 프로타입의 속성과 메서드를 상속받을 수 있음

-  프로토타입 체인
객체에 특정 속성이나 메서드가 없을 경우, JavaScript는 해당 객체의 프로토타입을 검사하며, 
그래도 없으면 프로토타입의 프로토타입을 계속 검사함 이를 프로토타입 체인이라고 함
이 체인은 최종적으로 `Object.prototype`에 도달하게 되며, 이후 `null`로 끝남


# 타입스크립트
자바스크립트보다 더 엄격하게 정의한 자료형 사용
자바스크립트는 데이터가 동적으로 할당돼 런타임 시 해당 변수에 값이 할당될 때까지 변수의 자료형을 알지 못함
![[Pasted image 20231226154732.png]]
![[Pasted image 20231226154820.png|400]]

- 인터페이스
![[Pasted image 20231226154903.png|400]]











# 팁
string형 변수에 앞에다가 +를 붙이면 숫자형으로 바뀜

	let num='4';
	console.log(typeof(+num));      //number