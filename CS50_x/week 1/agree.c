#include <stdio.h>
#include <cs50.h>


int main (void)
{

    char c = get_char("do u agree? y/n: ");

    if(c == 'y' || c=='Y')
    {
        printf("agreed\n");
    }
    else if(c == 'n' || c == 'N')
    {
        printf("disagreed\n");
    }
    else
    {
        printf("invalid input\n");
    }

}
