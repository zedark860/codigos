//

#include <stdio.h>

int main()
{
    float salario, financiamento;
    
    int tempo;
    
    printf("Digite seu salário e seu financiamento pretendido");
    
    scanf("%f%f", &salario, &financiamento);
    
    if(financiamento<=(salario*5))
        printf("O seu financiamento foi aprovado!\n");
        
    else
    {
        printf("O seu financiamento foi negado.\n");
        return 0;
    }        
            printf("Agora digite quanto tempo o valor ficará armazenado, de acordo com a tabela, mas em meses.\n");
            
            scanf("%i", &tempo);
            
            if(tempo>=60)
                {
                    printf("A taxa de juros é de 0.95");
                    return 0;
                }
                
            if(tempo<60 && tempo>=48)
                {
                    printf("A taxa de juros é de 0.9");
                    return 0;
                }
                
            if(tempo<48 && tempo>=36)
                {
                    printf("A taxa de juros é de 0,85");
                    return 0;
                }
                
            if(tempo<36 && tempo>=24)
                {
                  printf("A taxa de juros é de 0,75");
                  return 0;
                }
                
            if(tempo<24 && tempo>=12)
                {
                    printf("A taxa de jurtos é de 0,65");
                    return 0;
                }
            if(tempo<12)
                {
                    printf("A taxa de juros é de 0,55");
                    return 0;
                }

    return 0;
}