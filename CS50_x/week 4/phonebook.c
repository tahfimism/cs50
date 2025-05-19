#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    // opening the phonebook
    FILE *book = fopen("phonebook.csv", "a");
        if (file == NULL) return 1;

    // to ask if we want to put another contact
    char repeat = 'y';

    while (repeat == 'y')
    {
        // getting inputs
        char *name = get_string("name: ");
        char *number = get_string("number: ");

        // printing the contact
        fprintf(book, "%s, %s\n", name, number);

        // asking if we wanna put another contact
        repeat = get_char("another? y/n ");
    }

    fclose(book);
}
