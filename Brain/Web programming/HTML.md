HTML이란?
Hyper Text Markup Language
하이퍼텍스트(hypertext)
	서로 링크로 연결된 문서

마크업 언어(markup language)
	마크업하는(추가적인 표시를 하는) 프로그래밍 언어
	
서로 연결되는 문서를 구조와 의미도 표시하는 언어


HTML 기본 문법
```html
<a href='rsv.html'>예약</a>

태그
꺽쇠로 감싸진 것
	<a href='rsv.html'>예약</a>

태그이름
꺽쇠 바로 옆에 있는 것
	a

시작태그
태그 중 앞에 있는 것
	<a href='rsv.html'>

종료태그
태그 중 뒤에 있는 것
종료 태그 앞엔 /가 붙음
	</a>

내용
시작태그와 종료태그 사이에 들어감
	예약

속성
시작태그에 있음
href='rsv.html'
속성이름, 속성값

참 거짓을 나타내는 속성은 속성이름만 쓸 수도 있음
	<video src='asdf.mp4' autoplay> 참
	<video src='asdf.mp4'> 거짓
```


HTML 구조 + 주석다는 방법
```html
<!DOCTYPE html> <!--html 파일이라는 걸 알려줌-->
<html>
	<head>
		페이지에 대한 정보가 들어가는 부분
	</head>
	<body>
		화면에 보이는 내용이 들어가는 부분
	</body>
</html>
```

여러 줄 주석은 혹은 한 줄 주석은 보통 ctrl+/ 을 하면 됨



# 링크
```html
<a href='https://movie.naver.com'>
<a href='contents.html'>
```

href 속성으로는 사이트 주소와 파일이름(파일 경로)를 사용할 수 있음

./    현재 디렉토리
../    이전 디렉토리
/    홈 디렉토리


페이지 안에서 이동하기
url fragment
주소 맨 뒤에 붙어서 한 페이지 내에서 일부분을 나타내는 것

	www.naver.com#ad-element

위에 예시에서는 ad-element라는 id를 가진 위치로 이동할 것이다.


새 창 열기
```html
새 창으로 열기
	<a href='contents.html' target='_blank'>

기존 창으로 열기
	<a href='contents.html' target='_self'>
	
탭에 이름 붙이기
content라는 이름의 새 창 만드고 열기
	<a href='contents.html' target='content'>

만든 이 후 content 탭을 대상으로 새 창 열기
	<a href='contents.html' target='content'>
```
			
다양한 링크 동작
링크는 보통 해당 주소의 페이지로 연결
https:// 나 http:// 대신에 다른 내용을 넣으면 
페이지 연결 외에 다른 동작들도 가능 
이런 약속들을 URI 스킴(URI Scheme)

이메일 보내기
mailto:<이메일 주소>라고하면 이메일을 보낼 수 있음
이 링크를 클릭하면 이메일 프로그램이나 이메일 앱을 열 수 있고,
받는 사람 주소에 링크에 적힌 이메일 주소를 자동으로 입력해 줌
	
	<a href="mailto:test@example.com">메일 보내기</a>

전화 걸기
tel:<전화번호>를 사용하면 전화를 걸 수 있음
스마트폰에서 이 링크를 클릭하면 전화 앱으로 연결됨

	<a href="tel:+821012340123">전화 걸기</a>


# 텍스트 태그
`<h1>`은 웹 브라우저에서 큰 글자로 두껍게 보이지만 
이런 겉모습이 제목 태그의 본질은 아님
`<h1>`태그의 본질은 현재 페이지에서 가장 큰 제목이라는 의미
이런 식으로 태그가 가지고 있는 의미에 대해 이해하는 게 중요

