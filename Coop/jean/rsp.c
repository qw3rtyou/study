#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    char type[3][7] = { "가위", "바위", "보" };

    srand(time(NULL));

    int me;
    int com;

    while (1) {
        scanf("%d", &me);
        me = me % 3;
        com = rand() % 3;
        switch ((me - com + 3) % 3)
        {
        case 0:
            printf("YOU : %s\tCOM : %s\t비김\n", type[me], type[com]);
            break;
        case 1:
            printf("YOU : %s\tCOM : %s\t이김\n", type[me], type[com]);
            break;
        case 2:
            printf("YOU : %s\tCOM : %s\t짐\n", type[me], type[com]);
            break;
        default:
            break;
        }
    }

    return 0;
}