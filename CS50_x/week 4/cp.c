#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

typedef uint8_t BYTE;

// use terminal like -- ./cp.c source.filetype destination.filetype
int main(int argc, char *argv[])
{
    if(argc != 3)
    {
        printf("./cp.c source.filetype destination.filetype \n");
        return 1;
    }

    FILE *src = fopen(argv[1] , "r");
    FILE *dst = fopen(argv[2] , "w");

    BYTE b ;

    while (fread(&b, sizeof(b), 1, src) != 0)
    {
        fwrite(&b, sizeof(b), 1, dst);
    }

    fclose(src);
    fclose(dst);
    return 0;
}