```html
제목 태그 <h1> ~ <h6>
문서의 제목을 나타내는 태그

	<h1>한국 영화</h1>

	<h2>한국 영화의 역사</h2>
	<h3>1950년대: 침체기</h3>
	<h3>1960년대: 황금기</h3>
	<h3>1970년대: 쇠퇴기</h3>

	<h2>유명한 한국 감독</h2>
	<h3>박찬욱</h3>
	<h3>봉준호</h3>
	<h3>임권택</h3>
	
본문 <p>
본문을 작성할 때 쓰는 태그

	<h1>한국 영화</h1>

	<h2>한국 영화의 역사</h2>
	<h3>1950년대: 침체기</h3>
	<p>
		1950년대에는 한국전쟁이 일어나면서 영화계는 침체를 맞게 됩니다.
		하지만 1950년대 중반을 지나서 그 사이 발전된 기술에 힘입어
		점점 많은 영화가 나오기 시작하더니 1950년대 후반에 들어서는 1년에 100편 가까이 제작되었습니다.
	</p>
	<h3>1960년대: 황금기</h3>    
	
줄바꿈 <br>
제목이나 본문 같은 데서 줄을 바꿀 때 사용하는 태그
줄 바꿈이 없으면 보통 아래처럼 한 문단으로 이어서 보여줌

	<p>
		1950년대에는 한국전쟁이 일어나면서 영화계는 침체를 맞게 됩니다.<br>
		하지만 1950년대 중반을 지나서 그 사이 발전된 기술에 힘입어
		점점 많은 영화가 나오기 시작하더니 1950년대 후반에 들어서는 1년에 100편 가까이 제작되었습니다.
	</p>
 
중요 <strong>
중요한 내용을 강조해서 표시할 때 사용하는 태그
크롬 브라우저에서는 기본적으로 <strong> 태그를 두꺼운 글씨로 보여줌
꾸미기 위해 두꺼운 글씨를 넣으려면 CSS로 두꺼운 글씨를 만들고
의미상 강조의 의미가 있는 경우에만 <strong>을 사용

	<p>
		코드잇 영화관에서는 영화 상영 전 광고없이 정시에 상영을 시작합니다.
		정시에 입장하여 관람중인 관객들을 위해
		<strong>상영 시작 10분 후에는 입장이 제한됨을 알려드립니다.</strong>
	</p>

강조 <em>
글은 말하는 것과 달리 억양을 다르게 표현하기 힘들다는 단점이 있음
책이나 잡지 같은데서는 전통적으로 글자를 조금 
다른 모양으로 보여주거나 하는 식으로 억양을 표현
HTML에서도 <em> 이라는 태그를 사용해서 이런 내용의 강조를 나타낼 수 있음
크롬 브라우저에서는 <em> 태그의 기본 디자인을 기울어진 글씨로 보여주는데,
영어권에서 강조할 때 주로 사용하는 표시

	<p>
		제 이름은 윤 <em>여정</em>입니다. 요정도 아니고 유정도 아니고 여정이죠.
	</p>

취소 <s>
어떤 내용을 적었다가 지우지 않고, 지웠다는 표시만 남기고 싶을 때
어떤 내용이 취소, 제거되었다는 의미를 표현할 때 <s> 태그를 사용

	<p>
		<s>단체 관람을 원하시는 분들은 코드잇 홈페이지에서 예약해주세요.</s>
		<br>
		현재 코로나 방역으로 인해 극장 입장을 20인으로 제한하고 있어 단체 관람이 어렵습니다.
	</p>
	
인용 <blockquote>, <q>
다른 곳에서 가져온 내용을 긴 글로 인용할 때

	<blockquote>
		또 감사드릴 분이... 저는 경쟁을 싫어합니다. 제가 어떻게 글렌 클로즈를
		이기겠어요? 저는 그녀의 영화를 수없이 많이 봤습니다. 5명 후보가 모두 각자 다른
		영화에서의 수상자입니다. 우리는 각자 다른 역을 연기했잖아요. 우리끼리 경쟁할
		순 없습니다. 오늘 제가 여기에 있는 것은 단지 조금 더 운이 좋았을 뿐이죠.
		여러분보다 조금 더 운이 좋았네요. 그리고 아마도 미국인들이 한국 배우를
		대접하는 방법일 수도 있죠. 아무튼 감사합니다.
		<br>
		- 윤여정, 오스카 수상소감 중에서
	</blockquote>
	
글 안에서 짧게 인용할 때는 <q> 를 사용

	<p>
		윤여정은 오스카에서 김기영 감독에 대한 애정을 표시하기도 했습니다.
		<q>
			저는 이 상을 저의 첫 번째 감독님, 김기영에게 바치고 싶습니다.
			아주 천재적인 분이셨고 제 데뷔작을 함께 했습니다.
		</q>
		수상 소감의 마지막을 그녀가 존경하는 한국의 천재 감독을 언급한 것이죠.
	</p>
	
크롬 브라우저에서는 기본적으로 <q> 태그를 따옴표로 감싸는 디자인으로 보여줌

주제 전환(Thematic Break)
과거에는 가로 선(Horizontal Line)이라고 불러서 <hr> 라고 쓰지만, 
최근 HTML에서는 글에서 주제를 전환할 때 쓰는 태그
브라우저에서는 기본적으로 가로 선을 그어서 보여줌

	<p>
		윤여정은 오스카에서 김기영 감독에 대한 애정을 표시하기도 했습니다.
		<q>
			저는 이 상을 저의 첫 번째 감독님, 김기영에게 바치고 싶습니다.
			아주 천재적인 분이셨고 제 데뷔작을 함께 했습니다.<sup>[1]</sup>
		</q>
		수상 소감의 마지막을 그녀가 존경하는 한국의 천재 감독을 언급한 것이죠.
	</p>
	<hr>
	<p>
		[1] "윤여정, 오스카 최고의 수상소감"…미국 '들썩', KBS뉴스 2021.04.27.
	</p>
	
미리 서식이 정해진 텍스트 <pre>
본문 태그인 <p> 처럼 글을 이어서 보여주는 게 아니라, 
HTML에 적혀있는 그대로 보여주는 태그
보통 코드 같은 걸 쓸 때 많이 사용

	<p>body 태그의 배경색과 글자색을 바꾸는 CSS 코드입니다.</p>
	<pre>
		body {
			background-color: #000000;
			color: #ffffff;
		}
	</pre>

코드 <code>
글 안에서 짧은 코드를 작성할 때 사용

	<p><code>body</code> 태그의 배경색과 글자색을 바꾸는 CSS 코드입니다.</p>
	<pre>
		body {
			background-color: #000000;
			color: #ffffff;
		}
	</pre>
	
위첨자 <sup>
윗첨자(superscript) 텍스트를 표현할 때 사용

	<p>제곱 공식은 다음과 같습니다.</p>
	<p>(a+b)<sup>2</sup> = a<sup>2</sup> + 2ab + b<sup>2</sup></p>
	
아래첨자 <sup>
아래첨자(subscript)를 표현할 때 사용

	<p>이것은 아래첨자<sub>아래첨자</sub> 입니다.</p>
```
# 리스트
```html
순서리스트

<ol>
	<li>명량</li>
	<li>극한직업</li>
	<li>신과함께</li>
	<li>국제시장</li>
	<li>어벤져스</li>
</ol>

순서 없는 리스트
<ul>
	<li>명량</li>
	<li>극한직업</li>
	<li>신과함께</li>
	<li>국제시장</li>
	<li>어벤져스</li>
</ul>

리스트 스타일링
type으로는 a,A,i,I,1 가 있음

	<ol type='a'>
		<li>명량</li>
		<li>극한직업</li>
		<li>신과함께</li>
		<li>국제시장</li>
		<li>어벤져스</li>
	</ol>
	
css 스타일링을 더 많이 사용함
disc, none, hangul, decimal, decimal-leading-zero 등이 있음

	ol{
		list-style: dics;    /*ul태그 처럼 보임*/
	}
	
특히, none이 자주 사용되는데

	ul{
		list-style: none;
		margin: 0;
		padding: 0;
	}
	
	ul > li{
		display: inline-block;
		border: 1px solid #dddddd;
		border-radius: 24px;
	}
	
이런식으로 디자인 하면 가로로 내용이 이쁘게 정렬되어 있어서
마치 div 태그로 스타일링 한 것 같지만
html 상으론 리스트임을 나타낼 수 있어서 자주 사용한다.
	
```
# 테이블

