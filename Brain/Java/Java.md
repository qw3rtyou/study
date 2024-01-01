[[Java - OOP]]
[[Swing]]

# 변수 참조 순서
1. 블록변수
2. 지역변수
3. 매개변수
4. 인스턴스 변수
5. 전역변수

# 인스턴스
일반적으로 객체와 비슷한 의미로 사용
클래스의 인스턴스 == 객체
관계의 느낌이 강함


# 기본타입 vs 객체타입
객체는 힙(heap) 메모리에 할당, 변수는 이 객체를 가리키는 참조(reference)를 가지게 됨
기본 타입은 단순한 데이터 값을 직접 저장하며, 스택(stack) 메모리에 저장
기본 타입 변수는 해당 값을 직접 저장하며, 변수 자체가 값을 나타냄
참조(reference)를 사용하지 않음

아래 8개 제외 전부 클래스의 인스턴스들임
1. **정수 타입 (Integer Types)**:
- `byte`: 8비트 정수. 범위: -128 ~ 127
- `short`: 16비트 정수. 범위: -32,768 ~ 32,767
- `int`: 32비트 정수. 범위: -2^31 ~ 2^31-1
- `long`: 64비트 정수. 범위: -2^63 ~ 2^63-1
2. **부동소수점 타입 (Floating-Point Types)**:
- `float`: 32비트 부동 소수점. 단정밀도 (대략 7자리 유효 숫자)
- `double`: 64비트 부동 소수점. 배정밀도 (대략 15자리 유효 숫자)
3. **문자 타입 (Character Type)**:
- `char`: 16비트 유니코드 문자를 표현 (범위: '\u0000' ~ '\uffff')
4. **불리언 타입 (Boolean Type)**:
- `boolean`: `true` 또는 `false` 값을 가짐


# 별칭
별칭이란 다른 이름의 변수가 같은 객체를 가리키는 걸 말함
어느 이름으로 접근하든 같고 참조변수를 매개변수로 전달할 때도 별칭이 됨
기본타입은 각자의 메모리를 가지므로 별칭이 생기지 않음
![[Pasted image 20231021103731.png]]


# String 사용 시 주의 할 점
String은 객체 타입이기 때문에 참조 변수를 지정함
그리고 일반적으로 `==` 는 해당 심볼에 위치에 있는 값을 비교하고
해당 심볼에 위치에는 문자열이 아닌 문자열의 주소가 있음
그러나 서로 **따로 선언하더라도 내용이 같은 문자열이면 같은 주소를 가리킴**(재사용성 극대)
자바에서는 문자열이 같은 문자열을 여러 번 선언하게 되면 메모리 낭비가 심한 구조여서 그럼
이를 방지하기 위해선 **new로 새로운 위치를 가리키게 만들어야 함**

![[Pasted image 20231021102943.png]]
![[Pasted image 20231021103038.png]]

**스트링 객체는 불변임**
값을 수정하려면 새로운 객체를 생성해야 함
모든 스트링 객체의 값을 바꾸는 메소드는 새로운 객체를 만들어서 반환
![[Pasted image 20231021104342.png]]

지속적으로 문자열을 수정해야 한다면 
새로운 객체를 만드는 행위 이므로 비효율적임
이 때 사용하는 방법이 `StringBuilder`, `StringBuffer`

문자열 비교할 땐, `name.equals(input)` 또는 `name.contentEquals(input)` 이런 함수 사용 

# 상속
자바는 다중 상속이 안됨


# 다형성
메소드 오버라이딩으로 구현 
참조의 다형성
가상함수 호출의 다형성
가상함수는 호출하는 객체에 따라 다를 메소드 참조
동적바인딩 때문

# 인터페이스
메소드 정의만 가지고 표준을 제공하는 역할
클래스처럼 참조 다형성과 가상함수 다형성을 제공할 수 있음
인터페이스를 이용하면 전혀 다른 클래스도 같은 타입으로 취급될 수 있음
다중 상속의 역할을 함

