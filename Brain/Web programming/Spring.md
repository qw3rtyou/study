# 스프링 프레임워크 모듈
- 이러한 모듈을 사용하려면 프로젝트에 모듈에 대한 ‘의존 설정’을 해야 함

![[Pasted image 20240116061100.png]]

![[Pasted image 20240116061114.png]]


- 경량 컨테이너로 자바 객체의 라이프 사이클 직접 관리
- 제어 반전(IoC : Inversion of Control) : 스프링->사용자 코드 호출
- 의존성 주입(DI : Dependency Injection)
- 관점 지향 프로그래밍(AOP : Aspect-Oriented Programming)
- iBatis, Hibernate등 DB처리 모듈과 쉽게 연결
- 확장성이 높음


---
# DI
- 의존하고 있는 인스턴스를 외부에서 주입받는 것
- 스프링 컨테이너 생성 및 bean 객체 획득

![[Pasted image 20240116062400.png|400]]


# DI 설정
- constructor 방식
![[Pasted image 20240116062542.png|400]]


- setter method 방식
![[Pasted image 20240116062555.png|400]]



# 컴포넌트 스캔
- 스프링이 직접 클래스를 검색해서 bean으로 등록해주는 기능
- 설정 클래스에 bean으로 등록하지 않아도 원하는 클래스 등록 가능
- 기본 스캔 대상 - @Component,@Controller,@Service,@Repository,@Aspect,@Configuration

- 스캔 설정
![[Pasted image 20240116063215.png|300]]



---
# IoC
- 프로그램의 제어를 사용자 대신 컨테이너나 프레임워크가 하는 것


---
# Aspect Oriented Programming (AOP)
- 핵심 기능의 실행은 다른 객체에 위임하고 부가적인 기능 추가 제공
- 공통 기능과 핵심 기능의 구현을 분리
- Proxy - 여러 객체에 공통으로 적용할 수 있는 공통 기능 구현
- 런타임에 프록시를 이용해 공통 기능 삽입


---
# 컴파일과 빌드의 차이점
### 컴파일
- 코딩한 코드 파일을 컴파일러(compiler)가 바이트코드(bytecode) 파일로 변환하는 과정을 뜻함
- 바이트코드 파일은 JVM에 의해 기계어로 바뀌어 컴퓨터에서 실행됨

### 빌드
- 컴파일보다 넓은 의미로 라이브러리 다운로드 및 연결, 컴파일, 링크, 패키징 등 애플리케이션 제작에 필요한 전반적인 과정을 뜻함

---
# Maven
- 설정파일 - pom.xml
- 필요한 라이브러리를 연결해주고 빌드 설정을 담당함


### spring-context 모듈 설정
- 모듈 하나를 artifact(아티팩트)라는 단위로 관리함

```xml
<dependency>
	<groupId>org.springframework</groupId>
	<artifactId>spring-context</artifactId>
	<version>${org.springframework-version}</version>
	<exclusions>
		<!-- Exclude Commons Logging in favor of SLF4j -->
		<exclusion>
			<groupId>commons-logging</groupId>
			<artifactId>commons-logging</artifactId>
		 </exclusion>
	</exclusions>
</dependency>
```

### 빌드 설정
```xml
<build>
	<plugins>
		<plugin>
			<groupId>org.apache.maven.plugins</groupId>
			<artifactId>maven-compiler-plugin</artifactId>
			<version>2.5.1</version>
			<configuration>
				<source>11</source>
				<target>11</target>
				<compilerArgument>-Xlint:all</compilerArgument>
				<showWarnings>true</showWarnings>
				<showDeprecation>true</showDeprecation>
			</configuration>
		</plugin>
	</plugins>
</build>
```


---
# IoC container
- applicationContext.xml


---
# InitSampleData 빈
- 객체 생성과 조립(Bean의 생성과 초기화)
- `<bean id="initSampleData" class="클래스경로"/>`

