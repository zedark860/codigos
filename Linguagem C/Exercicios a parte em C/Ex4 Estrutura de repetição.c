//Faça	um	programa	em	C	que	exiba	na	tela	os	números	ímpares	entre	100	 e	300.	

#include <stdio.h>

int main()
{
    
    int i;
    
    printf("100");
    
    for(i=100;i<=300;i++)
    {
        
        if(i%2==1)
            printf(" %i", i);
        
    }

    printf(" 300");

    return 0;
}