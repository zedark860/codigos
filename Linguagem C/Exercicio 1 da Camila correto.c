// Escreva um algoritmo que solicite ao usuário que digite três números e imprima na tela o maior valor entre eles.//

#include <stdio.h>

int main()
{
    
    int n1,n2,n3,i,maior;
    
    printf("Digite 3 números para saber qual deles é o maior:\n");
    
    scanf("%i %i %i", &n1, &n2, &n3);

    if(n1>n2 && n1>n3)
    {
        
        maior=n1;
        
        printf("O número maior é %i.", maior);
        
    }
    
    else if(n2>n1 && n2>n3)
    {
        
        maior=n2;
        
        printf("O número maior é %i.", maior);
        
    }
    
        if(n3>n1 && n3>n2)
        {
            
            maior=n3;
            
            printf("O número maior é %i", maior);
            
        }

    return 0;
}