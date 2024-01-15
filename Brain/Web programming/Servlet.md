
# Servlet
- Client에 의해 요청된 request를 동적으로 처리하고 이에 대한 response를 생성해 내는 Java object
- Java 플랫폼에서 동적인 contents를 생성하기 위해 사용


---

# Servlet container(Web container)
- Servlet을 관리하고 실행하는 component
- 자체적으로 JVM과 JRE를 포함
- 웹서버의 URL요청을 받아 매핑되는 servlet을 실행
- JSP도 내부적으로 servlet으로 변환되어 실행

---
# 동작 방식 
![[Pasted image 20240115110126.png]]

![[Pasted image 20240115110157.png]]

---

# web.xml
- Servlet 매핑 정보를 작성
- web.xml 예
```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app version="2.5" xmlns="http://java.sun.com/xml/ns/javaee"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://java.sun.com/xml/ns/javaee https://java.sun.com/xml/ns/javaee/web-app_2_5.xsd">

	<!-- The definition of the Root Spring Container shared by all Servlets and Filters -->
	<context-param>
		<param-name>contextConfigLocation</param-name>
		<param-value>/WEB-INF/spring/root-context.xml</param-value>
	</context-param>
	
	<!-- Creates the Spring Container shared by all Servlets and Filters -->
	<listener>
		<listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
	</listener>

	<!-- Processes application requests -->
	<servlet>
		<servlet-name>appServlet</servlet-name>
		<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
		<init-param>
			<param-name>contextConfigLocation</param-name>
			<param-value>/WEB-INF/spring/appServlet/servlet-context.xml</param-value>
		</init-param>
		<load-on-startup>1</load-on-startup>
	</servlet>
		
	<servlet-mapping>
		<servlet-name>appServlet</servlet-name>
		<url-pattern>/</url-pattern>
	</servlet-mapping>
</web-app>

```


---
# Servlet Lifecycle

1. 새로운 요청이 들어오면 container가 servlet의 새로운 thread를 생성
2. 해당 thread의 service()를 호출
3. service() 내에서 요청이 GET방식인지 POST방식인지 구분해서 doGet()/doPost() 를 호출 (이때, request 객체와 response 객체가 파라미터로 전송)
4. doGet()/doPost()에서 해당 요청을 처리
5. service()가 종료되면 thread 종료

---
# HttpServletRequest
- 사용자의 요청 정보와 쿠키, 세션 등의 정보를 제공하는 interface
- Container가 이 interface를 구현한 객체를 servlet에게 제공

|메서드|설명|
|---|---|
|getParameter()|클라이언트가 입력한 파라미터의 값을 제공|
|getParameterValues()|Checkbox나 select 등으로 하나의 이름으로 여러 값을 보낸 경우 사용|
|getParameterNames()|요청시 입력된 Name 값의 Enumeration을 제공|
|getHeader()|요청의 헤더 정보를 제공|
|getCookies()|요청자의 쿠키값을 Cookie 객체의 array로 제공|
|getSession()|현재 요청자와 연결되어 사용되는 HttpSession 객체를 제공|
|getMethod()|요청자의 method (GET/POST)값을 제공|
|getRemoteAddr()|요청자의 IP address 값을 제공|

# HttpServletResponse
- 요청 처리 결과를 생성/전달하기 위한 정보를 제공하는 interface
- Container가 이 interface를 구현한 객체를 servlet에게 제공
- 주로 response로부터 Writer객체를 얻어서 HTML문서를 출력

|메서드|설명|
|---|---|
|setContentType()|요청에 대해 클라이언트에게 돌려줄 content의 타입을 결정|
|setHeader()|요청에 대해 클라이언트에게 돌려줄 content의 헤더 값을 설정|
|addHeader()|요청에 대해 클라이언트에게 돌려줄 content의 헤더 값을 추가|
|sendError()|에러가 발생했음을 알려줌|



- 예시
```java
@WebServlet("/Login")  
public class Login extends HttpServlet {  
    protected void doGet(HttpServletRequest request, HttpServletResponse response)  
          throws ServletException, IOException {  
       doPost(request, response);  
    }  
  
    protected void doPost(HttpServletRequest request, HttpServletResponse response)  
          throws ServletException, IOException {  
       LoginManager loginMgr = new LoginManager();  
       UserBean userBean = new UserBean();  
       String addr;  
       userBean.setUserid(request.getParameter("userid"));  
       userBean.setPasswd(request.getParameter("passwd"));  
       if (loginMgr.authenticate(userBean))  
          addr = "/ch07/login_success.jsp";  
       else          addr = "/ch07/login_fail.jsp";  
       request.setAttribute("userinfo", userBean);  
       RequestDispatcher dispatcher = request.getRequestDispatcher(addr);  
       dispatcher.forward(request, response);  
    }  
}
```

