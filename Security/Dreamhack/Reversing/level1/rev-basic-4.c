#include <stdio.h>

int main() {
    int data[28] = {
        0x24, 0x27, 0x13, 0xC6, 0xC6, 0x13, 0x16, 0xE6, 0x47, 0xF5, 0x26, 0x96, 0x47, 0xF5, 0x46, 0x27, 0x13, 0x26, 0x26, 0xC6, 0x56, 0xF5, 0xC3, 0xC3, 0xF5, 0xE3, 0xE3,
    };

    int ans[28] = { 0, };

    for (int i = 0; i < 28; i++)
    {
        for (int j = 0; j < 1000; j++)
        {
            if (((16 * j) & 0xF0 | (j >> 4)) == data[i])
            //& 0xF0해주는 이유는 크기 벗어나는걸 컽하기 위함
            //if (((16 * j) & 0xF0 | (j >> 4)) == data[i])
            {
                ans[i] = j;
                break;
            }
        }
    }

    for (int i = 0; i < 28; i++)
    {
        printf("%c", ans[i]);
    }

}