```html
<table>
  <thead>        /*머리글*/
	<tr>
	  <th></th>        
	  <th>Premium</th>        /*row나 col은 th태그로*/
	  <th>Standard</th>
	  <th>Basic</th>        
	</tr>
  </thead>
  <tbody>
	<tr>
	  <th>모바일+태블릿+PC</th>
	  <td>지원</td>
	  <td>지원</td>
	  <td>지원</td>
	</tr>
	<tr>
	  <th>TV</th>
	  <td>지원</td>
	  <td>지원</td>
	  <td>지원</td>
	</tr>
	<tr>
	  <th>화질</th>
	  <td>최대</td>
	  <td>FHD</td>
	  <td>HD</td>
	</tr>
	<tr>
	  <th>동시 시청</th>
	  <td>4명</td>
	  <td>2명</td>
	  <td>1명</td>
	</tr>
	<tr>
	  <th>다운로드</th>
	  <td>무제한</td>
	  <td>월 30회</td>
	  <td>불가</td>
	</tr>
  </tbody>
  <tfoot>
	<tr>
	  <th></th>
	  <th>₩15,900</th>
	  <th>₩10,900</th>
	  <th>₩8,900</th>
	</tr>
  </tfoot>        /*바닥글*/
</table>

table{
	border: 15px solid red;
	border-collapse: collapse;    /*table에 있는 기본적인 여백(간격) 삭제*/
	border-spacing: 15px;    /*기본여백 늘리기*/
}

th, td{
	border: 1px solid blue;
}

thead th, thead td{
	border: 1px solid green;
}
```


