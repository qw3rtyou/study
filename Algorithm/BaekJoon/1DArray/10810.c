#include <stdio.h>
int main (void){
    int a,b;
    int basket[100]={0};

    scanf("%d %d",&a, &b);

    int start,end;
    int num;

    for (int i = 0; i < b; i++)
    {
        scanf("%d %d %d",&start,&end,&num);

        for (int i = start-1; i < end; i++)
        {
            basket[i]=num;
        }
        
    }
    
    for (int i = 0; i < a; i++)
    {
        printf("%d ",basket[i]);
    }

    return 0;
}