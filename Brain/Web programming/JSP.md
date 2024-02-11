# JSP
![[Pasted image 20240116043657.png]]


---
# Servlet으로의 변환
![[Pasted image 20240116043731.png]]
![[Pasted image 20240116043747.png]]



---
# 주석
- 서버 내부에서만 처리
- `<%-- JSP 주석 --%>`


---
# 지시어 (directives)
- JSP 파일의 속성을 기술
- Container에게 해당 파일을 어떻게 처리해야 하는지 전달
- page, include, taglib


# Page Directives
- 현재 JSP 페이지의 속성을 기술
- `<%@ page 속성1=“속성값1” 속성2=“속성값2” … %>`
- JSP 파일 생성시 자동 추가
```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<%@ page import="myapp.*" %>
```


# Include Directives
- 현재의 JSP 파일에 다른 HTML이나 JSP를 포함하는 기능 제공
- 모듈화


# Taglib Directives
- 사용자 정의 태그 라이브러리를 사용하기 위한 정보 기술
- `<%@ taglib uri=“/META-INF/mytag.tld“ prefix=“mytag” %>`



# Scriptlet
- JSP 내에 java코드를 적는 부분
- `<% source code … %>`

![[Pasted image 20240116044806.png|300]]


---

# 표현식 (Expression)
- `out.println()`으로 표현된 scriptlet을 대체하는 간단한 방식
- `<%= expression %>`
- 표현식의 내용이 out.println()의 매개변수가 됨

![[Pasted image 20240116045011.png|400]]


---

# JSP 내장 객체
- JSP로부터 자동 생성되는 servlet 코드 내에 이미 선언/할당되는 객체
- Scriptlet 내에서 다른 변수와 마찬가지로 사용

| Servlet 객체 | JSP 내장 객체 instance명 |
| ---- | ---- |
| HttpServletRequest | request |
| HttpServletResponse | response |
| JspWriter | out |
| ServletContext | application |
| ServletConfig | config |
| HttpSession | session |
| PageContext | pageContext |
| JspException | exception |
| Object | page |

![[Pasted image 20240116045504.png]]


---

# include action
- 현재의 페이지에 다른 페이지를 포함시키는 기능 제공
- `<jsp:include page=“JSP name” />`

![[Pasted image 20240116045735.png|450]]

| 항목 | include directive | include action |
| ---- | ---- | ---- |
| 동작 방식 | 두 파일 내용을 하나로 합친 후 컴파일 | 실행 시점에 해당 파일을 호출해서 그 결과를 현 페이지에 포함 |
| 사용 케이스 | 정적인 페이지를 포함시킬 때 사용 | 동적인 페이지를 포함시킬 때 사용 |
|  |  |  |


# forward action
- 현재 페이지에서 제어권을 다른 페이지로 넘길 때 사용
- Servlet에서 RequestDispatcher.forward()와 동일한 기능

![[Pasted image 20240116045951.png|400]]


# forward vs. redirect
|항목|forward or request dispatch|redirect|
|---|---|---|
|동작 방식|요청에 대한 처리를 서버 내부에서 다른 component에게 위임|요청에 대해 새로운 URL을 client에게 전송해서 Client가 새로운 URL로 다시 요청을 보내도록 함|
|특징|요청에 관련된 request, response 객체가 함께 전달되어 처리|새 URL에 대한 요청이기 때문에 새로운 request, response 객체가 생성|
|사용 방법|서블릿에서는 RequestDispatcher 사용<br>JSP에서는 forward action 사용|서블릿 & JSP에서는 response 객체의 sendRedirect() 이용|


---
# JavaBeans
- JSP와의 연동을 위해 만들어진 beans
- 비즈니스 로직과 프리젠테이션 로직을 분리
- JSP beans는 컨테이너에 위치

- XxxBean 형식
- Parameter가 없는 default constructor 제공
- 클래스 내의 멤버 변수는 private으로 선언해서 direct access를 방지
- 멤버 변수명에 기반하는 getter/setter method를 생성해야 함



