#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

// find exponenets of 2
int main(void)
{
    //takes input
    int times = get_int("how many steps: ");

    //declare arraay
    int n[times];

    //initial term
    int x = 1;

    //loop
    for(int i=0; i < times; i++)
    {
        n[i] = x;
        x = x * 2;
        printf("%i \n", n[i]);
    }
}
