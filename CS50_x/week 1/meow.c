
#include <cs50.h>
#include <stdio.h>

// made up fuction's prototype
void meow(int n);
int get_positive_input(void);

// main code
int main(void)
{

    int times = get_positive_input();
    meow(times);  
}  




// funttion stock
int get_positive_input(void)
{
    int n;
    do
    {
        n = get_int("how many times? ");
    }
    while (n < 1);
    return n;
}




void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("meaow\n");
    }
}
