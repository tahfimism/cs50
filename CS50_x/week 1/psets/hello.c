#include <cs50.h>
#include <stdio.h>

int main()
{
    string ans = get_string("What's your name? ");
    printf("hello, %s\n", ans);
}
