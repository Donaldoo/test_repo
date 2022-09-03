#include <stdio.h>
#include <stdlib.h>

int count_letter(char *text, char letter);

/**
 * main - entry point
 *
 * Return: 0
 */
int main()
{
	char *array;
	char letter;
	int result;

	printf("Enter string: ");
	scanf("%[^\n]s", array);

	getchar();

	printf("Enter character: ");
	scanf("%c", &letter);

	result = count_letter(array, letter);

	printf("There are %d characters in array\n", result);

	return 0;
}


/**
 * count_letter - counts how many times a single char is found in an array
 * @text: array
 * @letter: letter to count
 *
 * Return: counter
 */
int count_letter(char *text, char letter)
{
	int i, count = 0;

	for (i = 0; text[i] != '\0'; i++)
	{
		if (text[i] == letter)
			count++;
	}
	return (count);
}
