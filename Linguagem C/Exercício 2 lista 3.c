/******************************************************************************
Solicite ao usuário que digite uma quantidade x de números e realizar a soma e média dos números digitados.
O usuário deverá escolher a quantidade de números que são digitados , e além disso deverá digitar os números para realizar a soma e média.
*******************************************************************************/

#include <stdio.h>

int main()
{
    
    float soma=0, num;
    
    int i, n;
    
    printf("Digite a quantidade de números para serem feitos a soma e depois média:");
    
    scanf(" %i", &n);
    
    for(i=1;i<=n;i++)
    {
        
        printf("Digite o a média %i:\n", i);
        
        scanf(" %f", &num);
        
        soma=(soma+num);
        
    }
    
    soma=soma/n;
    
    printf("O resultado da média é %f", soma);

    return 0;
}
