#include <stdio.h>

void swap(int *a,int *b){
    int tmp;
    tmp=*a;
    *a=*b;
    *b=tmp;
}

int main(){
    int a=5,b=12;
    printf("a: %d\tb: %d\n",a,b);
    swap(&a,&b);
    printf("a: %d\tb: %d\n",a,b);
    return 0;
}