# JSP에서 Beans 사용
- Scriptlet 내에 java code를 통해 특정 bean 객체 접근이 가능하지만, JSP action을 이용해 bean 객체 사용 가능
- `<jsp:useBean id=“bean id” class=“bean class” scope=“범위” />`
- bean id - Bean의 인스턴스 명
- bean class - Bean 클래스 명으로 패키지 경로 포함

|객체|사용 범위|
|---|---|
|application|웹 어플 종료시까지 사용|
|session|현재 세션 종료시까지 사용|
|request|현재 request가 처리 완료될 때까지 사용|
|page|현재 페이지 내에서만 사용|

```jsp
<jsp:useBean id=“user” class=“UserBean” scope=“request”>
```
위아래는 같음
```java
UserBean user = (UserBean)request.getAttribute(“user”); 
if (user == null) { user = new UserBean(); request.setAttribute(“user”, user); }
```

![[Pasted image 20240116051702.png|400]]



---
# 표현 언어(Expression Language)
- 처음 JSTL(JSP Standard Tag Library)이 소개되었을 때 나온 것
- MVC 패턴에 따라 뷰(view) 역할을 수행하는 JSP를 더욱 효과적으로 만들려는 목적
- 간단한 방법으로 데이터를 표현하기 위해 고안된 언어인 SPEL(Simplest Possible Expression Language)에 기본을 둠

![[Pasted image 20240116052958.png|400]]

- 현재 페이지에서 출력하고자 하는 데이터(or 객체)가 미리 확보 되어 있어야 함
- page, request, application, session 내장 객체중 하나에 사용하고자 하는 객체가 있 어야만 표현언어를 이용해 데이터 출력이 가능
### 기본문법
- 표현 언어는 ‘$’로 시작한다.
- 모든 내용은 ‘{표현식}’과 같이 구성된다. 
- 표현식에는 기본적으로 변수 이름, 혹은 ‘객체_이름.멤버변수_이름’구조로 이루어진다. 
- 표현식에는 부가적으로 숫자, 문자열, boolean, null과 같은 상수 값도 올 수 있다. 
- 표현식에는 기본적인 연산을 할 수 있다.

- `${member.id} 혹은 ${member[“id”]}` → member 객체의 getId() 메서드 호출과 동일
- `${row[0]}` → row라는 이름의 컬렉션 객체의 첫 번째 값
- 기본적인 연산자를 사용할 수 있음

![[Pasted image 20240116053354.png|500]]



---
# 커스텀 태그
- 원래 JSP 페이지에서 반복적인 프로그램 로직을 캡슐화하기 위해 고안됨
- 기본적으로 제공되는 태그 이외 사용자가 확장한 태그라는 의미에서 붙여진 이름
- HTML 문서는 브라우저에 의해 해석되므로 커스텀 태그를 구현할 수 없지만, JSP 는 서버에서 해석되므로 커스텀 태그를 구현할 수 있음

![[Pasted image 20240116054039.png]]


# taglib 지시어
- 커스텀 태그를 사용하기 위해서는 태그 사용을 원하는 jsp에 taglib 지시어를 기술
- taglib 지시어는 태그에 대한 정보 수집을 위한 uri 혹은 태그파일 디렉토리와 태그 에 붙이기 위한 prefix 정보를 등록한다.
- `<%@ taglib uri=“/WEB-INF/tld/MsgTag.tld” prefix=“mytag” %>`


# 태그파일 기반 커스텀 태그
- 태그 파일을 이용하면 비교적 간단하고 JSP 페이지 개발과 유사한 구조로 태그 파 일을 만들 수 있다
- tag 지시어를 사용해 태그 파일을 선언하고 JSP 문법과 표현언어, JSTL 등을 자유 롭게 사용할 수 있다.
- .tag 파일로서, 몇 가지 제약사항을 제외하고는 대부분의 JSP 파일과 구성이 동일하다. 
- `[WEB-INF\tag]` 폴더에 저장한다. 
- 기본적인 JSP 지시어와 추가된 tag 지시어 attribute 와 variable 이라는 태그를 사용 할 수 있다.

