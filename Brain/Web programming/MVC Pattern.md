
# MVC Pattern
- Model-View-Controller patter
- 객체간의 coupling 레벨을 줄임으로써 보다 유연한 data처리 가능
- Web application에서 많이 사용되는 중요 패턴

![[Pasted image 20240116052058.png]]


---
# Three Logical Layers
### Model (Business process layer)
- Backend단에서의 비즈니스 로직 담당
- data와 그에 대한 행동을 모델링
- 실제 처리해야 하는 작업을 수행(query 수행)
- Presentation layer와 무관하게 data를 encapsulate

### View (Presentation layer)
- 비즈니스 로직(Model)을 통해 얻어진 결과를 출력
- 사용자 타입과 환경에 맞게 다양한 정보를 출력
- 정보 자체가 어디로부터 왔는지, 어떻게 생성되었는지는 상관하지 않음

### Controller (Control layer)
- 사용자와 backend의 비즈니스 로직을 연결해 주는 역할
- 여러 presentation중 어느 것을 제공할지 결정해 주는 역할
- 사용자의 요청을 받은 후, 요청을 어떻게 처리하고 어떤 결과를 얻어서 표현해야 하는지를 결정



---
# MVC Pattern 구현
- Three Logical Layers 구현
- 데이터 표현에 beans 사용
- 요청 핸들링시 servlet 사용
- beans 채우기
- request, session, or servlet context에 bean 저장
- JSP 페이지로 요청 포워딩
- beans에서 데이터 추출

