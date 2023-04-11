#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int num, limit;
    int *tmp;
    scanf("%d %d", &num, &limit);
    
    tmp = (int *)malloc(num * sizeof(int)); // num만큼 int형 변수를 동적으로 할당
    
    for (int i = 0; i < num; i++) {
        scanf("%d", &tmp[i]); // 동적으로 할당한 배열에 입력값 저장
        if (tmp[i] < limit) {
            printf("%d ", tmp[i]);
        }
    }
    free(tmp); // 할당된 메모리 반환
    return 0;
}