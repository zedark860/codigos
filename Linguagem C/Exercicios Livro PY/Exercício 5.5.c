#include <stdio.h>

int main()
{
    
    int cont=0;
    
    while(cont <= 10)
    {
        
        cont=cont + 1;
        
        if(cont%3==0)
        {
            
            printf(" %i", cont);
            
        }
        
    }
    
    return 0;
}