num=int(input('Digite um número para saber se ele é ou não primo: '))
total=0

for i in range(1, num+1):
    if num % i ==0:
        print('\33[33m ', end='')
        total+=1
    else:
        print('\33[31m ', end='')
    print(f'{i} ', end='')

print(f'\n\nO total de vezes que o número {num} foi divido: {total} vezes')

if total==2:
    print('Ele é primo.')
else:
    print('Ele não é primo.')


