#include <stdio.h>

int main()
{
    
    int n, cont=0, multi, fim=0, inc;
    
    printf("Digite o número da tabuada e os início da mesma e final:");
    
    scanf(" %i %i %i", &n, &cont, &fim);
    
    fim=fim - 1;
    
    cont=cont - 1;
    
    while(cont<=fim)
    {
        
        cont=cont + 1;
        
        multi=n*cont;
        
        printf("%ix%i=%i\n", n, cont, multi);
        
    }

    return 0;
}