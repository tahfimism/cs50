#include <cs50.h>
#include <stdio.h>

void print_row(int n);
void print_space(int n);
int get_positive_input(void);

int main(void)
{
    // Prompt the user for the pyramid's height
    int n = get_positive_input();

    // configuring relation of no. of space and # with height
    int sp = n - 1;
    int row = 1;

    for (int h = 0; h < n; h++)
    {
        // left side
        print_space(sp);
        print_row(row);

        // middle space
        printf("  ");

        // right side
        print_row(row);

        // moving to next line
        printf("\n");

        // decrease no. of space per row
        sp = sp - 1;

        // increase no. of # per row
        row = row + 1;
    }
}

// print #
void print_row(int n)
{

    for (int r = 0; r < n; r++)
    {
        printf("#");
    }
}

// print space function
void print_space(int n)
{
    for (int s = n; s > 0; s--)
    {
        printf(" ");
    }
}

// positive input
int get_positive_input(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);
    return n;
}
