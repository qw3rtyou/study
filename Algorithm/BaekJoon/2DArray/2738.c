#include <stdio.h>
int main (void){
    int n,m;
    int matrix[100][100];
    int tmp;

    scanf("%d %d",&n,&m);

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%d",&tmp);
            matrix[i][j]=tmp;
        }      
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%d",&tmp);
            matrix[i][j]+=tmp;
        }      
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            printf("%d ",matrix[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}