#include <stdio.h>

int main()
{
    
    float dinicial, jpou, total;
    
    int mes=1, fim;
    
    printf("Digite o total do Depósito inicial e a taxa de juros de uma poupança:\n");
    printf("Digite também até qual mês você quer fazer o depósito:\n");
    
    scanf(" %f %f %i", &dinicial, &jpou, &fim);
    
    total=dinicial;
    
    mes=mes - 1;
    
    fim=fim - 1;
    
    while(mes<=fim)
    {
        
        mes=mes + 1;
        
        printf("Mês %i:\n", mes);
        
        total=total +(total*(jpou/100));
        
        printf("O saldo é: R$%2.f\n", total);
        
    }
    
    printf("Taxa total ganha com juros é: R$%2.f\n", total - dinicial);

    return 0;
}