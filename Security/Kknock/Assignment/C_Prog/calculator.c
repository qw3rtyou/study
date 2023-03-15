#include <stdio.h>

int main(void){
    int a,b;
    char op;
    int res;

    jump:
        printf("입력 예시)2+4, 5-2, 6*8, 4/2, 6%2\n계산 식 입력: ");
        scanf("%d%d%c",&a,&b,&op);
    
        switch (op)
        {
        case '+':
            res=a+b;
            break;
        case '-':
            res=a-b;
            break;
        case '*':
            res=a*b;
            break;
        case '/':
            res=a/b;
            break;
        case '%':
            res=a%b;
            break;
        
        default:
            printf("입력오류!\n");
            goto jump;
        }

    printf("%d %c %d %d",a,op,b,res);

    return 0;
}