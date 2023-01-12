#include <stdio.h>

int main() {
    struct Point {
        int x;
		int y;
		struct asdf ptr;
    };
	
	struct asdf {
        int x;
		int y;
    };

    struct Point point1={1,5};
	struct Point point2={3,2};
	struct Point point3={4,3};
	
	point1.ptr.x=1;

    printf("point1.x = %d : point1.y = %d\n" , point1.x , point1.y);
	printf("point2.x = %d : point2.y = %d\n" , point2.x , point2.y);
	printf("point3.x = %d : point3.y = %d\n" , point3.x , point3.y);
    return 0;
}