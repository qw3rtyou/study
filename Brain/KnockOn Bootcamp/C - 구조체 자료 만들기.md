# 구조체

<aside> 💡 이번에 공부할 내용은 다음과 같습니다.

1. 구조체의 개념과 용도
2. 구조체 선언과 초기화
3. 구조체와 배열, 포인터의 관계
4. 구조체와 함수
5. 구조체의 중첩과 typedef

구조체는 여러 개의 다른 자료형의 변수들을 하나의 이름으로 묶어서 관리할 수 있는 고급 자료형입니다. 
구조체를 이용하면 서로 다른 자료형의 데이터를 묶어서 하나의 덩어리로 처리할 수 있습니다.

구조체는 간단한 변수와 배열, 포인터 등을 기반으로 복잡한 자료구조를 만들기 위한 기본적인 틀이자 도구입니다.

</aside>

---

```c
// 다음과 같은 코드를 이해해봅시다.
#include <stdio.h>

struct Student {
    char name[20];
    int score;
};

void print_student(struct Student* s) {
    printf("Name: %s, Score: %d\n", s->name, s->score);
}

int main() {
    struct Student s1 = {"Nogony", 90};
	print_student(&s1);
    return 0;
}
```

---

```c
// 아래의 코드의 실행 결과를 예상하여 봅시다
#include <stdio.h>

struct Point {
    int x, y;
};

struct Point add_point(struct Point p1, struct Point p2) {
    struct Point result = {p1.x + p2.x, p1.y + p2.y};
    return result;
}

int main() {
    struct Point p1 = {1, 2};
    struct Point p2 = {3, 4};
    struct Point p3 = add_point(p1, p2);
    printf("(%d, %d)\n", p3.x, p3.y);
    return 0;
}
```

---

```c
#define SIZE 200
struct Wc {
	char word[30];
	int count;
};

struct Wc simbol_table[SIZE];
int idx=0;

void count(input) {
    // 이곳을 완성
}

#define INPUT_SIZE 4
int main() {
	char buf[100];

	for (int i = 0; i < INPUT_SIZE; i++)
	{
		printf("단어를 입력하세요 : ");
		scanf("%s", buf);
		count(buf);
	}

	printf("\n[빈도수]\n");
	for (int i = 0; i < idx; i++)
	{
		printf("%s : %d\n", simbol_table[i].word, simbol_table[i].count);
	}
}
```
---

<aside> 🔥 다음과 같은 내용을 도전해봅시다.

1. 1번째 예시에서 1명이 아닌 5명의 학생 정보를 배열을 이용해 여러 학생의 정보를 출력 동작을 구현하기
2. 2번째 예시에서 두 점의 좌표를 더하는 함수의 동작 원리 및 실행 결과 예상하기
3. 3번째 예시에서 단어의 개수를 세는 count 함수 완성하기
4. 구조체를 이용한 복소수 연산 함수 구현해보기 (덧셈, 뺄셈, 곱셈)

</aside>