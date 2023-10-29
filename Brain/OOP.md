[[OOP - Python]]
# SOLID
-  단일 책임 원칙 (Single Responsibility Principle, SRP)
클래스는 단 하나의 책임을 가져야 하며, 
그 책임을 변경하는 이유는 오직 하나이어야 함
클래스가 여러 책임을 갖게 되면 유지 보수가 어려워지고 오류가 발생하기 쉬워지기 때문
가독성도 좋아짐
어디에서 이것을 책임지는 지가 분명해짐
소프트웨어의 유지 보수가 쉬워짐
    
- 개방-폐쇄 원칙 (Open/Closed Principle, OCP)
소프트웨어 엔티티(클래스, 모듈, 함수 등)는 확장에 대해 열려 있어야 하지만 변경에 대해서는 닫혀 있어야 함
즉, 새로운 기능을 추가할 때 기존 코드를 변경하지 말아야 한다는 원칙

변경에 닫혀있기 위해서는 
클래스 외부에 보여질 것을 최소화
접근 권한을 최소로 열어준다는 원칙
외부에 필요한 지점에서 메소드를 통해 접근 방법을 제공 
내부적으로 변경이 필요할 때 다른 클래스에 미칠 영향을 최소화할 수 있다
    
- 리스코프 치환 원칙 (Liskov Substitution Principle, LSP)
서브 타입은 언제나 기본(슈퍼) 타입으로 대체할 수 있어야 함
여기서 서브 타입은 상속 받는 클래스 혹은 비슷한 위치의 타입
이는 상속 관계에서 하위 클래스가 상위 클래스를 대체할 때 기대 동작을 변경하지 않아야 함을 의미
다형성과 확장성을 극대화하려면 하위 클래스를 사용하는 것보다는 
상위의 클래스(인터페이스)를 사용하여 코딩하는 것이 좋음
일반적으로 선언은 기반 클래스로, 생성은 구체 클래스로 대입하는 방법을 사용
    
- 인터페이스 분리 원칙 (Interface Segregation Principle, ISP)
클라이언트는 자신이 사용하지 않는 메서드에 의존하도록 강요받지 않아야 함
즉, 한 인터페이스가 너무 많은 메서드를 포함하지 않아야 함
인터페이스는 밀접하게 관련된 메소드들만 모아 작게
 
- 의존성 역전 원칙 (Dependency Inversion Principle, DIP)
의존성이란 하나의 구성 요소가 다른 구성 요소에 의존하여 그 구성 요소가 제대로 동작하기 위해 필요한 것을 나타냄
A가 B에 의존한다면 A가 B의 함수를 호출하는 것, B가 바뀌면 A가 영향을 받음
```java
public class Engine {
    public void start() {
        System.out.println("Engine is starting.");
    }
}

public class Car {
    private Engine engine; // Car 클래스는 Engine 클래스에 의존

    public Car() {
        engine = new Engine(); // Car 클래스는 엔진을 직접 생성하여 의존
    }

    public void startCar() {
        engine.start(); // Car는 엔진에 의존하여 엔진을 시작함
    }
}
```

고수준 모듈은 저수준 모듈에 의존해서는 안 되며, 둘 모두 추상화에 의존해야 함
이는 추상화를 통해 상위 수준 모듈과 하위 수준 모듈 사이의 결합도를 낮추는 원칙임
추상화된 수준은 구체적인 구현의 세부적인 사항에 의존하지 말아야 함

위의 예시에서 `Car`클래스가 `Engine`클래스에 대한 의존성을 낮추고 느슨하게 결합하기 위해선 
**의존성 주입(Dependency Injection)** 을 사용할 수 있음

```java
public class Car {
    private Engine engine; // Car 클래스는 Engine 클래스에 의존

    public Car(Engine engine) {
        this.engine = engine; // 엔진을 외부로부터 주입받음 (의존성 주입)
    }

    public void startCar() {
        engine.start(); // Car는 주입받은 엔진을 사용하여 엔진을 시작함
    }
}
```