인터페이스는 기본적으로 public 으로만 선언 가능
따라서 구현부도 public 으로 선언해야 함
만약 private 로 하고 싶다면 다음과 같이 사용할 순 있음
```java
public interface MyInterface {
    default void publicMethod() {
        // 다른 메서드에서 호출 가능한 public 메서드
        privateMethod();
    }

    private void privateMethod() {
        // 인터페이스 내에서만 접근 가능한 private 메서드
        System.out.println("Private method in the interface");
    }
}

public class MyClass implements MyInterface {
    public static void main(String[] args) {
        MyClass myClass = new MyClass();
        myClass.publicMethod(); // publicMethod 내에서 privateMethod 호출
    }
}
```


# 추상 클래스(Abstract Class)
추상 클래스는 일반 클래스와 마찬가지로 필드와 메서드를 포함할 수 있지만, 하나 이상의 추상 메서드를 포함할 수 있음
추상 메서드는 메서드의 선언만 있고 본문(구현)이 없는 메서드
추상 클래스는 객체를 직접 생성할 수 없으며, 하위 클래스에서 추상 메서드를 반드시 구현해야 함

```java
abstract class Shape {
    protected int x, y;

    public Shape(int x, int y) {
        this.x = x;
        this.y = y;
    }

    // 추상 메서드
    public abstract void draw();
}

class Circle extends Shape {
    private int radius;

    public Circle(int x, int y, int radius) {
        super(x, y);
        this.radius = radius;
    }

    // 추상 메서드의 구현
    @Override
    public void draw() {
        System.out.println("원을 그립니다.");
    }
}

class Rectangle extends Shape {
    private int width, height;

    public Rectangle(int x, int y, int width, int height) {
        super(x, y);
        this.width = width;
        this.height = height;
    }

    // 추상 메서드의 구현
    @Override
    public void draw() {
        System.out.println("사각형을 그립니다.");
    }
}

public class AbstractClassExample {
    public static void main(String[] args) {
        Circle circle = new Circle(5, 5, 3);
        Rectangle rectangle = new Rectangle(2, 2, 4, 6);

        circle.draw();
        rectangle.draw();
    }
}
```



# 디폴트 메서드
인터페이스(Interface) 내에서 메서드의 기본 구현을 제공하는 기능을 의미
디폴트 메서드는 기존의 인터페이스를 확장하고, 
이미 해당 인터페이스를 구현한 클래스들에게 새로운 메서드를 제공하는 방법으로 유용하게 사용될 수 있음

```java
interface Vehicle {
    default void start() {
        System.out.println("Vehicle started.");
    }

    void stop();
}

interface Engine {
    default void start() {
        System.out.println("Engine started.");
    }

    void stop();
}

class Car implements Vehicle, Engine {
    @Override
    public void stop() {
        System.out.println("Car stopped.");
    }

    // 충돌하는 디폴트 메서드를 재정의
    @Override
    public void start() {
        Vehicle.super.start(); // Vehicle 인터페이스의 start 메서드 호출
        Engine.super.start();   // Engine 인터페이스의 start 메서드 호출
    }
}

public class DefaultMethodExample {
    public static void main(String[] args) {
        Car car = new Car();
        car.start();
        car.stop();
    }
}
```


# 클래스 선언 방식
- 별도 클래스
![[Pasted image 20231022205207.png]]


- 중첩 클래스
![[Pasted image 20231022205228.png]]


- 무명 클래스
한 번만 사용하고 버림
심볼이 없음
인터페이스가 생성자를 가지면 무명클래스 사용 불가
무명 클래스를 여러 번 재사용해야 할 때 사용 불가
![[Pasted image 20231022205239.png]]


- 로컬 클래스



# 람다식
함수를 대신하는 수식
매개변수(입력) -> {실행할 코드} 형태의 수식
매개변수가 1개 이하이고 실행할 코드가 한 줄로 간단할 때
함수에 이름을 붙이고 호출하는 대신 함수를 전달만 할 때 사용
람다식을 이용해 인테페이스도 구현할 수 있음

