#include <stdio.h>

int main (void){
    char input[1000];
    int idx;

    scanf("%s\n%d",input,&idx);

    printf("%c",input[idx-1]);

    return 0;
}