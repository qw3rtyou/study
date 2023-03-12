#include <stdio.h>
int main (void){
    int sum,num;
    scanf("%d\n%d",&sum,&num);

    int a,b;
    int tmp=0;
        
    for (int i = 0; i < num; i++)
    {
        scanf("%d %d",&a,&b);
        tmp+=a*b;
    }
    
    if (sum==tmp)
    {
        printf("Yes");
    } else {
        printf("No");
    }
    

    return 0;
}