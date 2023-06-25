/******************************************************************************
4)
*******************************************************************************/

#include <stdio.h>
#include <math.h>

int main()
{
    int n, raiz;
    
    printf("Digite um número inteiro positivo:");
    
    scanf(" %i", &n);
    
    raiz=sqrt(n);
    
    if(n == raiz*raiz)
        printf("O número digitado é um quadrado perfeito.");
        
    else
        printf("O número digitado não é um quadrado perfeito");
    
    return 0;
}