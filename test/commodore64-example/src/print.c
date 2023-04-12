#include "print.h"
#include <stdio.h>

void print()
{
    const char *cur = "HELLO, PUTCHAR!\n";
    while (*cur)
        __putchar(*cur++);
}