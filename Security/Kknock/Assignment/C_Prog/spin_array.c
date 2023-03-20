#include <stdio.h>

int main(void){
    int arr_basic[4][4]={ {0, 1, 1, 0}, {4, 0, 0, 2}, {4, 0, 0, 2},{0, 3, 3, 0} };
    int arr_90[4][4],arr_180[4][4],arr_270[4][4];

    printf("=== Basic Arr ===\n");
    for (int i = 0; i < 4; i++)
    {       
        for (int j = 0; j < 4; j++)
        {
            printf("%d",arr_90[i][j]);
        }
        printf("\n");
    }


    for (int i = 0; i < 4; i++)
    {       
        for (int j = 0; j < 4; j++)
        {
            arr_90[i][j]=arr_basic[3-j][i];
        }
        
    }
    printf("=== Basic Arr ===\n");
    for (int i = 0; i < 4; i++)
    {       
        for (int j = 0; j < 4; j++)
        {
            printf("%d",arr_90[i][j]);
        }
        printf("\n");
    }


    for (int i = 0; i < 4; i++)
    {       
        for (int j = 0; j < 4; j++)
        {
            arr_180[i][j]=arr_basic[3-i][3-j];
        }
        
    }
    printf("=== Basic Arr ===\n");
    for (int i = 0; i < 4; i++)
    {       
        for (int j = 0; j < 4; j++)
        {
            printf("%d",arr_180[i][j]);
        }
        printf("\n");
    }


    for (int i = 0; i < 4; i++)
    {       
        for (int j = 0; j < 4; j++)
        {
            arr_270[i][j]=arr_basic[j][3-i];
        }
        
    }
    printf("=== Basic Arr ===\n");
    for (int i = 0; i < 4; i++)
    {       
        for (int j = 0; j < 4; j++)
        {
            printf("%d",arr_270[i][j]);
        }
        printf("\n");
    }

    return 0;
    
}