![[Pasted image 20240116054915.png]]



# 태그 핸들러 기반 커스텀 태그
- 태그 핸들러란 커스텀 태그를 처리하는 객체를 말한다
- 태그 파일과 달리 자바 클래스를 이용해 커스텀 태그를 구현하는 방법
- 구현 난이도는 높은 편

![[Pasted image 20240116055033.png]]

- 태그 핸들러 클래스
커스텀 태그를 실제 구현한 자바 클래스다. 태그 라이브러리 기술자에서 설계된 내용을 구현해야
한다. 태그 라이브러리 기술자와 마찬가지로 태그 파일 기반의 커스텀 태그에서는 필요 없다.

- 태그 라이브러리 기술자(Tag Library Descriptor)
xml 규격으로 커스텀 태그에 대한 구조를 정의하는 파일이다. .tld 파일로 만들어지며 태그 파일 기
반의 커스텀 태그에서는 필요하지 않다.

- taglib 지시어
jsp 지시어의 한 종류로, JSP 페이지에 공통으로 필요한 정보를 기술하는 부분이다. 커스텀 태그 사
용을 위한 태그 파일 혹은 태그 라이브러리 기술자의 위치 등을 설정한다. 따라서 커스텀 태그를 사
용하는 모든 JSP 페이지에 taglib 지시어를 사용해야 한다


---

# JSTL
- 커스텀 태그 라이브러리 기술을 이용해서 일반 적으로 필요한 기능들을 표준화한 것
- 핵심(CORE), xml, I18N(국제화), 데 이터베이스(SQL), 함수(functions) 라이브러리로 구성
- 커스텀 태그 기반이므로 JSTL을 사용하는 방법은 일반적인 커스텀 태그와 같다.
- `<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>`

![[Pasted image 20240116055516.png]]

![[Pasted image 20240116055546.png]]
![[Pasted image 20240116055602.png]]



### `<c:out>` 태그
- `<c:out value=“value” [escapeXml=“{true|false}”] [default=defaultValue”]/>`
- <c:out value=“${member.name}"/>은 ${member.name}로 대체할 수 있음

![[Pasted image 20240116055807.png]]



###  `<c:set>` 태그
- 변수 값을 설정하거나 객체의 멤버변수 값을 설정할 때 사용
- `<c:set value=“value” var=“varName” [scope=“{page|request|session|application}”]/>`

![[Pasted image 20240116060041.png]]



### `<c:remove>` 태그
- 해당 scope 에 설정된 객체를 제거
- `<c:remove var=“varName” [scope=“{page|request|session|application}”]/>`

![[Pasted image 20240116060141.png]]



### `<c:catch>` 태그
- 바디에서 실행되는 코드의 예외를 처리

![[Pasted image 20240116060237.png]]



### `<c:forEach>` 태그
- 반복문과 관련된 태그로 자바의 for 문과 유사
- 가장 중요하고 널리 쓰이는 JSTL 태그 중 하나

- foreach
```jsp
<c:forEach[var="varName"] items="collection" [varStatus="varStatusName"]
[begin="begin"] [end="end"] [step="step"]>
body content
</c:forEach>
```

- forin
```jsp
<c:forEach [var="varName"] [varStatus="varStatusName"] begin="begin" end="end"
[step="step"]>
body content
</c:forEach>
```

![[Pasted image 20240116060550.png]]



### `<c:choose>` 태그
- Java switch 문과 유사
- <c:when>, <c:otherwise>와 함께 사용

![[Pasted image 20240116060708.png|350]]



### `<c:url>` 태그
- 적합한 URL 생성

### `<c:param>` 태그
- URL에 parameter 추가

![[Pasted image 20240116060813.png|350]]


---
