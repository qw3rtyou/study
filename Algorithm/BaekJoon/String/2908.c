#include <stdio.h>
#include <string.h>

int main (void){
    char a[4];
    char b[4];

    scanf("%s %s",a,b);
    
    int tmp=0;

    tmp=a[0];
    a[0]=a[2];   
    a[2]=tmp;

    tmp=b[0];
    b[0]=b[2];   
    b[2]=tmp;
    
    int _a=100*(int)a[0]+10*(int)a[1]+(int)a[2];
    int _b=100*(int)b[0]+10*(int)b[1]+(int)b[2];

    printf("%d",(_a>_b)?_a:_b);
}