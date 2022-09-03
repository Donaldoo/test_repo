#include <stdio.h>
#include <stdlib.h>

void temp_info(int *temps);

/**
 * main - entry point
 *
 * Return: 0
 */
void main()
{
	int temp[] = {32, 19, 41, 25, 17, 14, 22, '\0'};
	int low, high, amplitude;

	temp_info(temp);
}

/**
 * temp_info - find the lowest, highest and amplitude of temps in an array
 * @temps: array containing all temperatures
 */
void temp_info(int *array)
{
	int i, low, high, amplitude;

	low = high = array[0];

	for (i = 0; array[i]; i++)
        {
                if (array[i] > high)
                        high = array[i];

		if (array[i] < low)
                        low = array[i];
	}
	amplitude = high - low;

	printf("Lowest temp is: %d\nHighest temp is: %d\nAmplitude is: %d\n",
			low, high, amplitude);
}
