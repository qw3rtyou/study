# 문자열

<aside> 💡 이번에 공부할 내용은 다음과 같습니다.

1. 문자열의 개념과 용도
2. 문자열의 선언과 초기화
3. 문자열과 배열의 관계
4. 문자열과 포인터의 관계
5. 문자열 관련 함수들

문자열은 문자들의 집합으로, C 언어에서는 문자 배열로 표현됩니다.
여러 문자를 하나의 이름으로 관리할 수 있어, 다양한 정보를 표현하고 처리하는 데 유용합니다.

단순히 어떤 데이터를 표현하는 자료형일 뿐이라고 생각할 수 있지만, 포인터, 배열과 연계되는 개념이고 깊이 다루다 보면 정말 다양한 개념을 배울 수 있는 중요한 주제입니다.

</aside>

---

```c
// 다음과 같은 코드를 이해해봅시다.
#include <stdio.h>

void reverse(char* str) {
    int len = 0;
    while(str[len] != '\0') {
        len++;
    }

    for(int i=0; i<len/2; i++) {
        char temp = str[i];
        str[i] = str[len-i-1];
        str[len-i-1] = temp;
    }
}

int main() {
    char str[] = "Hello, World!";
    reverse(str);
    printf("%s\n", str);
    return 0;
}
```

---

```c
// 아래의 코드의 실행 결과를 예상하여 봅시다
#include <stdio.h>
#include <string.h>

int find_char(char* str, char c) {
    for(int i=0; str[i] != '\0'; i++) {
        if(str[i] == c) {
            return i;
        }
    }
    return -1;
}

int main() {
    char str[] = "Hello, World!";
    char c = 'o';
    int pos = find_char(str, c);
    if(pos != -1) {
        printf("The character '%c' found at position %d\n", c, pos);
    } else {
        printf("The character '%c' not found\n", c);
    }
    return 0;
}
```

---

<aside> 🔥 다음과 같은 내용을 도전해봅시다.

1. 1번째 예시에서 문자열을 뒤집는 함수의 동작 원리 설명하기
2. 2번째 예시에서 문자열 중에 특정 문자를 찾는 함수의 동작 원리 및 실행 결과 예상하기
3. strcat(), strcpy(), strcmp() 등등 기본 문자열 함수를 구현해보기 (string 헤더 include 금지!!)
4. 문자열 사이 공백을 제거(void MyNoSpace(char* str) {})
5. 단어 개수 세기(int MyCountWord(char* str, char* target) {}),  

</aside>