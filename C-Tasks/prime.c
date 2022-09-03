#include <stdio.h>
#include <stdlib.h>

int is_prime(int n);

/**
 * main - entry point
 *
 * Return: 0
 */
int main()
{
	int n, result;

	printf("Enter a number: ");
	scanf("%d", &n);

	result = is_prime(n);

	if (result == 0)
		printf("%d is a prime number\n", n);
	else
		printf("%d is not a prime number\n", n);

	return 0;
}

/**
 * is_prime - check if a number is prime or not
 * @n: number to check
 *
 * Return: 0 if prime, 1 if not
 */
int is_prime(int n)
{
	int i;

	for (i = 2; i < n / 2; i++)
	{
		if (n % i != 0)
			continue;
		else
			return 1;
	}
	return 0;
}
