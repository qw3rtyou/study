#include <stdio.h>
#include <stdlib.h>

int main()
{
    char s[80];
    FILE *fd = fopen("/flag.txt","r");
    fgets(s, 80, fd);
    printf("%s\n", s);
    fclose(fd);
    return 0;
}
