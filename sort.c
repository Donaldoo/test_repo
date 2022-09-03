#include <stdio.h>
#include <stdlib.h>

void sort(int *array, int size);

/**
 * main - entry point
 */
void main()
{
	int array[] = {20, 17, 13, 32};
	int i, size = 4;

	sort(array, size);

	for (i = 0; i < size; i++)
		printf("%d ", array[i]);
	putchar('\n');
}

/**
 * sort - sorts an array using selection sort algorithm
 * @array: array to be sorted
 * @size: size of the array
 */
void sort(int *array, int size)
{
	int i, j, min, tmp;

	for (i = 0; i < size - 1; i++)
	{
		min = i;
		for (j = i + 1; j < size; j++)
		{
			if (array[j] < array[min])
				min = j;
		}
		if (min != i)
		{
			tmp = array[i];
			array[i] = array[min];
			array[min] = tmp;
		}
	}
}
