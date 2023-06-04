#include <stdio.h>

int main() {
    int data[24] = {
        0x49,
        0x60,
        0x67,
        0x74,
        0x63,
        0x67,
        0x42,
        0x66,
        0x80,
        0x78,
        0x69,
        0x69,
        0x7B,
        0x99,
        0x6D,
        0x88,
        0x68,
        0x94,
        0x9F,
        0x8D,
        0x4D,
        0xA5,
        0x9D,
        0x45,
    };

    int ans[24] = { 0, };

    for (int i = 0; i < 24; i++)
    {
        for (int j = 0; j < 200; j++)
        {
            if (data[i] == (j ^ i) + 2 * i)
            {
                ans[i] = j;
                break;
            }
        }
    }

    for (int i = 0; i < 24; i++)
    {
        printf("%c", ans[i]);
    }

}
