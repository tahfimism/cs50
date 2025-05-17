// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

string replace(string word);

int main(int argc, string argv[])
{
    if(argc != 2)
    {
        printf("usage: ./no-vowels.c word");
        return 1;
    }

    printf("%s\n", replace(argv[1]));
}

string replace(string word)
{
    int n = strlen(word);
    string s = word;
    string replace = "6bcd3fgh1jklmn0pqrstuvwxyz";

    for(int i = 0; i < n; i++)
    {
        if(islower(s[i]))
        {
        int c = s[i] - 'a';
        s[i] = replace[c];
        }
        else if (isupper(s[i]))
        {
            int c = tolower(s[i]) - 'a';
            s[i] = toupper(replace[c]);
        }
    }
    return s;
}
