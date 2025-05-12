#include <cs50.h>
#include <stdio.h>

int get_positive_input(void);

int main(void)
{
    // take input
    int i = get_positive_input();

    // finding out no. of coins
    int q25 = i / 25;
    int q10 = (i - 25 * q25) / 10;
    int q5 = (i - 25 * q25 - 10 * q10) / 5;
    int q1 = (i - 25 * q25 - 10 * q10 - 5 * q5) / 1;

    // printing output
    int cash = q25 + q10 + q5 + q1;
    printf("%i \n", cash);
}

// positive input
int get_positive_input(void)
{
    int n;
    do
    {
        n = get_int("Change owed: ");
    }
    while (n < 1);
    return n;
}
