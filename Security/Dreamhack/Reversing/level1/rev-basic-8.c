#include <stdio.h>

int main() {
    int data[32] = {
        0xAC, 0xF3, 0x0C, 0x25, 0xA3, 0x10, 0xB7, 0x25, 0x16, 0xC6, 0xB7, 0xBC, 7,0x25, 2, 0xD5, 0xC6, 0x11, 7, 0xC5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    };

    int ans[21] = { 0, };

    for (int i = 0; i < 21; i++)
    {
        for (int j = 0; j < 200; j++)
        {
            if ( (-5 * j) != data[i] ) {
                ans[i] = j;
            }
        }

    }

    for (int i = 0; i < 21; i++)
    {
        printf("%c", ans[i]);
    }


    return 0;
}


    