#include <cs50.h>
#include <math.h>
#include <stdio.h>

long get_positive_input(void);

int main(void)
{
    // take input
    long x = get_positive_input();

    int n = 0;
    long temp = x;
    int sum1 = 0;
    int sum2 = 0;

    // checksum loop
    do
    {
        int digit = temp % 10;
        temp = temp / 10;

        // checking from second last
        if (n % 2 == 1)
        {
            digit = digit * 2;
            sum1 = sum1 + digit / 10 + digit % 10;
        }
        // checking from last
        else
        {
            sum2 = sum2 + digit;
        }
        n++;
    }
    while (temp > 0);

    // suming the sums
    int sum = sum1 + sum2;

    // checking if invalid
    if (sum % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }

    // ✅ Card is valid. Now check card type.

    long first_2 = x;
    while (first_2 >= 100)
    {
        first_2 /= 10;
    }

    // finding first digit
    int first_1 = first_2 / 10;

    if (n == 15 && (first_2 == 34 || first_2 == 37))
    {
        printf("AMEX\n");
    }

    else if ((n == 13 || n == 16) && first_1 == 4)
    {
        printf("VISA\n");
    }

    else if (n == 16 &&
             (first_2 == 51 || first_2 == 52 || first_2 == 53 || first_2 == 54 || first_2 == 55))
    {
        printf("MASTERCARD\n");
    }

    else
    {
        printf("INVALID\n");
    }
}

// positive input
long get_positive_input(void)
{
    long n;
    do
    {
        n = get_long("Number: ");
    }
    while (n < 1);
    return n;
}
