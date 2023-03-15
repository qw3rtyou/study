#include <stdio.h>
int main (void){
    int num;
    int max=-1;
    int tmp;
    int sum=0;

    scanf("%d",&num);

    for (int i = 0; i < num; i++)
    {
        scanf("%d",&tmp);
        max=(max<tmp)?tmp:max;
        sum+=tmp;
    }

    printf("%f",((float)sum/num)*(float)100/max);
    
    return 0;
}