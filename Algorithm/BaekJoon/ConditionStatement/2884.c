#include <stdio.h>
int main (void){
    int a,b;
    scanf("%d\n%d",&a,&b);

    int flag=0;

    if (b<45)
    {   
        b+=15;
        flag=1;
    } else{
        b-=45;
    }

    if (flag==1)
    {
        a=(a+23)%24;
    }
    
    printf("%d %d",a,b);
    
    return 0;
}