#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc,char **argv){
	char cmd[100];
	
	printf("count of arg = %d\n",argc);
	printf("%s, %s",argv[0],argv[1]);
	strcpy(cmd,argv[1]);
	
	system(cmd);
}
