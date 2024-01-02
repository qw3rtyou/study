# 파일 입출력

<aside> 💡 이번에 공부할 내용은 다음과 같습니다.

1. 파일 입출력의 개념과 필요성
2. 파일 열기와 닫기
3. 파일에서 데이터 읽고 쓰기
4. 파일 위치 지시자 개념, 제어하는 함수들
5. 파일 입출력과 에러 처리
6. 파일 디스크립터

파일 입출력은 프로그램이 파일에 데이터를 쓰거나 파일로부터 데이터를 읽는 작업을 말합니다. 파일 입출력을 이용하면 프로그램이 종료된 후에도 데이터를 유지할 수 있으며, 다른 프로그램과 데이터를 공유할 수 있습니다.

파일 입출력은 fopen, fclose 함수를 이용하여 수행할 수 있으며, 파일에서 데이터를 읽고 쓰는 것은 fscanf, fprintf, fread, fwrite 등의 함수를 이용할 수 있습니다. 한편, fseek, ftell 등의 함수를 사용하여 파일 위치 지시자를 제어할 수 잇습니다.

</aside>

---

```c
// 다양한 모드를 사용해 봅시다.
#include <stdio.h>

int main() {
    FILE *fp;
    fp = fopen("test.txt", "w");

    if(fp == NULL) {
        printf("파일 열기 실패");
        return 0;
    }

    fprintf(fp, "Hello, File!");

    fclose(fp);

    return 0;
}
```

---

```c
// 모든 줄을 읽을 수 있도록 코드를 수정하여 봅시다.
#include <stdio.h>

int main() {
    FILE *fp;
    char str[20];

    fp = fopen("test.txt", "r");

    if(fp == NULL) {
        printf("파일 열기 실패");
        return 0;
    }

    fscanf(fp, "%s", str);

    printf("%s\n", str);

    fclose(fp);

    return 0;
}
```

---

```c
// 다음과 같은 코드는 파일 위치 지시자를 이용한 예시입니다.
#include <stdio.h>

int main() {
    FILE *fp;
    char str[20];

    fp = fopen("test.txt", "r+");

    if(fp == NULL) {
        printf("파일 열기 실패");
        return 0;
    }

    fprintf(fp, "Hello, File!");

    fseek(fp, 0, SEEK_SET);

    fscanf(fp, "%s", str);

    printf("%s\n", str);

    fclose(fp);

    return 0;
}
```

---

<aside> 🔥 다음과 같은 내용을 도전해봅시다.

1. 1번째 예시에서 다른 모드로 파일을 열어보기 (예: "a", "r+", "w+")
2. 2번째 예시에서 파일 전체를 읽어보기 (while문과 feof 함수 사용)
3. 3번째 예시에서 fseek()를 이용하여 3번 반복하여 읽어보기

</aside>