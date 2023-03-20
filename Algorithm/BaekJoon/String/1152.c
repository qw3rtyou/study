#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main (void){
    char input[1000002];
    scanf("%[^\n]s",input);

    int cnt=0;

    if(input[0]!=' ') cnt++;

    for (int i = 0; i < strlen(input); i++)
    {
        if(input[i-1]==' ' && input[i]!=' ') cnt++;
    }
    
    printf("%d",cnt);

    return 0;
}