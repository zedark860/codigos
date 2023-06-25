/******************************************************************************

4) Calcule a média aritmética das 3 notas de um aluno e mostre, além do valor da média, uma mensagem de "Aprovado", caso a média seja igual ou superior a 6, ou a mensagem "reprovado", caso contrário.

*******************************************************************************/

#include <stdio.h>

int main()
{
    float n1,n2,n3,media;
    
    printf("Digite 3 números para saber sua média e se você foi aprovado:\n");
    
    scanf("%f %f %f", &n1, &n2, &n3);
    
    media=(n1+n2+n3)/3;
    
    if(media>=6)
    {
        printf("Você foi aprovado! Aqui está sua média: %f", media);
    }

    else
    {
        printf("Você infelizmente foi reprovado. Aqui está sua média: %f", media);
    }

    return 0;
}