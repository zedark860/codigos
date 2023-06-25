A	 prefeitura	 de	 uma	 cidade	 fez	 uma	 	 pesquisa	 com	 200	 pessoas,	coletando	dados	sobre	o	salário	e	o	número	de	filhos.	A	prefeitura	deseja	
saber	
• A	média	do	salário	dessas	pessoas	
• A	média	do	número	de	filhos		
• O	maior	salário	
• A		percentagem		de		pessoas		com		salários		até		R$	150,00

#include stdio.h

int main()
{
    
    int n, filhos, i, media1, media2, maiorsla, pcnt=0, soma1=0, soma2=0;
    
    for(i=1;i=5;i++)
    {
        
        printf(Digite seu salário e número de filhosnR$);
        scanf( %i %i, &n, &filhos);
        
        soma1=soma1+n;
        soma2=soma2+filhos;
        
        media1=soma1i;
        media2=soma2i;
        
        if(nmaiorsla)
            maiorsla=n;
        
        if(n=150)
            pcnt=pcnt+1;
        
    }
    
    printf(A média	do	salário das pessoas %in, media1);
    printf(A média	do	número	de	filhos %in, media2);
    printf(O maior	salário das pessoas %in, maiorsla);
    printf(A porcentagem de pessoas com salários até R$ 150,00 %%%in, pcnt);
    
    return 0;
}