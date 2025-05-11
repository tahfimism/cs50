#include <cs50.h>
#include <stdio.h>
#include <math.h>

int get_positive_input(void);

int main(void)
{

    //taking input
    //long x = get_long("Number: ");
    long x = 378282246351235;

    long k;
    long sum1 = 0;
    long sum2 = o;
    int p1 = 1;
    int p2 = 0;

    //if invalid
    do
    {
        k = (x / (long)pow(10,p1)) % 10;
        sum1 = sum1 + k*10;
        p1 = p1+2;
    }
    while(k > 1);

    //if invalid
    do
    {
        k = (x / (long)pow(10,p2)) % 10;
        sum2 = sum2 + k*10;
        p2 = p2+2;
    }
    while(k > 1);


    //adding
    long validity = sum1*2 + sum2 ;

    //checking validity
    if(validity % 10 == 0)
    {
        printf("valid ");

        if( x/pow(10,15) == 0)
        {
            printf("american express");
        }

        else if(x/pow(10,16) == 0)
        {
            printf("visa");
        }
        else
        {
            printf("invalid ");
        }
    }
    else
    {
        printf("invalid");
    }

    //if valid
    printf("%li \n", validity);


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
