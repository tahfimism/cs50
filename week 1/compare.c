
// compare between two integer

#include <stdio.h>
#include <cs50.h>


int main (void)
{

    int x = get_int("X=? ");
    int y = get_int("y=? ");

    if (x>y)
    {
        printf("x is larger\n");
    }
    else if (x<y)
    {
        printf("y is larger\n");
    }
    else
    {
        printf("x is equal to y\n");
    }


}
