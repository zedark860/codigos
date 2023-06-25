#include <stdio.h>

int main()
{
    char opcao;
    
    do
    {
        printf("5 é maior do que 10? Digite S ou N:");
        
        scanf(" %c", &opcao);
        
        if(opcao== 'S' || opcao== 's')
        {
            
            printf("Está errado, pois 5 não é maior que 10!");
            
            return 0;
            
        }
        
        else if(opcao== 'N' || opcao== 'n')
        {
            
            printf("Está correto!");
            
            return 0;
            
        }
        
        
    }

    while(opcao!= 'S' || 's' || opcao!= 'N' || 'n');

    return 0;
}