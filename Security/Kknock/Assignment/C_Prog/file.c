#include <stdio.h>

int main(){
    FILE *fp;
    fp=fopen("./file.txt","w");

    fputs("이름 : 최정원\n학년: 2학년\n학과: 컴퓨터공학부\n\n오늘부로 C스터디 끝~",fp);

    fclose(fp);
}