```java
// 인터페이스 정의
interface Calculator {
    int calculate(int a, int b);
}

public class LambdaExample {
    public static void main(String[] args) {
        // 람다식을 사용하여 두 수를 더하는 함수 구현
        Calculator addition = (a, b) -> a + b;
        
        int result = addition.calculate(5, 3);
        System.out.println("덧셈 결과: " + result);
    }
}
```

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class LambdaExample {
    public static void main(String[] args) {
        List<String> names = new ArrayList<>();
        names.add("Alice");
        names.add("Bob");
        names.add("Charlie");

        // 람다식을 사용하여 문자열을 길이에 따라 정렬
        Collections.sort(names, (a, b) -> a.length() - b.length());

        System.out.println("정렬된 이름: " + names);
    }
}
```

다음과 같은 경우 람다식 사용 불가
- 추상 메서드가 두 개 이상인 인터페이스
- 람다식에서 변수 사용 - 해당 변수는 상수처럼 사용하거나 final이어야 함
- 객체를 생성하는 작업 불가능

특징
- 매개변수의 타입 생략(컴파일러가 컨텍스트를 통해 타입을 유추)
- 매개변수 개수를 맞춰야 함
- 람다식의 본문이 단일 표현식이라면 중괄호 생략 가능 + return 생략해야 함
- 단일 표현식이 아니라면 중괄호를 써야하지만 복수의 문장을 포함할 수 있고, return 키워드를 사용해 값을 반환할 수 있음
- 함수형 인터페이스에서 사용됨 


# 메소드 참조
메서드를 다른 메서드의 매개변수로 전달하거나 반환할 때 람다식 대신 사용할 수 있음

```java
import java.util.ArrayList;
import java.util.List;

class Person {
    private String name;

    public Person(String name) {
        this.name = name;
    }

    public void sayHello() {
        System.out.println("안녕, 나는 " + name + "이야!");
    }
}

public class MethodReferenceExample {
    public static void main(String[] args) {
        List<Person> people = new ArrayList<>();
        people.add(new Person("Alice"));
        people.add(new Person("Bob"));
        people.add(new Person("Charlie"));

        // 람다식을 사용하여 Person 객체의 sayHello 메서드를 호출
        people.forEach(person -> person.sayHello());

        // 메서드 참조를 사용하여 Person 객체의 sayHello 메서드를 호출
        people.forEach(Person::sayHello);
    }
}
```


# 함수형 인터페이스
하나의 추상 메서드(abstract method)를 정의하는 인터페이스를 가리킴
람다식(lambdas) 또는 메서드 참조(method references)와 같은 함수형 프로그래밍 기법을 지원하는데 사용

- 반드시 하나의 추상 메서드를 가져야 함
이 메서드가 인터페이스의 사실상 기능을 담당함
다른 메서드는 default 메서드나 정적 메서드로만 정의할 수 있음
- 람다식 사용 가능
- 메서드 참조도 가능
- @FunctionalInterface 어노테이션을 사용해주는 게 일반

```java
@FunctionalInterface 
public interface Factory { 
	public void create(); 
}
```


# 훅메소드, 후킹
라이브러리 모듈은 함수가 있다 치고 해당 시그너처의 함수를 호출 (훅메소드) 
사용자는 그 함수를 제공하고 그걸 호출해 달라고 등록 (후킹)

```java
import java.util.function.Consumer;

// 라이브러리 모듈
public class LibraryModule {
    private Consumer<String> logFunction;

    // 사용자가 로깅 함수를 등록할 수 있도록 설정
    public void registerLogFunction(Consumer<String> logFunction) {
        this.logFunction = logFunction;
    }

    // 라이브러리 모듈 내에서 로깅 함수 호출
    public void doSomething() {
        if (logFunction != null) {
            logFunction.accept("LibraryModule: Doing something...");
        }
    }
}

