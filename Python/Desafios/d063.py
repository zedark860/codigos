print('-'*20)
print('Sequência de Fibonacci')
print('-'*20)
n1=0
n2=1
n3=0
termos=int(input('Quantos termos você quer mostrar? '))
cont=0
while cont < termos:
    print(f'{n3} -> ', end='')
    n1=n2
    n2=n3
    n3=n1+n2
    cont+=1
print('FIM')