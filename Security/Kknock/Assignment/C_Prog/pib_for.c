#include <stdio.h>
//피보나치 for문 버전
int fibonacci(int i){
    int a=1,b=1;
    int tmp=0;

    for (int j = 1; j < i; j++) {
        tmp=a;
        a=a+b;
        b=tmp;
    };
    
    return a;
}

int main(){
    int input;

    printf("정수를 입력하세요: ");
    scanf("%d",&input);

    for (int i = 0; i < input; i++) printf("%d번째: %d\n",i+1,fibonacci(i));

    return 0;
}