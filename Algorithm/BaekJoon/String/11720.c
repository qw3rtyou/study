#include <stdio.h>

int main (void){
    char input[100];
    int size;

    scanf("%d\n%s",&size,input);

    int sum=0;

    for (int i = 0; i < size; i++)
    {
        sum+=(int)input[i]-48;
    }
    
    printf("%d",sum);

    return 0;
}