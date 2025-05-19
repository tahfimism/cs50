#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int count(string s);


int p[26] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int main (void)
{
    //taking inputs
    string s1 = get_string("player 1: ");
    string s2 = get_string("player 2: ");

    //compute
    int sum1 = count(s1);
    int sum2 = count(s2);

    //comparing
    if(sum1 > sum2)
    {
        printf("Player 1 wins! \n");
    }
    else if (sum2 > sum1)
    {
        printf("Player 2 wins! \n");
    }
    else
    {
        printf("Tie! \n");
    }

}




//computing
int count(string s)
{
    int sum = 0;
    for(int i = 0, n = strlen(s); i < n; i++)
    {
        if (isalpha(s[i]))
        {
        int x = toupper(s[i]) - 'A';
        sum = sum + p[x];
        }
    }
    return sum;
}
