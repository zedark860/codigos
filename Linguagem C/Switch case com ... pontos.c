#include <stdio.h>

int main()
{   
    int codigo;
    
    printf("Digite o código de acordo com a tabela de paises:\n");
    
    printf("Código do produto entre 1 a 20: Europa.\nCódigo do produto entre 21 a 40: Ásia.\nCódigo do produto entre 41 a 60: América.\nCódigo do produto entre 61 a 80: África.\nCódigo do produto maior que 80: Paraguai.\n");
    
    scanf(" %i", &codigo);
    
    switch(codigo)
    {
        
        case 1 ... 20:
            printf("Seu produto será da Europa.");
                break;
                
        case 21 ... 40:
            printf("Seu produto será da Ásia.");
                break;
                
        case 41 ... 60:
            printf("Seu produto será da América.");
                break;
                
        case 61 ... 80:
            printf("Seu produto será da África");
                break;
                
        default:
            printf("Seu produto será do Paraguai");
                break;
            
        
    }

    return 0;
}