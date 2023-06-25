//Uma		loja		ualiza		o		código		V		para		compras		à		vista		e		o	código		P		para		
//compras		a		prazo.		Faça		um		algoritmo		que	receba	o	código	de		e	o	valor	
//de	15	transações.	Calcule	e	mostre:	
//• O	valor	total	das	compras	à	vista	
//• O	valor	total	das	compras	a	prazo	
//• O	valor	total	das	compras	efetuadas	

#include <stdio.h>

int main()
{
    int avista=0, aprazo=0, cpefetuadas=0, valort, i;
    
    char codigo;
    
    for(i=1;i<=15;i++)
    {
    
    printf("Digite V para compras à vista e P para compras a prazo:\n");
    scanf(" %c", &codigo);
    
    printf("Digite o valor da transação:\n");
    scanf(" %i", &valort);
    
    if(codigo== 'V' || codigo== 'v')
        avista=avista+valort;
    else if(codigo== 'P' || codigo== 'p')
       aprazo=aprazo+valort;

    cpefetuadas=cpefetuadas+valort;

    }
    
    printf("Valor a vista: %i\n", avista);
    
    printf("Valor a prazo: %i\n", aprazo);
    
    printf("Valor de todas as compras efetuadas: %i\n", cpefetuadas);
    
    return 0;
}