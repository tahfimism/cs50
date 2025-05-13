#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
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
        if (!isalpha(key_s[i]))
        {
            printf("put only aplhabets as key \n");
            return 1;
        }
    }

    // checking if theres 26 letter
    if (lenk != 26)
    {
        printf("not 26 letters\n");
        return 1;
    }

    // checking if any leter is repeated
    for (int l = 0; l < 26; l++)
    {

        for (int j = l + 1; j < 26; j++)
        {
            if (tolower(key_s[l]) == tolower(key_s[j]))
            {
                printf("theres a common letter");
                return 1;
            }
        }
    }

    // taking input texts
    string text = get_string("plaintext:");
    int lens = strlen(text);

    // cipher

    printf("ciphertext: ");
    int c;

    for (int k = 0; k < lens; k++)
    {
        if (islower(text[k]))
        {
            c = text[k] - 97;
            printf("%c", tolower(key_s[c]));
        }
        else if (isupper(text[k]))
        {
            c = text[k] - 65;
            printf("%c", toupper(key_s[c]));
        }
        else
        {
            printf("%c", text[k]);
        }
    }
    printf("\n");
    return 0;
}
