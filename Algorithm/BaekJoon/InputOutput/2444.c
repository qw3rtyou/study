#include <stdio.h>

int main (void){
    int input;
    scanf("%d",&input);

    for (int i = 0; i < input-1; i++)
    {
        for (int j = 0; j < input-1-i; j++) printf(" ");
        for (int j = 0; j < 2*i+1; j++) printf("*");
        printf("\n");
    }

    for (int i = 0; i < 2*input-1; i++)
    {
        printf("*");
    }
    printf("\n");

    for (int i = input-2; i >= 0; i--)
    {
        for (int j = 0; j < input-1-i; j++) printf(" ");
        for (int j = 0; j < 2*i+1; j++) printf("*");
        printf("\n");
    }
    

    return 0;
}