#include<stdio.h>
#include<cs50.h>

//seach for a int number among a array thru linear search
int main (void)
{
    int coins[] = {5, 25, 100, 50, 70};

    int n = get_int("type ur number: ");
    for (int i = 0; i <5; i++)
    {
        if (coins[i] ==n)
        {
            printf("found \n");
            return 0;
        }
    }
    printf("not found");
    return 1;
}
