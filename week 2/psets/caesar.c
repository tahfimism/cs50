#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    // checking for invalid argument number
    if (argc != 2)
    {
        printf("put key after \n");
        return 1;
    }

    // checking if each character of key is digit
    string key_s = argv[1];
    int lenk = strlen(key_s);

    for (int i = 0; i < lenk; i++)
    {
        if (!isdigit(key_s[i]))
        {
            printf("put digits as key \n");
            return 1;
        }
    }

    // converting string to int for key
    int key = atoi(argv[1]);

    // taking plain text input
    string text = get_string("plaintext: ");
    int len = strlen(text);

    // encryption ----------
    printf("ciphertext: ");
    for (int j = 0; j < len; j++)
    {
        if (islower(text[j]))
        {
            char c = text[j];
            c = ((c - 97 + key) % 26) + 97;
            printf("%c", c);
        }

        else if (isupper(text[j]))
        {
            char c = text[j];
            c = ((c - 65 + key) % 26) + 65;
            printf("%c", c);
        }
        else
        {
            printf("%c", text[j]);
        }
    }
    printf("\n");
    return 0;
}
