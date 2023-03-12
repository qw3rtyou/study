#include <stdio.h>
int main (void){
    int a,b,c;
    scanf("%d %d\n%d",&a,&b,&c);
    
    if (b+c>=60)
    {
        a=(a+(b+c)/60)%24;
        b=(b+c)%60;
    } else{
        b+=c;
    }

    printf("%d %d",a,b);

    return 0;    
}