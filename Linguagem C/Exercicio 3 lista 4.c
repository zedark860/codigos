
#include <stdio.h>

int main()
{
    
    int soma=0, n1=1, n2=0, i;
    
    printf("Número de 1 a 10 de acordo com a sequência de Fibonacci:\n");

    for(i=1;i<=10;i++)
    {
        
        soma=n1+n2;
        n1=n2;
        n2=soma;
        
        printf(" %i", soma);
        
    }
    
    return 0;
}
