#include <cs50.h>
#include <stdio.h>

//array length
const int N = 3;


int main(void)
{

    //declaring array
    int score[N];

    // loop for input
    for(int i = 0; i < N; i++)
    {
        score[i] = get_int("score: ");
    }

    // loop for sum
    int sum = 0;
    for(int i = 0; i < N; i++)
    {
        sum = sum + score[i];
    }

    // finding average
    float avg = (float) sum / (float) N;

    printf("average: %f \n", avg);
}
