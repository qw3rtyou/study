#include <stdio.h>
int main (void){
    int basket[101];

    for (int i = 0; i < 101; i++)
    {
        basket[i]=i;
    }
    
    int basket_num;
    int case_num;

    scanf("%d %d",&basket_num,&case_num);

    int start,end,tmp;

    for (int i = 0; i < case_num; i++)
    {
        scanf("%d %d",&start,&end);
        for (int j = start; j <= start+(end-start)/2; j++)
        {
            tmp=basket[j];
            basket[j]=basket[start+end-j];
            basket[start+end-j]=tmp;
        }
    }

    for (int i = 1; i < basket_num+1; i++)
    {
        printf("%d ",basket[i]);
    }
    

    return 0;
}