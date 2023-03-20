#include <stdio.h>
#include <string.h>

int main (void){
    int mul;
    int size;
    char input[20];

    scanf("%d",&size);

    for (int i = 0; i < size; i++)
    {
        scanf("%d %s",&mul,input);
        
        for (int j = 0; j < strlen(input); j++)
        {
            for (int k = 0; k < mul; k++)
            {
                printf("%c",input[j]);
            }
        }
        printf("\n");
    }
    return 0;
}