# 함수

<aside> 💡 이번에 공부할 내용은 다음과 같습니다.

1. 함수의 기본 개념과 용도
2. 함수의 선언과 정의
3. 매개변수와 반환값
4. 함수의 스코프
5. 재귀 함수
6. 함수 포인터
7. 가변인자

함수는 특정 작업을 수행하는 코드의 묶음입니다. 코드의 재사용성을 높이고, 코드의 구조를 명확하게 하며, 프로그램의 복잡성을 줄이는 데 도움이 됩니다.

</aside>

---

```c
// 다음과 같은 코드를 이해해봅시다.
#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(5, 10);
    printf("The result is %d\n", result);
    return 0;
}
```

---

```c
// 아래의 코드의 실행 결과를 예상하여 봅시다
#include <stdio.h>

void print_hello(int n) {
    if (n <= 0) return;
    printf("Hello, World!\n");
    print_hello(n - 1);
}

int main() {
    print_hello(5);
    return 0;
}
```

---

```c
double add(double a, double b) {
	return a + b;
}

double sub(double a, double b) {
	return a - b;
}

double mul(double a, double b) {
	return a + b;
}

double dvd(double a, double b) {
	return a / b;
}

int main() {
	int select;
	int a, b;
	//함수포인터 선언부

	printf("===============\n");
	printf("0. 덧셈\n");
	printf("1. 뺄셈\n");
	printf("2. 곱셈\n");
	printf("3. 나눗셈\n");
	printf("4. 종료\n");
	printf("===============\n\n");

	printf("메뉴를 선택하시오 : ");
	scanf("%d", &select);

	printf("2개의 정수를 입력하시오 : ");
	scanf("%d %d", &a, &b);

	printf("연산결과 = %f\n", pf[select](a, b));
}
```
---


<aside> 🔥 다음과 같은 내용을 도전해봅시다.

1. 1번째 예시에서 함수의 선언, 정의, 호출 과정 설명하기
2. 2번째 예시에서 재귀 함수의 동작 과정 및 실행 결과 예상하기
3. 3번째 예시에서 함수 포인터를 이용하여 프로그램 완성하기

</aside>
