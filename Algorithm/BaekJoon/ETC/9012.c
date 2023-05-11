#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//(:40 ):41
int main() {
    int size;
    scanf("%d", &size);
    char** input = (char**)malloc(sizeof(char [51]) * size);

    for (int i = 0; i < size; i++)
    {
        input[i] = (char*)malloc(sizeof(char) * 51);
        scanf("%s", input[i]);
        int len = strlen(input[i]);
        int cnt = 0;

        for (int j = 0; j < len; j++)
        {
            if (input[i][j] == 40) cnt++;
            else if (input[i][j] == 41 && cnt == 0) {
                printf("NO\n");
                break;
            }
            else cnt--;
            if (j == len - 1) {
                if (cnt == 0) printf("YES\n");
                else printf("NO\n");
            } 
        }
       
    }

    return 0;
}