#include <stdio.h>
#define MAX(i, j) (((i) > (j)) ? (i) : (j))

int main (void){
    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);
    int cash=0;

    if (a==b && b==c)
    {
        cash+=10000+a*1000;
    } else if (a==b|b==c)
    {
        cash+=1000+b*100;
    } else if (c==a)
    {
        cash+=1000+a*100;
    } else
    {
        cash=MAX(MAX(a,b),c)*100;
    }

    printf("%d",cash);
    
    return 0;    
}