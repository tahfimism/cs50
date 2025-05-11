#include <stdio.h>
#include <cs50.h>


// prints a mario pyramid

void print_row(int n);

int main (void)
{

    int n= 3;
    for ( int row=0; row < n; row++)
    {
       print_row(n);
    }



}


void print_row(int n)
{
    for (int r=0; r < 3; r++)
        {
            printf("#");
        }
        printf("\n");
}
