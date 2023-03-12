#include <stdio.h>
int main (void){
    int array[9];
    
    for (int i = 0; i < 9; i++)
    {
        scanf("%d",array+i);
    }
    
    int max_num=-1;
    int max_index=0;

    for (int i = 0; i < 9; i++)
    {
        if (max_num<*(array+i))
        {
            max_num=*(array+i);
            max_index=i;
        }
    }

    printf("%d\n%d", max_num, max_index+1);
    
    return 0;
}