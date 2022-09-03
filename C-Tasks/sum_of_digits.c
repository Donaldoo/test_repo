#include <stdio.h>
#include <stdlib.h>

int sum_of_digits(int n);

/**
 * main - entry point
 *
 * Return: 0
 */
int main()
{
	int n;

	printf("Enter a number: ");
	scanf("%d", &n);

	printf("Sum of digits of number %d is %d\n", n, sum_of_digits(n));

	return 0;
}

/**
 * sum_of_digits - finds the sum of digits of a number
 * @n: number
 *
 * Return: sum of digits
 */
int sum_of_digits(int n)
{
	int sum = 0, remainder;

	while (n > 0)
	{
		remainder = n % 10;
		sum += remainder;
		n = n / 10;
	}
	return (sum);
}
