#include <stdio.h>
#include <stdlib.h>

int largest_three(int a, int b, int c);

/**
 * main - entry point
 * 
 * Return: Largest number
 */
int main()
{
	int a, b, c;

	printf("Enter first number: ");
	scanf("%d", &a);
	printf("Enter second number: ");
	scanf("%d", &b);
	printf("Enter third number: ");
	scanf("%d", &c);
	
	printf("Largest number is: %d\n", largest_three(a, b, c));

	return 0;
}

/**
 * largest_three - find the largest of 3 given numbers
 * @a: num 1
 * @b: num 2
 * @c: num 3
 * 
 * Return: Largest number
 */
int largest_three(int a, int b, int c)
{
	if (a > b && a > c)
		return (a);
	if (b > a && b > c)
		return (b);
	if (c > a && c > b)
		return (c);
}
