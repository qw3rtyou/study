#include <stdio.h>
#include <string.h>

int main(){
    char input[102];
    scanf("%s",input);
    int len=strlen(input);

    for (int i = 0; i < len; i++)
    {
        if (input[i]!=input[len-i-1]) 
        {
            printf("0");
            return 0;
        }
    }
    printf("1");
    return 0;
}