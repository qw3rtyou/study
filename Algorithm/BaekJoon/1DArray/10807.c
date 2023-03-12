#include <stdio.h>
int main (void){
    int a[100];
    int num;
    scanf("%d",&num);

    for (int i = 0; i < num; i++)
    {
        scanf("%d",a+i);
    }

    int key;
    scanf("%d",&key);
    int cnt=0;

    for (int i = 0; i < num; i++)
    {
        if (*(a+i)==key)
        {
            ++cnt;
        } 
    }

    printf("%d",cnt);
    
    return 0;
}