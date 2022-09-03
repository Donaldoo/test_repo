#include <stdio.h>
#include <stdlib.h>

int search(int *array, int size, int value);

/**
 * main - entry point
 */
void main()
{
	int array[] = {20, 17, 13, 32};
	int value, size = 4;
	int result;

	printf("Enter value: ");
	scanf("%d", &value);

	result = search(array, size, value);

	if (result == -1)
		printf("Value not found\n");
	else
		printf("Value found at index %d\n", result);
}

/**
 * search - searches for a value in array
 * @array: array
 * @size: size of the array
 * @value: value to search
 *
 * Return: index of the value if found, -1 if not
 */
int search(int *array, int size, int value)
{
	int i;

	for (i = 0; i < size; i++)
	{
		if (array[i] == value)
			return (i);
	}
	return (-1);
}
