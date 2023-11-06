
# css로 스타일링 하는 방법

1. 태그에 style 속성으로 넣기
```html
<p style={color:white;}></p>
```


2. css파일 분리하기
```html
<link rel="stylesheet" href="style.css"></link>
```

```css
@style.css
p{
	color: white;
}
```

# 선택자
스타일을 넣어줄 때, p,a와 같은 태그에 스타일링을 하면 모든 p태그,
a태그에 스타일이 들어간다.
스타일링을 할 때 특정 태그를 선택하고 싶은 경우가 많은데
이때 특정 태그 하나만 선택하려면 id,
여러 태그를 선택하려면 class를 사용하면 된다
이러한 id,class와 같은 것을 선택자라고 한다

id 속성을 넣으려면 먼저 특정 태그에 id 속성을 넣고

```html
<li id='food'>
```

css 파일에서는
```css
#li{
	color:white;
}
```


태그 앞에  넣고 스타일링을 넣으면 된다
마찬가지로 class 속성을 넣으려면 먼저 특정 태그에 class 속성을 넣고

```css
<li class='food'>
```


css 파일에서는
```css
.li{
	color:white;
}
```

태그 앞에 .을 넣고 스타일링을 넣으면 된다


한편 이러한 선택자는 꼭 id, class만 있는 건 아닌데,
예를 들어 a태그는 href 속성을 통해 다른 웹페이지로 이동 할 수 있게
만드는 하이퍼링크 기능이 있다.

```html
<a href="https://fancyurl.com">
```


그런데 css 파일에서

```css
[href="https://fancyurl.com"]{
	color:white;
}
```


이런 식으로 특정 속성을 스타일하면 href 속성으로 저 주소를 가지고 
있는 모든 태그의 글자색이 변경된다.

위의 예시를 일반화하면 다음과 같다.
[attr="value"]


# 그 외 선택자

```css
@or
h2,p{
	color:white;
}

@and
b.inner1{
	color:white;
}

@중첩
li i{
	color:white;
}

@직속자식
li > i{
	color:white;
}

@와일드카드
li *{
	color:white;
}

```

중첩랑 직속자식이랑 혼동될 수 있는데
중첩은 자식이기만하면 되고 직속은 한단계 아래 자식이어야만
적용이된다.

# table 태그
웹스크래핑을 할 때 자주 다루게되는 요소, 표형태를 말함

```html
<table>
	<tbody>
		<tr>
			<th></th>
			<th></th>
			<th></th>
		</tr>
		<tr>
		</tr>
		<tr>
		</tr>
		<tr>
		</tr>
	</tbody>
</table>
```


tr는 table row, th는 table head를 말함
th는 보통 테이블의 columns의 정보를 나타내는 경우가 많음