# 멀티미디어
##### 이미지

```html
<img src='image.png' alt='영화 포스터' width='300' height='428'>
```

alt를 설정해두면 이미지가 로드가 안되었을 때 텍스트를 보여주고
시각 장애인 용 사이트를 만들 때 자동으로 읽어준다고 한다.

##### 비디오

```html
<video src='video.mp4' autoplay muted controls></video>
```

autoplay는 사이트를 로드했을 때 자동 재생
muted는 영상을 재생할 때 음소거 상태로 재생
크롬 브라우저 같은 경우는 광고 때문에 autoplay와 muted를 같이
설정해야지 자동 재생된다고함
controls는 영상에 영상 재생용 컨트롤 패널을 주는 옵션
width,height도 설정 가능
	
##### 오디오
	<audio src='audio.mp3' control autoplay></audio>

크롬은 autoplay안됨 safari는 가능

꿀팁
태그를 서로 붙여서 써야 태그들 사이에 불필요한 공백이 생기지 않음
width와 height를 추가할 때 px과 같은 단위를 빼고 줘야함

##### iframe
인라인프레임이라는 뜻
html파일 안에 다른 html 문서를 불러올 때 사용하는 태그이다.
youtube영상이나 배너 광고 결재창등 다른 사이트의 요소를 가져올 때
사용하면 된다.

```html
<iframe src='other.html' width='230' height='120'></iframe>
```
# 폼
브라우저에서 서버에 접속할 때 로그인 양식을 주고 입력을 요구한다
이러한 양식을 폼이라고 하고 폼에는
입력을 받는 칸 인풋 입력을 받는 칸의 이름을 라벨 그리고 버튼이 있다.

```html
<form>
  <div>
	<label for="signup-email">이메일</label>
	<input id="signup-email" name="email" type="email">
  </div>
  <div>
	<label for="signup-password">비밀번호</label>
	<input id="signup-passowrd" name="password" type="password">
  </div>
  <div>
	<label for="signup-password-repeat">비밀번호 확인</label>
	<input id="signup-password-repeat" name="password-repeat" type="password">
  </div>
</form>
```

참고로 label의 for속성과 input의 id속성을 똑같이 쓰는 방법말고
label 태그로 감싸는 방법이 있다.
이렇게 하면 라벨을 클릭했을 때 인풋에 포커싱이 된다.

```html
<label>이메일
	<input>
</label>                                                            
```

#### button태그
전송할 때는 button이라는 태그를 사용하는데, 
button은 type라는 속성을 가지고 있다.

```html
<form>
  <div>
	<label for="signup-email">이메일</label>
	<input id="signup-email" name="email" type="email">
  </div>
  <div>
	<label for="signup-password">비밀번호</label>
	<input id="signup-passowrd" name="password" type="password">
  </div>
  <div>
	<label for="signup-password-repeat">비밀번호 확인</label>
	<input id="signup-password-repeat" name="password-repeat" type="password">
  </div>
  <button type='button'>
	  확인
  </button>
</form>
```

type의 기본값을 submit 이고 이는 입력한 폼을 전송한다. 
type를 button으로 바꾸면 아무런 동작을 하지 않고
reset으로 바꾸면 입력한 내용이 초기화 된다.

disabled이라는 속성이 있는데, True면 숨겨짐


#### 폼 전송하기
##### action 속성
폼을 전송하면 현재 사이트로 입력한 내용을 보낼 것이다.
예를 들어 쿼리스트링이 다음과 같다고 한다.

	http://127.0.0.1:3000/
	?
	email=html%40codeit.kr
	&
	password=ilovehtml
	&
	password_repeat=ilovehtml
	