// 사용자 코드
public class UserCode {
    public static void main(String[] args) {
        LibraryModule library = new LibraryModule();

        // 사용자는 로깅 함수를 등록
        library.registerLogFunction(message -> {
            // 로깅 함수가 호출될 때 수행할 동작 정의
            System.out.println("User's Log: " + message);
        });  // 해당 부분이 훅메소드임

        // 라이브러리 모듈의 함수 호출
        library.doSomething();
    }
}
```


# 추상클래스와 인터페이스의 차이점
추상 클래스는 클래스
따라서 인스턴스 변수를 가질 수 있으며, 생성자를 정의할 수 있음
추상 클래스는 일반 메서드(구현된 메서드)와 추상 메서드(구현되지 않은 메서드)를 모두 포함할 수 있음
하위 클래스는 여러 개의 클래스를 상속받을 수 없습니다. 즉, 단일 상속만 허용

인터페이스는 추상 메서드만을 정의하는 특수한 형태의 클래스
필드를 가질 수 없고, 모든 멤버 변수는 상수로 취급
모든 메서드는 추상 메서드이며, 디폴트 메서드와 정적 메서드를 정의할 수 있음
클래스는 여러 개의 인터페이스를 구현할 수 있으며, 다중 상속이 가능

# 함수형 프로그래밍
계산을 함수의 평가로 간주하고, 상태 및 변경 가능한 데이터보다는 불변성과 순수 함수(pure functions)를 강조하는 프로그래밍 스타일

- 순수 함수 (Pure Functions)
동일한 입력에 대해 항상 동일한 출력을 생성하며, 부작용(side effect)이 없는 함수를 의미
함수는 외부 상태를 변경하지 않고, 외부 상태에 의존하지 않음

- 불변성 (Immutability)
데이터는 변경 불가능하며, 새로운 데이터를 생성할 때 이전 데이터는 영향을 받지 않음

- First-Class 및 Higher-Order Functions
함수는 일급 시민(First-Class Citizen)으로 다뤄지며, 
함수를 다른 함수의 인자로 전달하거나 함수를 반환할 수 있음
이러한 함수를 고차 함수라고 부름

- 불변성 데이터 구조 (Immutable Data Structures):
함수형 프로그래밍에서는 불변성 데이터 구조를 사용하여 데이터를 효율적으로 조작하고 변경

- 재귀 (Recursion)
반복문 대신 재귀를 사용하여 반복적인 동작을 수행

- 선언형 프로그래밍 (Declarative Programming)
어떻게 수행할 것인지를 명시적으로 작성하는 대신 무엇을 수행할 것인지를 선언적으로 표현
SQL이 선언적 언어의 예시

- 모나드 (Monads)
함수형 프로그래밍에서 부작용을 다루는 방법 중 하나로, 
안전하게 부작용을 캡슐화하는 방법을 제공

`java.util.function` 패키지는 자바 8부터 소개된 함수형 프로그래밍을 지원하기 위한 함수형 인터페이스들을 제공하는 패키지
```
Function<T, R>
Predicate<T>
Consumer<T>
Supplier<T>
```

- 기존의 명령 프로그래밍 방식
```java
import java.util.ArrayList;
import java.util.List;

public class ImperativeExample {
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>();
        numbers.add(1);
        numbers.add(2);
        numbers.add(3);
        numbers.add(4);
        numbers.add(5);

        List<Integer> evenSquares = new ArrayList<>();
        for (Integer number : numbers) {
            if (number % 2 == 0) {
                evenSquares.add(number * number);
            }
        }

        for (Integer square : evenSquares) {
            System.out.println(square);
        }
    }
}
```

함수형 프로그래밍 방식
```java
import java.util.Arrays;
import java.util.List;