- `<bean>`은 생성자를 호출하고, `<property>`의 `<array>` 값은 InitSampleData의 `setsNums(String[ ] sNums)` 메서드에 전달됨
```xml
<bean id="initSampleData"
	class="ch04_pjt_01.ems.utils.InitSampleData">
	<property name="sNums">
		<array>
			<value>hbs001</value>
			<value>hbs002</value>
			<value>hbs003</value>
			<value>hbs004</value>
			<value>hbs005</value>
		</array>
	</property>
</bean>
```

- 자바에서는 개발자가 어떠한 생성자도 명시하지 않으면 컴파일러가 컴파일 단계에서 자동으로 디폴트 생성자(default constructor)를 생성


---
# 스프링 빈 범위
- IoC 컨테이너에 생성된 빈을 getBean()으로 호출하면 항상 동일한 객체가 반환됨
- 스프링이 기본적으로 객체 범위를 싱글턴으로 관리하기 때문


# 프로토타입(prototype)
- 싱글턴 범위의 반대 개념
- 프로토타입의 경우 개발자의 설정이 필요함
- 스프링 설정 파일에서 빈을 정의할 때 scope 속성을 명시해주면 됨

```xml
<bean id="dependencyBean" class="ch04_pjt_02.scope.DependencyBean" scope="prototype">
	<constructor-arg ref="injectionBean"/>
</bean>
```

---
# 의존 자동 주입
- 스프링이 자동으로 의존하는 bean 객체를 주입해주는 기능
- 결론적으로 주로 @Autowired 나 @Resource 사용

### 방법
1. context파일에 아래 두 줄 추가

![[Pasted image 20240116122506.png|400]]


2. `<context:annotation-config/>`
3. 기존에 사용하던 `<constructor-arg>` 제거

- `<context:annotation-config/>`에 의해서 `<constructor-arg ref="contactDao" />` 없이도 생성자에 ContactDao가 자동으로 주입 됨

### 생성자가 여러 개인 경우
- 동일한 생성자가 여러 개 있을 경우 기본적으로 default 생성자를 사용하게 됨
- 이를 위해 ContactDao를 필요로 하는 곳에 @Autowired 애너테이션을 명시하면 됨
![[Pasted image 20240116123024.png|400]]
- @Autowired 애너테이션을 사용하면 객체가 생성될 때 데이터 타입을 검색해서 알맞은 객체를 주입함 
- 즉, ContactRegisterService 객체가 생성될 때 필요한 ContactDao 객체를 데이터 타입으로 검색해서 알맞은 객체를 자동으로 주입함 

- @Autowired를 메서드에 적용할 수도 있음
- üsetter 메서드를 이용할 때도 기본적으로 객체가 생성되고 setter 메서드를 이용해서 의존 객체가 주입됨

![[Pasted image 20240116123256.png|300]]


# @Resource와 @Autowired의 차이점
![[Pasted image 20240116123403.png|450]]


### 다수의 빈 객체 중 의존 대상 객체 선택 방법
- 동일한 타입의 의존 객체가 2개 이상인 경우에는 어떤 의존 객체를 자동 주입해야 하는지 판단할 수가 없기 때문

- 해결방법 - `@Qualifier` 추가
![[Pasted image 20240116123626.png|400]]


# required 속성
- 빈을 생성하지 않고 @Autowired를 사용한 경우 오류를 회피할 수 있음
- @Aurowired에 required 속성을 false로 지정하면 의존 객체 자동 주입이 필수가 아닌 필요에 따라서만 주입됨
- 의존 대상 객체를 못 찾아서 발생하는 에러를 피할 수 있음

![[Pasted image 20240116123931.png|200]]


---
# XML 파일의 기능을 Java 파일로 변경하기
### @Configuration
- XML을 이용하지 않고 애너테이션을 이용한 스프링 설정 파일을 만들기 위해 사용하는 애너테이션

![[Pasted image 20240116124218.png|400]]


### @Bean
- 빈 객체를 생성하기 위한 애너테이션

![[Pasted image 20240116124439.png|250]]

