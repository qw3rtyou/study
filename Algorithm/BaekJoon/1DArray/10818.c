#include <stdio.h>
#include <math.h>
#define max(a,b) (a>b)?a:b
#define min(a,b) (a<b)?a:b

int main (void){
    int array[1000000];
    int num;

    scanf("%d",&num);
    
    for (int i = 0; i < num; i++)
    {
        scanf("%d",array+i);
    }
    
    int max_num=-INFINITY;
    int min_num=INFINITY;

    for (int i = 0; i < num; i++)
    {
        min_num=min(min_num,*(array+i));
        max_num=max(max_num,*(array+i));
    }

    printf("%d %d", min_num, max_num);
    
    return 0;
}