---
# ServletConfig 객체
- Servlet이 초기화될 때 관련 정보를 저장해서 제공되는 객체
- Container에 의해 생성되어 Servlet에게 전달됨
- web.xml에서 `<init-param>`을 읽어서 ServletConfig에 저장

```xml
<servlet>
	<servlet-name>appServlet</servlet-name>
	<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
	<init-param>
		<!-- context 디렉토리 설정 -->
		<param-name>contextConfigLocation</param-name>
		<param-value>/WEB-INF/spring/appServlet/servlet-context.xml</param-value>
		<!-- 관리자 이메일 -->
		<param-name>adminEmail</param-name>
		<param-value>admin@gmail.com</param-value>
	</init-param>
	<load-on-startup>1</load-on-startup>
</servlet>
```

- Annotaion 기반으로 설정할 수도 있음
![[Pasted image 20240115133659.png]]

- 초기화 과정
![[Pasted image 20240115133810.png|450]]

|메서드|설명|
|---|---|
|getInitParameter(name)|파라미터 중 name에 연관된 value를 리턴|
|getInitParameterNames()|파라미터의 name들을 묶어서 Enumeration으로 리턴|
|getServletContext()|ServletContext 객체를 리턴하여 웹 애플리케이션의 정보에 접근 가능 |


# ServletContext 객체
- 하나의 web application마다 하나의 ServletContext 객체가 존재
- 서버와 container에 관련된 정보를 servlet에 제공
- 포함된 모든 servlet에게 초기 파라미터를 제공할 때 유용 (ex. 회사명, DB server)
- Servlet간의 attribute 공유, 컨테이너와의 연결 등을 위해서도 사용

![[Pasted image 20240115134147.png|450]]

|메서드|설명|
|---|---|
|서버 정보 관련||
|getServerInfo()|서버의 정보를 반환합니다.|
|getMajorVersion()|서블릿 컨테이너의 주 버전을 반환합니다.|
|서버 자원 정보||
|getMimeType(filename)|주어진 파일 이름의 MIME 유형을 반환합니다.|
|getResource(path)|주어진 경로에 해당하는 자원을 반환합니다.|
|Logging||
|log(message)|로그에 메시지를 기록합니다.|
|Attribute 관리||
|getAttribute(name)|주어진 이름에 해당하는 속성 값을 반환합니다.|
|setAttribute(name, value)|주어진 이름으로 속성 값을 설정합니다.|
|Parameter||
|getInitParameter(name)|파라미터 중에서 name과 연관된 value를 반환합니다.|
|getInitParameterNames()|파라미터의 name들을 묶어서 Enumeration으로 반환합니다.|


# HttpSession 객체
- 대부분의 세션 관련 작업은 container가 처리
- Servlet은 request로부터 HttpSession 객체를 제공받음

|메서드|설명|
|---|---|
|`boolean isNew()`|이번 요청으로 새로운 세션이 생성되었는지 여부를 반환합니다.|
|`String getId()`|현재 세션의 ID를 반환합니다.|
|`void invalidate()`|현재 세션을 종료합니다.|
|`long getCreationTime()`|세션이 생성된 시간을 제공합니다.|
|`long getLastAccessedTime()`|마지막으로 세션과 관련된 클라이언트가 요청을 보낸 시간을 제공합니다.|
|`void setMaxInactiveInterval(int)`|초 단위로 최대 유휴 기간을 설정합니다.|
|`int getMaxInactiveInterval()`|초 단위로 설정된 최대 유휴 기간을 반환합니다.|
|`void setAttribute(String, Object)`|지정된 이름으로 속성 값을 설정합니다.|
|`Object getAttribute(String)`|지정된 이름의 속성 값을 반환합니다.|


# 객체별 lifecycle
|객체|생성|소멸|
|---|---|---|
|ServletContext|웹 애플리케이션 시작|웹 애플리케이션 종료|
|HttpSession|최초 접속시, 세션을 사용하는 컨텐츠|타임아웃, invalidate() 호출|
|HttpServletRequest|해당 서블릿 요청시|요청 완료|

---
# 속성(Atrribute)
- 특정 정보와 행위를 가지고 있는 객체
- ServletContenxt, HttpServletRequest, HttpSession 객체에 binding
- Java Object 형태의 객체
- 내부적으로 (name, value) 형식으로 저장
- 속성을 binding한 객체의 scope 내에서 정보 공유에 사용

|Methods|Description|
|---|---|
|void setAttribute(String name, Object value)|속성 저장|
|Object getAttribute(String name)|속성 추출|
|void removeAttribute(String name)|속성 제거|
|Enumeration getAttributeNames()|속성 name 리스트 획득|

### RequestDispatcher
- 한 애플리케이션 내의 다른 component에게 data를 넘겨주기 위해 사용
![[Pasted image 20240116043406.png|400]]
![[Pasted image 20240116043416.png|450]]



