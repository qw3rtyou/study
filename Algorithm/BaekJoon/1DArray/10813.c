#include <stdio.h>
int main (void){
    int array[101];

    for (int i = 0; i < 101; i++)
    {
        array[i]=i;
    }
    

    int array_size, num;

    scanf("%d %d",&array_size, &num);

    int a,b,tmp;

    for (int i = 0; i < num; i++)
    {
        scanf("%d %d",&a,&b);

        tmp=array[a];
        array[a]=array[b];
        array[b]=tmp;
    }
    
    for (int i = 1; i < array_size+1; i++)
    {
        printf("%d ",array[i]);
    }
    
    return 0;
}