현재 페이지에 3가지 내용을 전송하게 될 것이다.

그러나 form 태그의 action속성을 사용하면 
다른 사이트로 폼을 전송할 수 있다.

	<form action="https://google.com/search">
	  <input name="q">
	  <button>검색</button>
	</form>

	https://google.com/search?q='hi'
	
##### method 속성
웹 브라우저는 페이지를 이동하거나, 
어떤 데이터를 전송할 때 서버에 "리퀘스트"라는 걸 보냄

리퀘스트의 종류에는 여러 가지가 있음
GET 리퀘스트는 데이터를 받을 때 사용하고, 
POST 리퀘스트는 데이터를 보낼 때 쓰는 것

폼 버튼을 눌렀을 때 페이지를 이동하는 건, 
웹 브라우저가 어떤 서버로 GET 리퀘스트를 보낸 것

용량이 큰 사진같은 데이터를 보낼 때 GET리퀘스트와 퀘리스트링으론 힘듬
이럴 때 POST 리퀘스트를 사용
``<form>`` 태그의 method 속성을 바꿔 주면 POST 리퀘스트를 보낼 수 있음

추가적으로 GET으로 보냈을 때 입력한 내용이 url에 모두 나오는데
POST는 body 안으로 숨겨서 보내줌
그런데 이렇게 숨겨도 다 찾을 수 있음

#### 다양한 input
##### 체크박스 checkbox
한 항목만 선택하는 경우
아래 예시에서는 "동의합니다"에 체크하는 경우 agreement의 값이 
on이라는 문자열로 지정

```html
<label>
  <input name="agreement" type="checkbox">
  동의합니다
</label>
```

여러 항목 중에서 몇 항목을 선택하는 경우
`<input>` 태그에 value 속성으로 값을 지정해 주면, 
선택된 항목의 지정된 값이 입력됨 
예를 들자면 아래 코드에서는 "액션"이랑 "코미디"를 선택했을 때 
film의 값으로 action과 comedy라는 문자열이 지정됨
폼을 전송했을 때 쿼리 문자열에서는 &film=action&film=comedy처럼 전송

```HTML
<label for="film">좋아하는 영화 장르</label>
<label>
  <input name="film" value="action" type="checkbox">
  액션
</label>
<label>
  <input name="film" value="comedy" type="checkbox">
  코미디
</label>
<label>
  <input name="film" value="romance" type="checkbox">
  로맨스
</label>
```

##### 날짜 date
선택한 날짜로 값을 지정할 수 있음

``<input name="birthdate" type="date">`

##### 파일 file
파일을 선택할 수 있는 인풋

```html
<input name="avatar" type="file">

파일 형식 지정하기
	accept라는 속성을 써서 허용할 파일 확장자들을 정해 줄 수 있음

		<input name="avatar" type="file" accept=".png,.jpg">

파일 개수 지정하기
	multiple이라는 참/거짓 속성을 사용하면 여러 개 또는 한 개만 
	선택하도록 정할 수 있음

		<input name="photos" type="file" mutliple> <!-- 여러 개 선택 가능 -->
		<input name="avatar" type="file"> <!-- 한 개만 선택 가능 -->
```

##### 이메일 email
텍스트를 입력할 수 있는 건 똑같지만, 버튼을 눌러서 폼을 전송할 때 
올바른 이메일 형식인지 자동으로 검사해 줌

``<input name="email" type="email">``


##### 숫자 number
숫자를 입력하고, 최소 최대 값이나 버튼을 눌렀을 때 증가, 감소할 양을 
정할 수 있음

```html
<input type="number">

<!-- 100에서 1000사이 -->
<input type="number" min="100" max="1000">

