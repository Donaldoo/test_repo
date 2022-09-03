#include <stdio.h>
#include <stdlib.h>

int recursive_factorial(int n);

/**
 *main - entry point
 */
void main()
{
	int n;

	printf("Enter a positive number: ");
	scanf("%d", &n);

	printf("Factorial of number %d is %d\n", n, recursive_factorial(n));
}

/**
 * recursive_factorial - finds factorial of a number
 * @n: number
 *
 * Return: factorial of number n
 */
int recursive_factorial(int n)
{
	if (n == 1 || n == 0)
		return 1;
	else
		return (n * recursive_factorial(n - 1));
}
