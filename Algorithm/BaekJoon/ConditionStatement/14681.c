#include <stdio.h>
int main (void){
    int a,b;
    scanf("%d\n%d",&a,&b);

    if (a>0&b>0)
    {
        printf("1");
    }else if(a<0&b>0){
        printf("2");
    }else if(a<0&b<0){
        printf("3");
    }else{
        printf("4");
    }
    
    return 0;
}