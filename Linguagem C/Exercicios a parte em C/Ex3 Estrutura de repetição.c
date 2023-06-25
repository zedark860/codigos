//Faça	 um	 programa	 em	 C	 (utilize	 a	 estrutura	 for)	 que	 leia	 10	 valores	inteiros	e:	
//•	Encontre	e	mostre	o	maior	valor		
//•	Encontre	e	mostre	o	menor	valor		
//•	Calcule	e	mostre	a	média	dos	números	lidos

#include <stdio.h>

int main()
{
    
    int n, i, maior, menor, acumulador=0, media;
    
    printf("Digite 10 números inteiros positivos:\n");
    
    for(i=1;i<=5;i++)
    {
        
        printf("Digite o número %i:\n", i);
        
        scanf(" %i", &n);
    
        if(n>maior)
        {
            maior=n;
        }
        
        else if(n<menor)
        {
            menor=n;
        }
        
        acumulador=acumulador+n;
        media=acumulador/i;
        
    }
    
    printf("Maior número: %i\n", maior);
    printf("Menor número: %i\n", menor);
    printf("Media dos 10 valores: %i\n", media);
    
    
    return 0;
}