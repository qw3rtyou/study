#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int main() {
    srand(time(NULL));

    while (1) {
        switch (rand() % 5)
        {
        case 0:
            printf("도\n");
            break;
        case 1:
            printf("개\n");
            break;
        case 2:
            printf("걸\n");
            break;
        case 3:
            printf("윷\n");
            break;
        case 4:
            printf("모\n");
            break;
        default:
            break;
        }
        
        Sleep(1000);
    }

    return 0;
}