- 메서드 이름은 빈 객체의 id이고 반환되는 데이터 타입은 빈 객체의 타입명

![[Pasted image 20240116124729.png|300]]

- 객체가 생성되는 시점에 인자로 의존 객체 주입

![[Pasted image 20240116125120.png|400]]

- setter 메서드를 이용한 주입

![[Pasted image 20240116125438.png|400]]

![[Pasted image 20240116125549.png|400]]



# 스프링 컨테이너 초기화
- 설정파일이 기존 XML 파일(applicationContext.xml)에서 애너테이션을 이용한 Java 파일(MemberConfig.java)로 변경됨

![[Pasted image 20240116130022.png]]


- 스프링 설정 파일을 분리했다면, 컨테이너를 초기화하는 코드 수정하기

![[Pasted image 20240116132019.png]]



# 외부 스프링 설정파일 사용
- `<import>` 태그를 이용한 외부 스프링 설정 파일 사용

![[Pasted image 20240116132313.png]]

- `@Import` - 스프링 설정 파일을 제작할 때 다른 Java 파일을 임포트하기 위한 애너테이션

![[Pasted image 20240116132327.png]]

![[Pasted image 20240116132356.png]]

- 설정 클래스 파일 경로 수정
![[Pasted image 20240116132412.png]]



---
# XML 설정파일들

### pom.xml
- 프로젝트 이름, 자바 버전, 스프링 버전, 스프링 mvc프레임워크와 관련 라이브러리, servlet 관련 라이브러리 등등
- 빌드 설정


### web.xml
- 웹 서비스의 전반적인 설정을 함
- DispatcherServlet 객체를 서블릿으로 등록해주는 코드도 web.xml에 있음
- 스프링 설정 파일(servlet-context.xml)을 설정함
![[Pasted image 20240116132830.png|400]]


### servlet-context.xml
- 스프링 설정의 역할을 담당함
- 스프링 빈 객체를 생성하고 관리하는 과정을 살펴



---
# `<annotation-driven>`
- @Controller 애너테이션이 명시된 클래스를 컨트롤러 객체로 이용할 수 있음


---
# DAO



# Service


# Controller
- 클라이언트의 요청을 실제로 처리하는 객체
- 컨트롤러 객체는 클라이언트의 요청을 받아서 사용자의 요청에 부합하는 메서드를 실행함
- 해당 메서드는 Service와 DAO 등을 이용해서 사용자의 요청에 대한 작업을 진행함
- 메서드의 작업이 완료되면 뷰 정보를 반환하고, 반환된 정보를 이용해서 JSP 파일이 실행됨

![[Pasted image 20240116133921.png|450]]



# View
- jsp반환



---
# 주요 객체들 역할
![[Pasted image 20240116133337.png]]


---
# 클라이언트 요청을 서버에서 처리하기


### @RequestParam
- 사용자가 입력한 정보를 컨트롤러에서 하나씩 받을 수 있음
- 데이터 타입은 스프링이 자동으로 형 변환을 함
![[Pasted image 20240116134807.png]]


### VO 객체
- Value Object
- 스프링에서는 데이터 이름을 이용해서 클라이언트에서 전송된 데이터를 VO 객체의 멤버 필드에 자동으로 할당함
- 멤버 필드에 해당하는 setter 메서드를 반드시 명시해야 함
- 스프링은 MemberVo에서 사용자가 입력한 데이터의 이름과 동일한 멤버 필드를 찾고, 이에 해당하는 setter 메서드를 이용해서 멤버 필드에 데이터를 할당함
- DTO와 VO는 엄밀히 말하자면 다른 개념이지 이를 구분하지 않고 사용하는 경우도 많음

![[Pasted image 20240116134948.png|450]]





---

# Servlet Filter
- 서블릿으로 요청이 가기 전에 가로채기
- 서블릿 작업이 완료된 후 응답에 추가 작업하기
- 요청 포맷팅 수정, 보안 관련 검사, 로깅, 압축 등
- Filter 인터페이스 구현
- 생명주기는 container에 의해 관리
- 주로 UTF8 지원을 위해 사용됨

