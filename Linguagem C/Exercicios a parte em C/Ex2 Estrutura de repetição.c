//Faça	 um	 programa	em	 C	 (com	a	estrutura	 do...while)	 que	leia	 20	 valores	inteiros	e:	
//–	Encontre	e	mostre	o	maior	valor;	
//–	Encontre	e	mostre	o	menor	valor;	
//–	Calcule	e	mostre	a	média	dos	números	lidos;	

#include <stdio.h>

int main()
{
    
    int n, maior, menor, soma, inc=1;
    float media;
    
    printf("Digite 20 valores inteiros positivos:\n");
    
    do
    {
        
        printf("Digite o número %i:\n", inc);
        
        scanf(" %i", &n);
        
        
        if(n>maior)
        {
            maior=n;
        }
     
        else if(n<menor)
        {
            menor=n;
        }
        
        soma=soma+n;
        media=soma/inc;
        
        inc++;
        
    }
    while(inc<=20);

    printf("Maior número=%i\n", maior);

    printf("Menor número=%i\n", menor);
    
    printf("Valor da média=%f\n", media);
    
    return 0;
}