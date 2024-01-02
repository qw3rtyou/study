# 동적할당

<aside> 💡 이번에 공부할 내용은 다음과 같습니다.

1. 동적할당의 개념과 필요성
2. 동적할당의 사용 방법과 함수들
3. 동적할당과 구조체
4. typedef 와의 연계
5. 동적할당의 주의점과 메모리 누수

동적할당은 프로그램 실행 중에 필요한 만큼의 메모리를 할당받는 것을 말합니다. 동적할당을 사용하면 메모리의 효율적인 사용이 가능하며, 배열과 같이 미리 크기를 지정하지 않아도 되는 장점이 있습니다.

동적할당은 malloc, calloc, realloc 함수를 이용하여 수행할 수 있으며, 할당받은 메모리는 반드시 free 함수를 이용하여 해제해야 합니다.

</aside>

---

```c
// 다음과 같은 코드가 오류가 나지 않게 수정하여 봅시다.
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr;
    arr = (int*)malloc(sizeof(int) * 5);

    for(int i = 0; i < 5; i++){
        arr[i] = i;
    }

	//여기에 작성

	for(int i = 6; i < 10; i++){
        arr[i] = i;
    }

    for(int i = 0; i < 10; i++){
        printf("%d ", arr[i]);
    }
    free(arr);

    return 0;
}
```

---

```c
// 아래의 코드를 개선하여 봅시다.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Student {
    char name[20];
    int age;
};

int main() {
    struct Student *s;
    s = (struct Student*)malloc(sizeof(struct Student));

    strcpy(s->name, "Nogony");
    s->age = 20;

    printf("Name: %s, Age: %d\n", s->name, s->age);
    free(s);

    return 0;
}
```

---

```c
// 동적할당을 이용하여 이중 포인터를 활용한 2차원 배열 구현
// 아래의 코드에서 오류가 나는 이유를 찾아 수정하여 봅시다.
#include <stdio.h>
#include <stdlib.h>

int main() {
    int **arr;
    int row = 3;
    int col = 4;

    arr = (int**)malloc(sizeof(int*) * row);

    // 오류발생!

    for(int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            arr[i][j] = i * col + j;
        }
    }

    for(int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }

    for(int i = 0; i < row; i++){
        free(arr[i]);
    }
    free(arr);

    return 0;
}
```

---

<aside> 🔥 다음과 같은 내용을 도전해봅시다.

1. 1번째 예시에서 동적할당받은 배열의 크기를 늘려보기 (realloc 함수 사용)
2. 2번째 예시에서 typdef를 이용하여 코드 개선하기
3. 3번째 예시에서 오류가 나는 이유를 찾아 수정해보기

</aside>