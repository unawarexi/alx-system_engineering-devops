#include "main.h"
/**
*_memset -   fills memory with a const  byte
*@s: pointer block of memory to fill
*@b: character value to be  set
*@n: bytes assigned to  memory
*Return: dest
*/

char *_memset(char *s, char b, unsigned int n)

{
unsigned int i;

/*using for loops*/
for (i = 0; i < n; i++)
{
*(s + i) = b;

}

return (s);
}
