#include <stdio.h>

int main (void){
    int a,b;
    int num;

    scanf("%d",&num);

    for (int i = 0; i < num; i++)
    {
        scanf("%d %d",&a,&b);
        printf("Case #%d: %d\n",i,a+b);
    }
    
    return 0;
}

/*
testcase

5
1 1
2 3
3 4
9 8
5 2

*/