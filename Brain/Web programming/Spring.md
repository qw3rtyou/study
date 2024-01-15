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
- @Autowired 나 @Resource 사용



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


---
# JDBC Programming
- DB에 연결하는 각 jsp에서 각자 작업을 하게 되면, 코드가 중복되고, 수정/보수가 어려워짐


# DAO Pattern
- Use a Data Access Object
- To abstract and encapsulate all access to the data source
- The DAO manages the connection with data source to obtain/store data

![[Pasted image 20240116065139.png]]


---
# 어노테이션 모음

### `@Autowired`
- autowired를 사용하지 않으면 스프링 입장에서 의존객체를 가져오는게 아닌 그냥 디폴트 생성자를 사용하게 됨
- 이를 막기 위해 의도적으로 스프링이 의존객체를 찾아와서 주입하게 만드는 역할을 함
- 즉, 자동 빈 주입
- 어노테이션 사용하기 위해 <context:annotation-config/> 추가 해야함


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


---