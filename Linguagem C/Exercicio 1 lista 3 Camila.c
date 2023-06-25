/******************************************************************************
1) Solicite ao usuC!rio que digite 10 nC:meros e apC3s realizar a impressC#o dos nC:meros em ordem decrescente.
*******************************************************************************/

#include <stdio.h>

int main ()
{
    int i;

    for (i=10;i>=1;i--)
    {
        
       if(i%2==1)
       {
           printf("Número %i\n", i);
       }
        
    }
    


  return 0;
}