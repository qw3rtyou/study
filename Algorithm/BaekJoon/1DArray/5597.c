#include <stdio.h>
int main (void){
    int array[31]={0};
    int buf;

    for (int i = 0; i < 28; i++)
    {
        scanf("%d",&buf);
        array[buf]=1;
    }

    for (int i = 1; i < 31; i++)
    {
        if (array[i]==0)
        {
            printf("%d\n",i);
        }
    }

    return 0;
}