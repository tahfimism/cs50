#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input));
}

int convert(string input)
{
    // Get the length of the input string
    int len = strlen(input);

    // Base case:
    // If the string has only one character (e.g., "7"), return its integer value.
    // '0' has ASCII value 48, so to get the actual digit from a character like '7',
    // we subtract '0'. Example: '7' - '0' = 55 - 48 = 7
    if (len == 1)
        return (input[0] - '0');

    // Recursive case:
    // input[0] - '0' gives us the integer value of the first character
    // Multiply it by 10^(len-1) to shift it to the correct place value
    // Then recursively call convert on the remaining substring starting from input[1]
    // i.e., convert("234"), and add that result
    return (input[0] - '0') * pow(10, len - 1) + convert(&input[1]);
}
