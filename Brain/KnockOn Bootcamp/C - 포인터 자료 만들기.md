# 포인터

<aside> 💡 이번에 공부할 내용은 다음과 같습니다.

1. 포인터의 기본 개념과 용도
2. 포인터를 사용하는 이유와 장점
3. 포인터의 선언과 사용 방법
4. 포인터와 배열 사이의 관계
5. Call by Value, Call by Reference
6. 이중 포인터

포인터는 메모리 주소를 저장하고 참조하는 데 사용되며, C 언어에서는 매우 중요한 요소 중 하나입니다. 포인터를 통해 메모리를 효율적으로 관리할 수 있으며, 복잡한 자료 구조를 구현할 때 필수적인 도구입니다.

추후에 배울 리버싱, 시스템 해킹에서는 포인터를 알아야 깊이 있는 학습을 진행할 수 있습니다.

</aside>

---

```c
// 다음과 같은 코드를 이해해봅시다.
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 5, y = 10;
    printf("x: %d, y: %d\\\\n", x, y);
    swap(&x, &y);
    printf("x: %d, y: %d\\\\n", x, y);
    return 0;
}

```

---

```c
// 아래의 코드의 실행 결과를 예상하여 봅시다
void main() {
	char m[] = "ABC";
	char* ap = m;
	*ap++ += 1;		
	*++ap += 3;		
	ap -= 2;		
	ap[1] += 2;		
	puts(m);		
}
```

---

<aside> 🔥 다음과 같은 내용을 도전해봅시다.

1. 1번째 예시에서 Call by Value, Call by Reference 개념 설명하기
2. 2번째 예시에서 실행 결과 예상하기, 설명하기

</aside>