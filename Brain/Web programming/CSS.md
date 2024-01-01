
# 캐스케이딩(cascading)

# css 규칙
css속성을 하나나 태그에 넣기보다는 css규칙을 정해 놓고 사용하는게 좋음

	선택자 {
	  속성: 속성값;
	  속성: 속성값;
	}


# css 선택자
태그 이름
모든 태그에 스타일 적용

	h3 {
	  font-size: 24px;
	}

id
id는 중복되면 안됨

	<h3>우도</h3>
	<h3 id="hallasan">한라산 국립공원</h3>
	<h3>성산 일출봉</h3>
	<h3>군산 오름</h3>

	#hallasan {
	  color: #f56513;
	}

class
여러 요소에 중복해서 사용할 때 사용함

	<h3 class="place">우도</h3>
	<h3 class="place" id="hallasan">한라산 국립공원</h3>
	<h3 class="place">성산 일출봉</h3>
	<h3 class="place">군산 오름</h3>

	.place {
	  font-size: 16px;
	  font-weight: 400;
	}



# 자주 쓰는 CSS 속성
### 색상 단위
색상 코드
`#`으로 시작하는 여섯 글자의 코드
빨강, 초록, 파랑 값을 0~255 사이의 정수로 표현한 다음 이걸 16진수로 표현
대소문자 구분안함

	#FFFF00
	#ffff00

RGB
빨강, 초록, 파랑 값을 0~255 사이의 정수로 표현

	rgb(255, 255, 0)

RGBA
빨강, 초록, 파랑, 알파 값을 순서대로 써서 색상 표현

	rgba(255, 255, 0, 0.5)


### 크기 단위
절대적인 크기
픽셀 px
화면을 표시하는 기준이 되는 크기

상대적인 크기
퍼센트 %
부모 태그의 크기에 상대적으로 지정할 때 사용

	<div id="parent">
	  저는 높이가 320px입니다.
	  <div id="child">
		저는 높이가 160px이에요!
	  </div>
	</div>

	#parent {
	  background-color: #A655ED;
	  height: 320px;
	}

	#child {
	  background-color: #6942D6;
	  height: 50%;
	}

em
인쇄술에서 대문자 M의 크기를 나타내는 단위
CSS에서 em은 부모 태그 font-size의 크기

	<div id="parent">
	  저는 16px입니다.
	  <div id="child">
		저는 64px이에요!
	  </div>
	</div>

		#parent {
		  font-size: 16px;
		}

		#child {
		  font-size: 4em;
		}

rem
	rem은 루트(root) em이라는 의미의 단위
	CSS에서 rem은 html 태그의 font-size 크기

	<html>
	  <body>
			저는 18px 입니다.
			<div id="other">
		  저는 32px이에요!
			</div>
	  </body>
	</html>

	html {
	  font-size: 16px;
	}

	body {
	  font-size: 18px;
	}

	#other {
	  font-size: 2rem;
	}


css주석
한 줄 주석

	/*주석*/

여러 줄 주석
	
	/*
		주석
	*/


### 텍스트 스타일링
	글자색 color

	글자크기 font-size

	글꼴 font-family
		쉼표를 연결하여 여러개 사용 가능
		왼쪽 폰트부터 써보고 적용안되면 오른쪽으로 넘어가는 방식

	글자 굵기 font-weight
		100단위로 사용

	줄 높이 line-height
		단위 없이 글자 크기에 상대적인 값
		line-height:1 이면 줄높이가 글자 크기랑 같음
		이 속성을 사용하면 image와 div 같은 요소를 같은 선상에 둘 수 있음            
		
	텍스트 꾸미기 text-decoration
		텍스트에 밑줄 취소선 등을 넣을 수 있음
		속성 값으로는 none, underline, line-through 등이 있음
		none은 <a> 태그에 기본으로 들어 간 밑줄을 없애는 데 많이 사용


### CSS 속성

margin
padding
width
height


배경 이미지 background-image
	url('pizza.png') 이미지를 배경으로
	linear-gradient(rgba(0,0,0,1),rgba(0,0,0,0)) 검은색 그라데이션
	linear-gradient(90deg,rgba(0,0,0,1),rgba(0,0,0,0)) 각도 설정
	linear-gradient(90deg,rgba(0,0,0,1),rgba(0,0,0,0)),url('pizza.png')
	이미지가 배경 그라데이션이 앞으로 와서 이쁨
	배경이미지는 먼저오는게 가장 화면 앞으로 나옴

배경 반복 background-repeat
	기본값 repeat
	no-repeat 기본적으로 타일처럼 반복이 설정되어 있는데 반복하지 않음

배경 위치 background-position
	기본값 left top
	center

