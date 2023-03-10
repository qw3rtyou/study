#include <stdio.h>
int main (void){
    int one,two;
    scanf("%d\n%d",&one,&two);

    int three, four, five, six;

    three=one*(two%10);
    four=one*(two%100/10);
    five=one*(two/100);

    six=100*five+10*four+three;

    printf("%d\n%d\n%d\n%d",three,four,five,six);

    return 0;
}