#include <stdio.h>

int main(){
    typedef struct {
        char name[20];
        char prop[10];
        int level;
    }Pokemon;

    Pokemon monster1={"피카츄","전기",5};
    Pokemon monster2={"파이리","불",2};
    Pokemon monster3={"꼬부기","물",11};

    Pokemon poke_list[3]={monster1,monster2,monster3};

    int flag;

    printf("1. 피카츄\t2. 파이리\t3. 꼬부기 (숫자입력): ");
    scanf("%d",&flag);

    printf("이름: %s\t타입: %s\t레벨: %d\n",poke_list[flag-1].name,poke_list[flag-1].prop,poke_list[flag-1].level);

    return 0;
}