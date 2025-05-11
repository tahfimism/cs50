#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    // Loop through all arguments starting from argv[1]
    for (int i = 1; i < argc; i++)
    {
        // Loop through each character in the current argument
        for (int j = 0, n = strlen(argv[i]); j < n; j++)
        {
            printf("%c", toupper(argv[i][j]));
        }

        // Print a space between words (optional)
        if (i < argc - 1)
        {
            printf(" ");
        }
    }

    printf("\n");
}
