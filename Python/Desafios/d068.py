from random import randint
from socket import gethostname

player = gethostname()
n = cont = 0

print('=-' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 10)

while True:
    num = randint(0, 10)
    n = int(input('Digite um número: '))
    p_ou_i = input('Você escolhe [P ou I?]: ').upper().strip()

    if p_ou_i not in ['P', 'I']:
        print('DIGITE NOVAMENTE, CARACTER INVÁLIDO!')
    else:
        soma = n + num
        if p_ou_i == 'P':
            if soma % 2 == 0:
                par = f'Total de {soma} DEU PAR'
                print(f'Você({player}) jogou {n} e o computador {num}. {par}')
                print('Você GANHOU!')
                cont += 1
            else:
                impar = f'Total de {soma} DEU ÍMPAR'
                print(f'Você({player}) jogou {n} e o computador {num}. {impar}')
                print('Você PERDEU!')
                print('-=' * 10)
                print(f'GAME OVER! Você venceu {cont} vezes.')
                break
        elif p_ou_i == 'I':
            if soma % 2 == 1:
                impar = f'Total de {soma} DEU ÍMPAR'
                print(f'Você({player}) jogou {n} e o computador {num}. {impar}')
                print('Você GANHOU!')
                cont += 1
            else:
                par = f'Total de {soma} DEU PAR'
                print(f'Você({player}) jogou {n} e o computador {num}. {par}')
                print('Você PERDEU!')
                print('-=' * 10)
                print(f'GAME OVER! Você venceu {cont} vezes.')
                break