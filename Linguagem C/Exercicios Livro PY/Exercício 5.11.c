#include <stdio.h>

int main()
{
    
    float dinicial, jpou, total;
    
    int mes=0;
    
    printf("Digite o total do Depósito inicial e a taxa de juros de uma poupança:\n");
    printf("Digite também até qual mês você quer fazer o depósito:\n");
    
    scanf(" %f %f", &dinicial, &jpou);
    
    total=dinicial;
    
    while(mes<=22)
    {
        
        mes=mes + 1;
        
        printf("Mês %i:\n", mes);
        
        scanf(" %f", &dinicial);
        
        total=dinicial;
        
        total=total +(total*(jpou/100));
        
        printf("O saldo é: R$%2.f\n", total);
        
    }
    
    printf("Taxa total ganha com juros é: R$%2.f\n", total - dinicial);

    return 0;
}