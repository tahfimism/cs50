#include <stdio.h>
#include <cs50.h>
#include <string.h>

// search string from a array with linear search
int main(void)
{
    string animals[] = {"cat" , "dog", "tiger", "lion"};

    string name = get_string("ur animal: ");

    for (int i = 0; i < 4; i++)
    {
        if ( strcmp(animals[i], name) == 0)
        {
            printf("found \n");
            return 0;
        }
    }

    printf(" not found \n");
    return 1;
}
