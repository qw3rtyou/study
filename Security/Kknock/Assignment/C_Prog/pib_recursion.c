#include <stdio.h>
//피보나치 재귀 버전
int fibonacci(int i){
    if (i==0||i==1) return 1;
    else return fibonacci(i-1)+fibonacci(i-2);
}

int main(){
    int input;

    printf("정수를 입력하세요: ");
    scanf("%d",&input);

    for (int i = 0; i < input; i++) printf("%d번째: %d\n",i+1,fibonacci(i));

    return 0;
}