배경 크기 background-size
	cover 꽉채움
	contain 비율이 깨지지않을정도로 꽉 채움
	40px 30px 처럼 구체적인 값을 정할 수 있음

그림자 box-shadow
	box-shadow 가로그림자 세로그림자 흐림효과(blur) 그림자퍼짐 색상
	box-shadow:10px 15px 20px 5px rgba(0,0,0,0.4)

불투명도 opacity
	rgba에서 a처럼 0이면 투명 1이면 불투명을 나타냄
	요소 전체를 불투명하게 만드는 것


# 우선순위
- 우선순위 판별
중요도: CSS 속성 마지막에 !important 키워드를 붙이면 가장 높은 우선순위 !important 키워드가 여러 개 사용됐다면 작성 순서가 더 늦은 것이 우선 적용

명시성: 선택자가 얼마나 구체적인지를 나타내는 값
내부적으로 명시성 값이 다음과 같이 정의 (총합이 높은 스타일이 우선 적용)
인라인 선택자: 1000
아이디 선택자: 100
클래스/가상클래스/속성 선택자: 10 
요소/가상 요소 선택자: 1 

- 작성 순서 
늦게 작성된 속성일수록 우선순위가 높음



# 박스 모델
모든 웹사이트 요소는 박스 모델을 따름
margin border padding content 순임

### Padding
영역 안쪽에 여백을 넣을 때 사용

상하좌우 한 번에

	padding: 8px;

상하, 좌우 각각

	padding: 16px 8px;

상, 좌우, 하

	padding: 16px 8px 24px;

상, 우, 하, 좌

	padding: 16px 8px 24px 10px;

숫자의 순서는 시계 방향으로 0시 → 3시 → 6시 순서


### padding- 속성
패딩 값을 각각 주고 싶을 때 쓰는 속성
앞에서 상, 우, 하, 좌 값을 따로 썼던 걸 속성으로 나눈 것

아래 두 코드는 똑같은 코드

	padding: 16px 8px 24px 10px;

	padding-top: 16px;
	padding-right: 8px;
	padding-bottom: 24px;
	padding-left: 10px;


### margin
영역 바깥쪽 여백을 넣을 때 사용
auto라는 걸 사용해서 자동으로 여백 채움
주의할 점은 요소의 width 속성이 정해져 있어야 자동으로 채울 수 있음

상하좌우

	margin: 8px;

상하, 좌우

	margin: 16px 8px;

자동으로 채우기

	width: 520px; /* 반드시 너비가 정해져 있어야 자동으로 채울 수 있음 */
	margin: 16px auto;

상, 좌우, 하

	margin: 16px 8px 24px;

상, 우, 하, 좌

	margin: 16px 8px 24px 10px;


### margin- 속성
padding 이랑 마찬가지로 값을 각각 주고 싶을 때 쓰는 속성들

	margin: 16px 8px 24px 10px;
	margin-top: 16px;
	margin-right: 8px;
	margin-bottom: 24px;
	margin-left: 10px;


### border
요소의 테두리 개념

border: 테두리두깨 태두리모양

	border: 10px solid #FFFFFF;

테두리 모양

	solid 실선
	dotted 점선
	dashed dash로 이뤄진 선 

border-radius
테두리 둥글기

	border-radius:14px;
	
타원 만들기
	
	border-radious: 50%;
	
알약 만들기

	border-radious: 9999px;


### box-sizing 
width나 height와 같은 속성을 설정하면 그 값대로
box요소가 나올 것 같으나 실제로 그러한 속성들이 적용되는
대상은 box가 아닌 box안에 content까지이다
이렇게 적용 대상을 content에서 box로 바꾸고 싶을 때 사용하는 속성이다.

	box-sizing: border-box;
	
추가적으로 box-sizing 설정은 편리한 기능이고 대부분의 요소에서 사용된다.
모든 요소에 추가하고 싶은 속성은 다음과 같은 방법으로 추가할 수 있다.

	*{
		box-sizing: border-box;
	}
	
### overflow
크기에 비해 내용이 너무 많으면 overflow가 일어난다.
	
	overflow: hidden;

hidden 넘치는 내용을 숨김
scroll 항상 내용을 스크롤로, 기본값 세로
auto 넘치면 스크롤

아래에서 설명하는 white-space 속성을 이용하면
좌우 스크롤도 구현할 수 있다.

### white-space
원래 설정된 가로 길이보다 긴 텍스트에 대해서 css는 자동으로 
다음 줄로 넘겨준다.
이러한 설정을 다루는 속성이 white-space다

	white-space: nowrap;


