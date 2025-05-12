#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{

    // taking inputs
    string text = get_string("Text: ");

    // declaring the variables
    int n = strlen(text);
    int nspace = 0; // no. of space
    int nw;         // no. of word
    int nsen = 0;   // no. of sentence
    int nl = 0;     // no. of letter

    // counting
    int i = 0;
    while (text[i] != '\0')
    {
        // counting blanks
        if (isblank(text[i]))
        {
            nspace++;
        }

        // cunting puntuation or sentence
        else if (text[i] == '!' || text[i] == '?' || text[i] == '.')
        {
            nsen++;
        }

        // counting letters
        else if (isalpha(text[i]))
        {
            nl++;
        }

        // incrementing
        i++;
    }

    // counting the no. of word
    nw = nspace + 1;

    // calculating L and S
    float L = ((float) (nl * 100)) / nw;
    float S = ((float) (nsen * 100)) / nw;

    // calculating index and rounding the value
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int rounded = round(index);

    // output
    if (rounded > 16)
    {
        printf("Grade 16+\n");
    }
    else if (rounded < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", rounded);
    }
}