```xml
<filter> 
	<filter-name>encodingFilter</filter-name> 
	<filter-class>org.springframework.web.filter.CharacterEncodingFilter</filter-class> 
	<init-param> 
	   <param-name>encoding</param-name> 
	   <param-value>UTF-8</param-value> 
	</init-param> 
	<init-param> 
	   <param-name>forceEncoding</param-name> 
	   <param-value>true</param-value> 
	</init-param> 
 </filter> 
 <filter-mapping> 
	<filter-name>encodingFilter</filter-name> 
	<url-pattern>/*</url-pattern> 
 </filter-mapping>
```


---
# Model
- Controller에서 View에 필요한 데이터 전달을 위해 Model 사용
- 클래스컨트롤러는 Model을 이용해서 뷰에 데이터를 전달할 수 있음


# ModelAndView 클래스
- 이름에서도 알 수 있듯이 뷰와 데이터를 동시에 설정해서 전달
- Model과 ModelAndView 둘 중에 어떤 것을 사용해도 상관없음


---
# JDBC Programming
- DB에 연결하는 각 jsp에서 각자 작업을 하게 되면, 코드가 중복되고, 수정/보수가 어려워짐


# JdbcTemplate
- JdbcTemplate을 이용하면 ‘SQL 쿼리 작성 및 실행’ 작업에 집중할 수 있는 장점이 있음
- 스프링에서는 JdbcTemplate 클래스를 제공함


# DAO Pattern
- Use a Data Access Object
- To abstract and encapsulate all access to the data source
- The DAO manages the connection with data source to obtain/store data

![[Pasted image 20240116065139.png]]


___
# 롬복
- 자동으로 getter, setter 메소드를 만듬

---
# 어노테이션 모음

### `@Autowired`
- autowired를 사용하지 않으면 스프링 입장에서 의존객체를 가져오는게 아닌 그냥 디폴트 생성자를 사용하게 됨
- 이를 막기 위해 의도적으로 스프링이 의존객체를 찾아와서 주입하게 만드는 역할을 함
- 즉, 자동 빈 주입
- 어노테이션 사용하기 위해 `<context:annotation-config/>` 추가 해야함


### `@Resource`
- 스프링에서 제공하는 어노테이션이 아닌 자바에서 제공하는 어노테이션임
- autowired와 비슷함
- auotwired 는 타입을 먼저, resource는 이름을 우선 확인함
![[Pasted image 20240111142833.png]]

- 사용하려면 Javax AnnotationAPI 페이지에서 1.3.2를 클릭하고, 메이븐 코드를 복사해야 함


### `@Qualifier`
- 자동 주입 시 문제점 해결
- 동일한 타입의 의존 객체가 2개 이상인 경우에는 어떤 의존 객체를 자동 주입해야 하는지 판단할 수가 없음

![[Pasted image 20240111143305.png]]

- @Autowired와 @Qualifier를 이용한 특정 의존 객체 지정
![[Pasted image 20240111143602.png]]

- required 속성
- @Aurowired에 required 속성을 false로 지정하면 의존 객체 자동 주입이 필수가 아닌 필요에 따라서만 주입됨
- 의존 대상 객체를 못 찾아서 발생하는 에러를 피할 수 있음
![[Pasted image 20240111143705.png]]


### `@Inject`
- autowired 와 비슷하지만 autowired가 요즘 많이 사용
- 거의 비슷 몰라도 되는 듯

### `@ComponentScan`, `@commponent`
![[Pasted image 20240116063215.png|300]]



### `@Bean`
![[Pasted image 20240116063659.png|400]]


### `@RequestMapping, @GetMapping, PostMapping`
- Controller에서 특정 요청 URL 매핑


### `@Configuration
- XML을 이용하지 않고 애너테이션을 이용한 스프링 설정 파일을 만들기 위해 사용하는 애너테이션


### `@Bean`
- 빈 객체를 생성하기 위한 애너테이션


---