public class FunctionalExample {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);

        numbers.stream()
               .filter(n -> n % 2 == 0)  // 짝수 필터링
               .map(n -> n * n)          // 제곱값 계산
               .forEach(System.out::println);  // 출력
    }
}
```



# 시그니처
함수 또는 메서드의 특정 형식을 의미
메서드의 이름, 매개변수의 개수, 데이터 타입, 반환 타입 등을 모두 포함하는 함수 또는 메서드의 "서명"을 나타냄


# 제네릭
인터페이스는 공통의 기능을 가지는 클래스를 구별하지 않고 사용한다는 특성이 있기 때문에 구별하고 싶을 때 제네릭을 사용할 수 있음

만약 제네릭을 사용하지 않는다면 아래와 같이 instanceof 같은 비싼 연산을 사용하고, 다운캐스팅을 해줘야 함
```java
if(m instanceof Book && ((Book)m).matchesAuthor(kwd))
```
가독성을 해치고, 컴파일러가 오류를 잡지 못함

가장 대표적으로 제네릭을 사용하는 클래스가 ArrayList
```java
ArrayList strList = new ArrayList();
```
스트링 타입 객체만 리스트에 추가
다운캐스팅 불필요(항상 스트링 타입의 요소가 보장)
꺼낼 때는 스트링으로 자동 캐스팅해 줌

실제 ArrayList 구현부, 제네릭을 사용할 때 E가 String 타입으로 다 바뀌게 됨
```java
public class ArrayList<E> extends AbstractList<E>
        implements List<E>, RandomAccess, Cloneable, java.io.Serializable
{
    @java.io.Serial
    private static final long serialVersionUID = 8683452581122892189L;
	//..
```

여기에서 하위 클래스(타입)를 제한하려면 extends 키워드를 사용하면 됨
만약 상위 타입을 제한하려면 super를 사용하면 됨
```java
interface Factory<T extends Manageable>{
	T create();
}
```

```java
class Department extends Manager<Student> implements Factory<Student> {
    void run() {
        readAll("student.txt", this);
        printAll();
        Student st = find("김");
	    st.print();
    }

    @Override
    public Student create() {
        return new Student();
    }
}
```

다음과 같이 제네릭을 복잡하게 사용할 수도 있음
```java
class Coordinate<T extends Number & Comparable<T>> implements Comparable<Coordinate<T>> {
    private T x;
    private T y;

    public Coordinate() {
        System.out.println(toString() + " No data");
    }

    public Coordinate(T x, T y) {
        this.x = x;
        this.y = y;
    }

    public T getX() {
        return x;
    }

    public T getY() {
        return y;
    }

    @Override
    public int compareTo(Coordinate<T> o) {
        return o.getX().compareTo(this.x);
    }
}
```

# Collections 정렬
```java
import java.util.Collections;
Collections.sort(myList);
```
`
sort를 하려면 sort를 하게 만드는 메소드가 필요함
`Comparable` 인터페이스의 `compareTo`를 이용하면 됨

```java
public interface Comparable<T> {
    int compareTo(T o);
}
```

구현한 후 `Collections.sort(콜랙션)`를 이용하면 됨

```java
public class Student implements Comparable<Student> {
    private String name;
    private int age;

    // 생성자, getter, setter 등의 코드는 생략

    @Override
    public int compareTo(Student other) {
        // 이름을 기준으로 학생을 정렬
        return this.name.compareTo(other.getName());
    }
}

//메인
List<Student> students = new ArrayList<>();
// 학생 객체 추가

Collections.sort(students); // 이름을 기준으로 정렬

for (Student student : students) {
    System.out.println(student.getName());
}

```


# `Comparator <T>`
This를 이용하지 않고 두 요소 비교하는 메소드
똑같이 sort를 하려면 sort를 하게 만드는 메소드가 필요함
```java
class Student {
	private String name;
	private int score;

	public Student(String name, int score) {
		this.name = name;
		this.score = score;
	}

	public String getName() {
		return name;
	}

	public int getScore() {
		return score;
	}
}

class StudentComparator implements Comparator<Student>{
	
	@Override
	public int compare(Student a, Student b) {
		return a.getScore()-b.getScore();
	}
}

public class Sandbox {
	public static void main(String[] args) {
		List<Student> students = new ArrayList<>();
		students.add(new Student("Alice", 85));
		students.add(new Student("Bob", 70));
		students.add(new Student("Charlie", 95));
		
		// 학생 객체를 점수에 따라 정렬
		Collections.sort(students,new StudentComparator());

		for (Student student : students) {
			System.out.println(student.getName() + ": " + student.getScore());
		}
	}

}
```


# 와일드카드
제네릭 코드에서 타입을 유연하게 다루기 위해 사용됨
```java
class Box<T> {
    private T value;

    public Box(T value) {
        this.value = value;
    }

    public T getValue() {
        return value;
    }
}

public void printBox(Box<?> box) {
    // 어떤 타입의 상자도 인쇄 가능
    System.out.println(box.getValue());
}

Box<Integer> intBox = new Box<>(42);
Box<String> stringBox = new Box<>("Hello");

printBox(intBox); // 정수 상자를 출력
printBox(stringBox); // 문자열 상자를 출력
```

```java
public void printList(List<?> list) {
    for (Object element : list) {
        System.out.println(element);
    }
}

List<Integer> intList = Arrays.asList(1, 2, 3);
List<String> stringList = Arrays.asList("apple", "banana", "cherry");

printList(intList); // 정수 리스트를 출력
printList(stringList); // 문자열 리스트를 출력
```



# 업캐스팅, 다운캐스팅
모든 객체는 자기 타입을 알고 있다
모든 객체는 object 의 인스턴스고, object에는 type이라는 필드가 있음
type에서는 자신의 타입을 알고 있음

Object
Book
Ebook

`object o = new Ebook()`
여기서 o는 위에서 1칸까지만 읽음

`book b = new Ebook()`
b는 위에서 2칸까지만 읽음



# jar
cmd
`java --jar [파일이름.jar]`




# Object
심볼 주소를 다룰 수 없게 만듬
해시코드가 객체의 고유한 키값

-  상속 메소드
protected Object clone() throws CloneNotSupportedException
이 객체의 복사를 생성하여 리텀함

public boolean equals(Object obj)
주어진 다른 객체 obj가 이것과 같은지 여부를 돌려줌

public final Class getClass()
이 객체의 런타임 클래스를 돌려줌

public int hashCode()
객체의 해시코드 값을 반환

public String toString()
객체의 문자열 표현을 반환

## clone()
깊은 복사 안함
Cloneable implements
CloneNotSupportedException 구현

깊은 복사하고 싶으면 각 클래스가 구현해야 함

```java
class ShoppingCart implements Cloneable {
	String userName;
	ArrayList cartItems = new ArrayList<>();
	@Override
	public Object clone() throws CloneNotSupportedException {
		ShoppingCart cloned = (ShoppingCart)super.clone();
		cloned.cartItems = new ArrayList();
		cloned.cartItem.addAll(this.cartItems);
		return cloned;
	}
}
```


## equals()
새로 만든 객체에 대해 같다를 정의하고 싶을 때 사용
해시코드가 같으면 같다고 인식

```java
public class Book {
	public boolean equals(Object obj) {
		if (!obj instanceof Book)
			return false;
		Book b = (Book) obj;
		return ISBN.equals(b.getISBN());
	}
}
```

- contentEquals
`char[]`이나 `StringBuilder` 등 스트링과 비슷한 역할을 하는 다른 클래스 문자열 내용이 동일하면 같다고 취급


## getClass()
클래스는 스스로 자기가 무엇인지 알고 있음
클래스 타입을 리턴(Class 클래스)
이름, 패키지, 접근자 등

동적으로 객체 생성 가능
Ob의 타입으로 객체를 생성
Object ob2 = ob.getClass().getDeclaredConstructor().newInstance();
Try … catch로 묶어주어야 함 – checked 예외 발생


## hashCode()
객체를 고유한 숫자로 나타내는 값
vm이 주소에 해당하는 해시코드를 알고 있음
해시코드가 같으면 같은 객체
컬렉션의 contains 메소드는 hashCode()로 비교함
equals()를 오버라이드한 경우 hashCode()를 변경하는 것이 좋음


## toString()
default - `getClass().getName() + '@' + Integer.toHexString(hashCode())`
새로 만드는 클래스에서는 toString() 메소드를 항상 오버라이드해야 함



# final
필드, 메소드, 클래스에서 사용
처음 한 번은 초기화 가능

- 필드
필드의 값이 바뀌지 않음을 뜻함

- 메소드
메소드 final이면 오버라이드 불가
생성자에서 호출하는 함수는 final이어야 함 (권장사항)

- 클래스
상속불가
Immutable 클래스의 경우 final로 선언
동작이 바뀌지 못하게 하는 목적


# Number 상속 클래스
기본 타입이 없으면, 오버헤드가 너무 많이 나옴
성능을 높이기위해 기본 타입, 클래스 타입 두 가지를 모두 지원
그 두 가지 사이의 호환성을 위해 Number 상속 클래스를 사용
그 이외의 기능은 없음(계산, 비교 등은 못함)

기본타입이 허용되지 않는 경우 -> ArrayList에 넣을 때
라이브러리를 사용하기 위해 Object를 상속한 객체여야 되는 경우
![[Pasted image 20231124095408.png]]

여기에 Boolean, char 이렇게 총 8개의 기본 타입이 있음

- 반싱, 언박싱
오토박싱이란 자바 컴파일러가 기본 타입 값을 그에 대응하는객체 래퍼 클래스로 자동 변환하는 것
변환이 반대 방향이 되면 언박싱
`Character ch = 'a';` -> 박싱

계산이 필요하면 언박싱
객체를 필요로 하면 박싱이 자동으로 일어남


# 스트링
```java
public static boolean isNumeric(String input) {
	try {
		Double.parseDouble(input);
		return true;
	} catch (NumberFormatException e) {
		return false;
	}
}
```

- 불변성
지정에서 그냥 참조만 가져가도 됨
객체를 자유롭게 공유할 수 있음
나도 모르게 다른 참조에 의해 내 객체의 값이 바뀌는 일은 없음
변경 연산은 계속 새로운 객체를 생성함
+, replace, substring 등 연산은 계속 쓰레기를 만들어냄
-> StringBuilder 사용하면 됨


# enum


# 람다
자바는 함수 전달을 할 수 없음(모든 건 객체)
따라서 함수 전달을하려면 무명 클래스를 사용해야 함

아래와 같이 무명클래스를 사용하여 구현할 수 있는데 다소 거추장스러움
```java
Collections.sort(mylisy, Comparator<MyClass>() {
	@Override
	public void compare(MyClass ob1, MyClass ob2) {
	
	}
}
```

아래와 같이 람다를 사용하면 가독성이 향상됨
```java
Collections.sort(mylisy, (x, y) -> x.id – y.id);
```


람다식은 인터페이스를 구현한 객체
간단한 코드의 부분을 전달하는 방법
함수를 만들지 않고 (이름을 붙이지 않고) 코드 부분을 전달 또는 이용
한 번만 쓰일 함수 (Anonymous function): 객체생성 효과

다음과 같이 생략할 수 있음
```java
(int a) -> { System.out.println(a) }
(a) -> { System.out.println(a) } 
a -> System.out.println(a)
```

매개 변수가 없는 경우 생략 불가
```java
( ) -> { 실행문; ... }
```

리턴문 하나만 있는 경우
```java
x -> { return x*x; }
```

가장 간단한 형태
```java
x -> x*x
```

- 함수형 인터페이스
인터페이스가 함수 하나만 들고 있어야 람다 사용가능
이러한 함수를 함수형 인터페이스라고 함
함수 전달을 목표로 하는 인터페이스로 쓰임
`@FunctionalInterface`라는 어노테이션이 붙음

인터페이스가 쓰이는 자리에 람다 객체 전달 가능
무명클래스 생성한 것과 같은 효과

- 적합한 상황
함수형 인터페이스와 같이 사용
함수 코드가 1-2줄 정도로 짧음
간단한 수식을 반환하는 경우 등에 적합
부수효과가 있는 경우 바람직하지 않음 - 지역변수 매개변수 이외의 것을 건드림(read-only는 OK)

- 장점
코드가 간결해져 개발자의 의도가 명확히 드러나므로 가독성이향상
분산 병렬을 하기 위함 - >일반적으로 다중 cpu를 활용하는 형태로 구현되어 병렬 처리에 유리
따라서 부수효과(외부에 영향을 주는 로직)은 이러한 장점을 살지지 못하게 됨

- 단점
디버깅 시 함수 호출 스택 추적이 다소 어려움
지나치게 남발하면 코드가 이해하기 어렵고 지저분해짐
람다를 사용하여 만든 무명함수는 재사용이 불가능함
재귀 호출을 사용할 수 없음
반복 회수가 많은 경우 람다식이 조금 느릴 수 있음 (함수를 컴파일한 것보다 느릴 수 있음)

- 람다에 쓰이는 변수
스트림 요소 : 람다 내의 지역변수
람다 내의 지역변수는 Final 또는 effectively final 이어야 함



# 스트림



- 9
제네릭 선언방법
타입파라미터
타입파라미터 제약조건
매니저 팩토리 매니저블 상요법
컬랙션에서 매니저 사용

- 10
제네릭 기본클래스들
기본 클래스 계층 구조
5개정도 크랠스에 대해서 settext이런거만 알면된다고..
contentpanel
listener 


# 질문 
와일드카드 사용법 T랑 ? 랑 차이점 언제 사용하는

`class Coordinate<T extends Number & Comparable<T>> implements Comparable<Coordinate<T>> {`
이건 왜되는거? 중복상속안된대매
