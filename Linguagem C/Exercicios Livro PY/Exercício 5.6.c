#include <stdio.h>

int main()
{
    
    int n, cont=0, multi;
    
    printf("Digite um número para fazer a tabuada:");
    
    scanf(" %i", &n);
    
    while(cont<=9)
    {
        
        cont=cont + 1;
        
        multi=n*cont;
        
        printf("%ix%i=%i\n", n, cont, multi);
        
    }

    return 0;
}