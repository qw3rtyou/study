#include <stdio.h>

int main(){
    int size;
    scanf("%d",&size);

    int table[10002]={0};
    int tmp;

    for (int i = 0; i < size; i++)
    {
        scanf("%d",&tmp);
        table[tmp]++;
    }

    for (int i = 0; i < 10002; i++) {
        for (int j = 0; j < table[i]; j++) printf("%d\n",i);
    }
    
}