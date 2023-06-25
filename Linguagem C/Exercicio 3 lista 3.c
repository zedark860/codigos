/******************************************************************************
3)
*******************************************************************************/

#include <stdio.h>

int main()
{
    int i1,i2,n,primo;
    
    printf("Digite até que número será analisado os números primos:");
    
    scanf(" %i", &n);
    
    for(i1=2;i1<=n;i1++)
    {
        
        primo=1;
        
        for(i2=2;i2<i1;i2++)
        {
            
            if(i1%i2==0)
                primo=0;
            
        }
        
        if(primo==1)
            printf(" %i", i1);
        
    }

    return 0;
}