#include <stdio.h>
int main (void){
    int table[42]={0};
    int buffer;

    for (int i = 0; i < 10; i++)
    {
        scanf("%d",&buffer);
        table[buffer%42]=1;
    }
    
    buffer=0;

    for (int i = 0; i < 42; i++)
    {
        if (table[i]==1)
        {
            buffer++;
        }
        
    }

    printf("%f",buffer);

    return 0;
}