느슨한 결합은 한 모듈이 다른 모듈에 대해 가능한 한 적은 정보를 알도록 하는 것을 의미
예시에서, 의존성 주입을 사용하면 `Car` 클래스가 `Engine` 객체를 직접 생성하지 않고, 외부로부터 주입받음
이렇게 하면 `Car` 클래스는 `Engine` 객체를 어떻게 생성하는지 알 필요가 없으며, `Car` 클래스와 `Engine` 클래스 간의 결합이 느슨해짐
결과적으로, `Car` 클래스가 `Engine` 클래스에 대한 구체적인 세부 정보에 의존하지 않으므로 
`Engine` 클래스를 변경하더라도 `Car` 클래스는 변경될 필요가 없음

이때, `Car` 클래스는 어떤 종류의 엔진을 사용할지에 대한 제약이 없어지므로, 재사용성 및 테스트에 용이해짐

또, 여기서 언급한 `역전`이라는 표현은 
기존에는 고수준 모듈이 저수준 모듈에 직접 의존하고 있었다면,
고수준 모듈과 저수준 모듈 모두 추상화에 의존하도록 변경된 걸 말함

![[Pasted image 20231022223722.png]]

```java
//고수준 모듈
public class DataSender {
    private CommunicationModule communicationModule;

    public DataSender(CommunicationModule communicationModule) {
        this.communicationModule = communicationModule;
    }

    public void sendData(String data, Callback callback) {
        communicationModule.send(data);
        callback.onSuccess();
    }
}

//저수준 모듈
public interface CommunicationModule {
    void send(String data);
}

public class HttpCommunicationModule implements CommunicationModule {
    @Override
    public void send(String data) {
        // 간단한 HTTP 통신을 시뮬레이션하고, 통신이 성공했다고 가정 
        System.out.println("HTTP 통신 중..."); 
        
        // HTTP 통신이 완료되면 콜백 함수 호출 
        callback.onSuccess();
    }
}

//콜백 인터페이스
public interface Callback {
    void onSuccess();
}

//메인
public class Main {
    public static void main(String[] args) {
        // HttpCommunicationModule를 사용하는 DataSender 인스턴스 생성
        CommunicationModule communicationModule = new HttpCommunicationModule();
        DataSender dataSender = new DataSender(communicationModule);

        // 콜백 함수 정의
        Callback callback = () -> {
            System.out.println("데이터 전송 완료!");
        };

        // 데이터 전송 및 콜백 함수 호출
        dataSender.sendData("Sample Data", callback);
    }
}

```


![[Pasted image 20231022223735.png]]

```java
import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SwingExample {
    public static void main(String[] args) {
        // 고수준 컴포넌트: 버튼
        JButton button = new JButton("Click Me");

        // 버튼에 이벤트 핸들러(저수준 모듈) 등록
        button.addActionListener(new MyActionListener());

        // 프레임 설정 및 컴포넌트 추가
        JFrame frame = new JFrame("Swing Example");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add(button);
        frame.pack();
        frame.setVisible(true);
    }
}

// 이벤트 핸들러를 구현한 클래스
class MyActionListener implements ActionListener {
    @Override
    public void actionPerformed(ActionEvent e) {
        System.out.println("Button Clicked!");
    }
}
```

# BOTTOM-UP & TOP-DOWN
- Top-Down
전체 시스템 또는 프로젝트의 고수준 설계와 구조를 먼저 정의하고, 
그 다음 이를 하위 수준의 모듈로 분해
시스템의 일관성과 구조를 중요시하며,
초기 설계 단계에서 전체 시스템 아키텍처를 확립

- Bottom-Up
은 구성 요소나 모듈부터 출발하여 전체 시스템을 구성하는 방식
초기 결과물을 빠르게 얻을 수 있으며, 
세부 모듈의 동작을 확인하면서 시스템을 점진적으로 확장

# KISS
Keep It Simple and Short
클래스나 함수 작성시 필요한 기능만 포함


# DRY
Don’t Repeat Yourself
중복 배제 원칙
어딘가에 있는 기능을 또 만들면 안됨
함수는 여러 가지 기능을 한꺼번에 하기보다는
한 가지 기능만 가져서 불러다 쓰기 좋게 만들어야 함
매개변수를 통해 상황에 맞게 동작할 수 있게 작성하여 재사용 성을 높여야 함
SRP 원칙과도 통함


# Encapsulation
각 클래스의 필드는 클래스 내에서만 접근할 수 있음
밖에서는 보이지 않는 private를 원칙으로 함


