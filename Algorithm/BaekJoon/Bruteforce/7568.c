#include <stdio.h>

int main() {
	int n;

	int weight[51] = { 0 };
	int height[51] = { 0 };

	scanf("%d", &n);
    
    int tmp=0;

	for (int i = 0; i < n; i++) scanf("%d %d", &weight[i], &height[i]);

	for (int i = 0; i < n; i++) {
		tmp = 0;
		for (int j = 0; j < n; j++) {
			if (weight[i] < weight[j] && height[i] < height[j]) tmp++;
		}
		printf("%d ", tmp + 1);
	}
	return 0;
}