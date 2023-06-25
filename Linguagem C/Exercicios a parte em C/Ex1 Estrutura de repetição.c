//Faça	um	programa	em	C	que	mostre	a	 tabuada	do	número	5.	 (considerar	tabuada	do		número	1	ao	10).

#include <stdio.h>

int main()
{
    int n=5, i, resul;
    
    printf("Tabuada de 5:\n");
    
    for(i=1;i<=10;i++)
    {
        
        resul=n*i;
        
        printf("%ix%i=%i\n",n,i,resul);
        
    }

    return 0;
}