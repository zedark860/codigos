#include <stdio.h>

int main() 
{

  int num, aux, reverso;

  printf("Digite um natural: ");
  scanf("%d", &num);

  aux = num;
  reverso = 0;

  while (aux != 0) 
  {

    reverso = reverso * 10 + aux % 10;  
    aux = aux / 10;   

  }

  if (reverso == num)
    printf("%d é um número palíndromo.\n", num);
  
  else
    printf("%d não é um número palíndromo.\n", num);

  return 0;
}