#include <stdio.h>

int main()
{
    
    int fim, cont=1;
    
    printf("Digite o último número para imprimir:");
    
    scanf(" %i", &fim);
    
    printf("1");
    
    while(cont <= fim)
    {
        
        cont=cont + 2;
        
        printf(" %i", cont);
        
    }
    
    return 0;
}