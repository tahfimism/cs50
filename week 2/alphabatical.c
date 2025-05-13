#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

//check if a string is alphabatical or not
int main(void)
{

    //taking inputs
    string text = get_string("give the input: ");

    //using x to determine if its aplhabatical or not
    // initially x=1 that its alphabatical
    // if x turns 0, means its not alphabatical
    int x = 1;

    //loop to access the chars individually
    // i < n-1 --- so the loop doesnt overpass with i+1
    for(int i = 0, n = strlen(text); i < n-1; i++)
    {
        int next = i+1;
        //checking order with ascii numbers
        if( text[i] > text[i+1])
        {
            x = 0;
            break;
        }

    }

    //giving outputs
    if (x == 0)
    {
        printf("no \n");
    }
    else
    {
        printf ("yes \n");
    }
}
