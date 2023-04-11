#include <stdio.h>
int main (){
    int num;
    int info[51][2];
    int scoreBoard[51]={0};

    scanf("%d",&num);

    for (int i = 0; i < num; i++)
        scanf("%d %d",info[i][0],info[i][1]);
    
    int bestBig=info[0][0]+info[0][1];
    int bestWeight;
    int bestHeight;
    int bestIdx=0;
    int tmpBig;
    int rank=1;
    
    while(1){
        for (int i = 0; i < num; i++)
        {
            tmpBig=info[i][0]+info[i][1];
            if (tmpBig>bestBig) {
                bestBig=tmpBig;
                bestIdx=i;
            }
        }
        
        bestWeight=info[bestIdx][0];
        bestHeight=info[bestIdx][1];

        for (int i = 0; i < num; i++)
        {
            
        }
        
    }
    

    return 0;
}