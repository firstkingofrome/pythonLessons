#include <stdio.h>

/*
 * gcc -O3 whatIsCompile.c for optimization
 * gcc -S whatIsCompile.c for assembly
 * */


int main() {
    int x=3;
    int y=2;
    //float q = 1.0;
    //float w = 1.0;
    y= x*y*x*y;
    printf("y=%i\n",y);
    //char a='a';
    //printf("print this variable %c",a);
    return 0;

}
