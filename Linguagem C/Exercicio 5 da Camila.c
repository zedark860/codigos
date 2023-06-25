/******************************************************************************

5) Uma empresa concederá um aumento de salário aos seus funcionários, variável de acordo com o cargo, conforme a tabela abaixo. 
Faça um algoritmo que leia o salário e o cargo de um funcionário e calcule o novo salário. 
Se o cargo do funcionário não estiver na tabela, ele deverá, então, receber 40% de aumento. 
Mostre o salário antigo, o novo salário e a diferença.

*******************************************************************************/

#include <stdio.h>

int main()
{
    
    float salario_antigo, novo_salario, diferença, aumento;
    
    int codigo;
    
    printf("Digite o seu salário:");
    
    scanf("%f", &salario_antigo);
    
    printf("Digite o código referente ao cargo: (Caso não esteja na tabela digite 0)");
    
    scanf(" %i", &codigo);
    
    if(codigo== 101)
        {
        
        aumento=salario_antigo* 0.10;
        
        novo_salario=aumento+salario_antigo;
        
        diferença=novo_salario-salario_antigo;
        
        printf("Aqui está seu salário antigo: %2.f\n", salario_antigo);
        
        printf("Aqui está seu novo salário: %2.f\n", novo_salario);
        
        printf("Aqui está a diferença do salário antigo e novo salário: %2.f\n", diferença);
        
        }
       
        if(codigo== 102)
            {
            
            aumento=salario_antigo* 0.20;
            
            novo_salario=aumento+salario_antigo;
            
            diferença=novo_salario-salario_antigo;
            
            printf("Aqui está seu salário antigo: %2.f\n", salario_antigo);
            
            printf("Aqui está seu novo salário: %2.f\n", novo_salario);
            
            printf("Aqui está a diferença do salário antigo e novo salário: %2.f\n", diferença);
            
            }   
            
            if(codigo== 103)
                {
               
                aumento=salario_antigo* 0.20;
                
                novo_salario=aumento+salario_antigo;
                
                diferença=novo_salario-salario_antigo;
                
                printf("Aqui está seu salário antigo: %2.f\n", salario_antigo);
                
                printf("Aqui está seu novo salário: %2.f\n", novo_salario);
                
                printf("Aqui está a diferença do salário antigo e novo salário: %2.f\n", diferença);
               
                }
                    
                    else if(codigo== 0)
                    {
                        
                        aumento=salario_antigo* 0.40;
                        
                        novo_salario=aumento+salario_antigo;
                        
                        diferença=novo_salario-salario_antigo;
                        
                        printf("Aqui está seu salário antigo: %2.f\n", salario_antigo);
                        
                        printf("Aqui está seu novo salário: %2.f\n", novo_salario);
                        
                        printf("Aqui está a diferença do salário antigo e novo salário: %2.f\n", diferença);
                        
                    }

    return 0;
}