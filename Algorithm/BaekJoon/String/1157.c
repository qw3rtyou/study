#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main (void){
    char input[1000002];
    scanf("%s",input);
    int size=strlen(input);

    for (int i = 0; i < size; i++)
    {
        input[i]=toupper(input[i]);   
    }

    char max_char='?';
    int max_num=0;
    int cnt=0;

    for (char i = 65; i < 91; i++)
    {
        for (int j = 0; j < size; j++)
        {
            if (i==input[j]) cnt++;
        }

        if (cnt>max_num){
            max_char=i;
            max_num=cnt;
        } else if(cnt==max_num){
            max_char='?';
        }

        cnt=0;
    }
    
    printf("%c",max_char);

    return 0;
}