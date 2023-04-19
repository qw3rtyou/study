#pragma warning(disable: 4996)
#pragma warning(disable: 6031)
#include <stdio.h>

void selectionSort(int arr[], int size);
void swap(int*, int*);

int main() {
	int arr[1000] = { 0 };
	int size;

	scanf("%d", &size);
	for (int i = 0; i < size; i++) scanf("%d", &arr[i]);

    selectionSort(arr, size);

	for (int i = 0; i < size; i++) printf("%d\n", arr[i]);
}

void selectionSort(int arr[], int size) {
	int tmp,i,j;
	for (i = 0; i < size-1; i++) {
		tmp = i;
		for (j = i + 1; j < size; j++)
			if (arr[j] < arr[tmp])
				tmp = j;
		
		swap(&arr[i], &arr[tmp]);
	}
}

void swap(int* a, int* b) {
	int tmp;
	tmp = *a;
	*a = *b;
	*b = tmp;
}