#include <stdio.h>
#include <string.h>

int main (void){
    char input[1000];
    int num;

    scanf("%d",&num);
    
    for (int i = 0; i < num; i++)
    {
        scanf("%s",input);
        printf("%c%c\n",input[0],input[strlen(input)-1]); 
    }
    
    return 0;
}