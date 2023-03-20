#include <stdio.h>
#include <string.h>

int main (void){
    char input[100];
    
    scanf("%s",input);

    int size=strlen(input);

    int count=0;
    int table[26]={-1};

    for (int i = 0; i < 26; i++)
    {
        for (int j = 0; j < size; j++)
        {
            if ((int)input[j]==i+97)
            {
                table[i]=j;
                break;
            }

            if (j==size-1)
            {
                table[i]=-1;
            }
            
        }
    }
    

    for (int i = 0; i < 26; i++)
    {
        printf("%d ",(table[i]));
    }
    

    return 0;
}