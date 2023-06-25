/******************************************************************************

2) Escreva um algoritmo que solicite ao usuário que digite um número inteiro positivo e imprima na tela se ele é um número primo ou não.

*******************************************************************************/

#include <stdio.h>

int main()
{
    int n1, resto;
    
    printf("Digite um número inteiro positivo:");
    
    scanf("%i", &n1);
    
    resto=n1%2;
    
    if(resto== 0 && n1!=2)
    {
        printf("O número que foi digitado não é primo.");
    }

    else
    {
        printf("O número que voce digitou é primo.");
    }

    return 0;
}