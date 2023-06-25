/******************************************************************************
Imprima os números de 1 a 10, substituindo os múltiplos de 3 pela palavra "FIZZ" e os múltiplos de 5 pela palavra "BUZZ".
*******************************************************************************/

#include <stdio.h>

int main()
{
    int i;
    
    for(i=1;i<=10;i++)
    {
        
        if(i%3==0 && i%5==0)
            printf("FIZZ BUZZ ");
        
        else if(i%3==0)
            printf("FIZZ ");
        
        else if(i%5==0)
            printf("BUZZ ");
            
        else
            printf("%i ", i);
        
    }
    
    return 0;
}