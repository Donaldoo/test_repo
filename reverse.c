#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *reverse(char *text);

/**
 * main - entry point
 *
 * Return: 0
 */
int main()
{
	char text[100];

	printf("Enter string: ");
	scanf("%s", text);

	printf("Reverse string is: %s\n", reverse(text));

	return 0;
}

/**
 * reverse - reverses a string
 * @text: string to be reversed
 *
 * Return: reversed string
 */
char *reverse(char *text)
{
	int i = 0, len;
	char tmp;

	len = strlen(text);

	for (i = 0; i < len / 2; i++)
	{
		tmp = text[i];
		text[i] = text[len - i - 1];
		text[len - i - 1] = tmp;
	}
	return (text);
}
