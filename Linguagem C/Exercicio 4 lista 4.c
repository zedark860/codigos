
#include <stdio.h>

int main()
{

    int n=1;
    
    printf("Sequência de números de 1 a 20 pulando de dois em dois:\n");

    do
    {
        
        if(n%2==1)
        printf(" %i", n);

        n++;
        
    }
    while(n!=0 && n!=21);

    printf(" 20");
    
    return 0;
}
