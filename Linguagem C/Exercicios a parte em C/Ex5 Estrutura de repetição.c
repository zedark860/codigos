//Faça	 um	 programa	 em	 C	 que	 receba	 a	 idade	 de	 10	 pessoas	 e	 mostre	 quantas	são	maiores	que	18	anos.	

#include <stdio.h>

int main()
{
    
    int n, i, soma=0;
    
    printf("Digite a idade de 10 pessoas:\n");
    
    for(i=1;i<=10;i++)
    {
        
        printf("Digite a idade %i:\n", i);
        
        scanf(" %i", &n);
        
        if(n>=18)
        {
            
            soma=soma+1;
            
        }
        
    }

    printf("A quantidade que são maiores de 18 anos é: %i",  soma);

    return 0;
}