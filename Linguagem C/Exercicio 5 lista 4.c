#include <stdio.h>

int main()
{
    int i, n, tabuada;

    printf("TABELA DA TABUADA DE 1 A 10:\n\n");

    for(i=1;i<=10;i++)
    {
        printf("Tabuada de %i:\n\n", i);

        for(n=1;n<=10;n++)
        {
            
            tabuada=i*n;
            
            printf(" %ix%i=%i.\n\n", i, n, tabuada);
            
        }
       
    }
    
    return 0;
}