<!-- 100에서 1000사이, 버튼을 눌렀을 때 100씩 증가, 감소 -->
<input type="number" min="100" max="1000" step="100">
```

##### 비밀번호 password
값을 입력했을 때 입력한 내용이 숨겨짐

	<input type="password">


##### 라디오 radio
동그란 선택 버튼
체크박스와 다르게 여러 항목 중 하나의 항목만 선택할 수 있음
value 속성과 같이 사용하면, 같은 name을 가진 `<input>` 태그들 중에, 
선택한 `<input>`의 value 값을 입력하도록 할 수 있음
예를 들어서 아래 코드에 "좋음"을 선택하면 feeling의 값으로 3이라는 
값이 들어가게 됨
꼭 name 속성이 같아야함

```html
<input id="very-bad" name="feeling" value="0" type="radio">
<label for="very-bad">아주 나쁨</label>
<input id="bad" name="feeling" value="1" type="radio">
<label for="bad">나쁨</label>
<input id="soso" name="feeling" value="2" type="radio">
<label for="soso">보통</label>
<input id="good" name="feeling" value="3" type="radio">
<label for="good">좋음</label>
<input id="very-good" name="feeling" value="4" type="radio">
<label for="very-good">아주 좋음</label>
```

##### 범위 range
범위 안에서 선택할 수 있는 인풋

```html
<label for="signup-feeling">현재 기분</label>
<input id="signup-feeling" name="feeling" min="1" min="10" type="range">
```

##### 텍스트 text
인풋 타입의 기본 값
일반적인 텍스트를 입력할 때 사용

	<input name="nickname" type="text">


##### 옵션 선택 `<select>`
미리 정해져 있는 여러 값들 중에서 하나를 선택할 수 있는 태그
`<select>` 태그 안에 `<option>` 태그를 value와 함께 사용하면 됨
예를 들어서 아래 코드에서 드라마를 선택하면 
genre의 값이 drama가 됨


<label for="genre">장르</label>
```html
<select id="genre" name="genre">
  <option value="korean">한국 영화</option>
  <option value="foreign">외국 영화</option>
  <option value="drama">드라마</option>
  <option value="documentary">다큐멘터리</option>
  <option value="vareity">예능</option>
</select>
```

##### 긴 글 `<textarea>`
긴 글을 입력할 수 있는 인풋
`<input>` 태그와 달리 반드시 종료 태그(`</textarea>`)를 써 줘야함

	<textarea name="content"></textarea>


#### 유용한 input 태그 속성
min
최소값 설정

##### placeholder
값이 비어있을 때 보여주는 값

	<input name="username" placeholder="이메일 또는 휴대전화">

##### required
반드시 입력해야 하는 값

	<input name="email" type="email" required>

##### autocomplete
자동 완성 기능 활성화
폼이 전송될 때마다 입력한 값을 브라우저에 저장해 두고
나중에 입력할 때 추천해 줌

	<input name="search" type="text" autocomplete="on">
	<input name="email" type="email" autocomplete="email">
	<input name="telephone" autocomplete="tel">



# 다른 코드 불러오기
link 태그
다른 코드를 불러오는 용도이다.
css나 구글 폰트, 아이콘 같은 걸 불러올 수 있다.
 어떤 목적인지를 rel 속성에 
 위치는 href로 
 주로 `<head>` 태그 안에서 맨 마지막에 써 줌

	<link rel='stylesheet' href='style.css'>
	<link rel="preconnect" href="https://fonts.googleapis.com">
	
웹브라우저에서 보이는 아이콘을 파비콘(favicon)이라고함
	<link rel='icon' href='favicon.ico'>


script 태그
자바스크립으로 짜진 스크립트 언어를 불러올 수 있다.
 주로 `<body>` 태그 안에서 맨 마지막에 써 줌

	<body>
	   <script src='script.js'></script>
	</body>
	
		

# 의미있는 HTML
head 태그
페이지에 대한 정보를 담고 있는 태그
주로 이 페이지에 대한 데이터를 담고 있는데, 
화면에 보여 주기보다는 웹 브라우저가 읽어서 처리하는 용도


시맨틱 태그
`<div>`와 기능은 똑같지만, 의미가 담겨있는 태그들을 '시맨틱 태그'라고 함
시맨틱 태그를 잘 활용하면 검색 엔진 최적화(SEO)나 
접근성(Accessibility)을 높이는데 도움이 됨

```html
<header>	영역 위쪽에서 로고나 제목, 메뉴 같은 걸 담고 있는 도입부
<main>	사이트의 본격적인 내용으로 페이지에서 딱 한 번만 사용 가능
<footer>	영역 아래쪽에서 여러 가지 연락처나 관련 정보를 담고 있음
<article>	하나의 완성된, 독립적인 내용을 나타내는 영역
<section>	어떤 것의 일부분을 나타내는 영역
<figure>	이미지와, 이미지 설명을 담고 있는 영역
```