#include <stdio.h>

int main() {
	int score[1002];
	int c,n;
    int count=0;
	double avg=0;

	scanf("%d", &c);

	for (int i = 0; i < c; i++) {
		scanf("%d", &n);
		avg=0;

		for (int j = 0; j < n; j++) {
			scanf("%d", &score[j]);
			avg+=score[j];
		}

		avg/=n;
		count=0;

		for (int j = 0; j < n; j++) {
			if (score[j] > avg) ++count;
		}

		printf("%.3f\n", (100.0*count)/n);
	}

	return 0;
}