### 마진 상쇄(margin collapsing)
부모자식간, 상하 요소간 마진이 설정한 값대로가 아닌 겹쳐진 값 중 큰값을 택함
말 그대로 여백이기 때문.
border나 padding이 있어서 어떤 경계가 생긴다면 마지 상쇄가 일어나지 않는다.


### text-align
text 형식의 content를 가운데 정렬하게 만듬



# Display

### 블록(block)
`<h1>,<p>,<div>
위에서 아래로 배치
너비와 높이를 정할 수 있음
	
	
### 인라인(inline)
``<a>,<span>``
평소에 글쓰는 방향
화면에 꽉 차면 다음줄로 넘어감
너비와 높이를 지정할 수 없음 
그러나 예외적으로 <img>와 같이 외부 데이터를 참조한다면 가능
margin이랑 padding은 가로로(글 쓰는 방향)만 가능


### 글을 오른쪽에서부터 쓰거나 위에서 아래로 쓰는 나라는..
direction
	아랍어는 오른쪽에서 왼쪽으로 사용하는 나라인데
	direction 속성을 rtl(right got left)로 설정하면
	인라인의 방향을 반대로 바꿀 수 있다.
	
writing mode
	조선시대에는 위에서 아래로, 오른쪽에서 왼쪽으로 글을 썻는데
	writing-mode: vertical-rl 라는 속성을 추가하면
	옛날 훈민정음처럼 글이 보이게 된다.


### 인라인 블록(inline-block)
인라인 요소는 기본적으로 크기가 없다는 판정이기 때문에
padding을 넣어주거나 width, height를 조정해도
주변을 무시한다.(요소가 겹친다)
이럴 때, 인라인 요소로 사용하고 싶은데 block처럼 겹치지 않게하려면
혹은 크기를 조절하고 싶다면 inline-block을 사용하면 된다.

	display: inline-block;


### 요소를 강제로 숨기기
	display: none;


### float
사진같은 데이터를 블록 맨 오른쪽 또는 왼쪽에 배치할 때 사용
블록 안에 있는 인라인들이 자리를 비켜줌

	float: left;
	


# 선택자
css파일 안에 있는 내용을 선택자 규칙이라고 하고
첫 줄은 선택자 중괄호 안에 있는 내용을 선택자 정의라고 하고
선택자 정의는 속성과 속성값으로 구분된다.

### 선택자 목록
공통된 선택자가 있으면 따로 쓰는 것 보다
선택자 목록을 만들어서 사용하는 것이 용이하다
선택자 목록은 같은 선택자 정의를 가지고 있는 선택자 규칙을
콤마로 구분해 같은 선택자 정의에 함께 쓰는 것이다.
그런데 잘 생각해보면 이는 or 연산과 같다(Webautomation 문서 참고)

	.book-description {
	  font-size: 12px;
	  font-weight: 400;
	  line-height: 17px;
	}

	.book-info {
	  font-size: 12px;
	  font-weight: 400;
	  line-height: 17px;
	  margin: 24px 0;
	  padding: 12px 32px;
	  text-align: center;
	}
	
이렇게 정의되어 있는 스타일을

	.book-description, .book-info {
	  font-size: 12px;
	  font-weight: 400;
	  line-height: 17px;
	}

	.book-info {
	  margin: 24px 0;
	  padding: 12px 32px;
	  text-align: center;
	  
이런 식으로 공통된 부분을 따로 빼두는 방식이다.

	.book-description, 
	.book-info {
	  font-size: 12px;
	  font-weight: 400;
	  line-height: 17px;
	}

	.book-info {
	  margin: 24px 0;
	  padding: 12px 32px;
	  text-align: center;
	  
이렇게도 사용한다.
	  

### 선택자 붙여 쓰기
한 요소에 2개 이상의 클래스를 사용하고 싶다면

	<a class='closed choose'>마감</a>

이렇게 사용하면 된다.

선택자를 붙여쓰면 a선택자면서 b선택자인 요소를 뜻한다.
and연산임

	.book-description.book-info


### 자식, 자손 선택하기
자식 결합자 (Child Combinator)
바로 아래 단계 요소를 말함

	.book-container > .title

자손 결합자 (Descendant Combinator)
아래 단계 요소, 자식일 필요는 없음

	.book-container .title


### 가상 클래스(Pseudo-class)
.가 아니라 :로 시작하는 클래스    
마우스를 올리면 색이 변한다.
처럼 특정 행동을 하면 요소의 모습을 변하게 만들 수 있는 클래스

	a {
		text-decoration: none;
	}
	
	a:hover {
		text-decoration: underline;
	}
	
:hover는 가상클래스인데 마우스를 요소에 올려놨을 때
활성화되는 요소라고 생각하면 된다.

마찬가지로

:active
	클릭했을 때

:focus 
	클릭하거나 tab을 이용해서 enter키를 누르면 이동하거나
	마우스가 깜빡거리는 상태
	  
:visited
	방문한 링크일 때
	  
	  
### 전체 선택자 (Universal Selector)
모든 요소를 선택하는 선택자

	* {
	  box-sizing: border-box;
	}
	
	/*.gallery의 모든 자식 요소 선택하기*/
	.gallery > * {
	  width: 120px;
	  height: 90px;
	}
  
  
### n번째 자식 선택자(n-th child Selector)
:nth-child()를 사용
괄호 안에는 숫자나 even, odd, 2n 같은 값이 들어갈 수 있음
1부터 시작(첫 번째 자식이 1임 0아님)

	.gallery의 세 번째 자식
	.gallery :nth-child(3) { ... }
	
	.gallery의 짝수 번째 자식
	.gallery :nth-child(even) { ... }
	.gallery :nth-child(2n) { ... }
	
	.gallery 의 홀수 번째 자식
	.gallery :nth-child(odd) { ... }
	.gallery :nth-child(2n+1) { ... }
	
	첫 번째 자식, 마지막 자식
	.gallery :first-child { ... }
	.gallery :last-child { ... }
	


# 스타일 계산하기
### 캐스케이드
계단식 조형물이나 종속을 뜻함
css에서는 css 속성들을 결정할 때, 계단식 폭포처럼
css규칙을 순서에 따라 합쳐서 적용한다는 의미
개발자 도구에서 styles탭을 보면
	
	style.css:61
	
이런 식으로 스타일을 적용시킨 파일이름이 나오는데
유저가 직접 추가한 스타일들을 말한다.
반면 user agent stylesheet와 같은 스타일은 브라우저에서 자동으로
추가한 스타일인데, 이렇게 여러 스타일들이 합쳐저서
computed탭에 나오는 것이다.
그런데 이런 구조면 같은 속성에 속성값이 여러개 나오는 경우가 생긴다.
다시 styles탭을 보면 선으로 구분되어 스타일 적용되는데
같은 속성에 대해서 다른 값이 있다면 위에 있는 스타일이 적용된다.
즉 위에 속성이 아래를 덮어쓴다.
이렇게 여러 css규칙이 적용될 때 순서에 따라서 합치는 것을 cascade라고 한다.

### 캐스케이드 순서
user agent stylesheet
	브라우저가 자동으로 넣은 스타일
	캐스케이드에서 가장 우선순위가 낮음

inline-style
	브라우저에서 직접 수정한 스타일
	캐스케이드애서 가장 우선 순위가 높음
	
코드 상에 순서
	가장 나중에 쓰는 속성이 덮어씀
	
selector specificity(선택자 명시도)
	css마다 점수가 있고 점수가 높을수록 덮어씀
	구글에 specifyicity calculator 검색해보면 점수 나옴
	id,class,태그가 몇 개 있는지에 따라 점수를 계산함
	쉽게 말하면 구체적으로 요소를 가르킨거라고 생각하면됨
	
	
### 상속
조상한테서 css속성을 물려받기도 함
styles탭에 inherited from body가 조상한테 상속받은것
흐릿한건 상속 안된거임
가까운 조상일수록 높은 우선순위고
선택자로 선택된 css규칙이나 웹 브라우저 기본 시트보다는 낮음

상속되는 요소
	color, font-family, font-size, font-weight, 
	line-height, text-align 등등 너무 많아서 검색해보면됨



# CSS 방법론

- OOCSS(Object Oriented CSS)
객체 지향 디자인 원칙을 CSS에 적용해 CSS를 객체 지향 디자인이 적 용된 프로그래밍 언어처럼 관리하기 쉽게 만들고자 함
![[Pasted image 20231226154458.png]]

- SMACSS(Scalable and Modular Architecture for CSS)
확장 가능한, 모듈러 방식의 아키텍쳐를 지원하는 방법론 
다섯 가지 규칙(기본, 레이아웃, 모듈, 상태, 테마)를 지켜야 함

- BEM
스타일을 정의하기 위한 class 속성의 명명 규칙에 초점을 둠
class 속성은 CSS를 적용하기 위한 식별자로, HTML의 모든 태그는 class 속성을 사용할 수 있음 
방법론을 자체적으로 정의해 사용하는 경우들이 있으므로 많은 시간을 할애하여 공부하는 것은 권장되지 않음

# VSC에서 시작하기
[[VSC]]
vsc에서 코드 에디터 부분에 !! 작성하면 기본 템플릿나옴

	* {
	  box-sizing: border-box;
	}
	
	body {
	  font-family: Poppins, 'Noto Sans KR', sans-serif;
	  margin: 0;
}
