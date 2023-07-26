from math import factorial

n=int(input('Digite um valor para ser feito o cáculo do seu fatorial: '))
fatorial=factorial(n)
n+=1

while n!=1:
    n-=1
    if n==1:
        print(f'{n} = ', end='')
    else:
        print(f'{n} x ', end='')
print(f'O resultado é {fatorial}')
