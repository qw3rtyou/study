#include <stdio.h>

int main() {
    int cover_num;
    int paper[100][100]={0};
    int x,y;

    scanf("%d",&cover_num);

    for (int  i = 0; i < cover_num; i++) {

        scanf("%d %d",&x,&y);
        
        for (int j = x; j < ((100<x+10)?100:x+10) ; j++)
        {
            for (int k = y; k < ((100<y+10)?100:y+10) ; k++)
            {
                paper[j][k]=1;
            }
        }
    }
    
    int cnt=0;

    for (int i = 0; i < 100; i++)
    {
        for (int j = 0; j < 100; j++)
        {
            if (paper[i][j]==1) cnt++;
        }
    }

    printf("%d",cnt);

    return 0;
}