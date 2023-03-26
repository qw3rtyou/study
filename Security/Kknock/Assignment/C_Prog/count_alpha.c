#include <stdio.h>
#include <string.h>

int main(void){
    char input[100];
    scanf("%[^\n]",input);
    int cnt=0;

    for (int j = 65; j < 91; j++)
    {
        for (int i = 0; i < strlen(input); i++)
        {
            if ((int)input[i]==j)
            {
                cnt++;
            }
        }
        printf("%c: %d개\n",j,cnt);
        cnt=0;
    }
    
    return 0;
}