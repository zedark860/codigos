#include <stdio.h>

int main()
{
   
   char opcao;
   
   int n1,n2,n3,n4,soma,divisao,conta;
   
    do
    {
     printf("Digite S ou N para efetuar o cálculo:");  
       
     scanf(" %c", &opcao);  
       
     if(opcao== 'S') { 
       
     printf("Ok digite 4 números:");
       
     scanf("%i %i %i %i", &n1, &n2, &n3, &n4); 
     
     soma=n1+n2+n3+n4;
     
     divisao=n3/n1;
     
     conta=soma*divisao;
     
     printf("O resultado de suas contas de soma=%i,divisao=%i,multiplicação de ambas as contas=%i.", soma, divisao, conta);
	return 0;
     }
   
{
    if(opcao== 'N') {
    
    printf("Ok, o programa irá desligar!");
    
    return 0;
    }    
}
    
    }
           while(opcao!= 'S'||'N'); {
            return 0;
   }
    return 0;
}