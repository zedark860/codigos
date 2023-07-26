import random

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 a 10.')
print('Será que consegue adivinhar qual foi?')
num=int(input('Qual foi seu palpite? '))

cont=0
numero_random=random.randint(0,10)

while num != numero_random:
    if numero_random > num:
        print('Mais... Tente mais uma vez.')
        num=int(input('Qual foi seu palpite? '))
        cont+=1
    else:
        print('Menos... Tente mais uma vez.')
        num=int(input('Qual foi seu palpite? '))
        cont+=1

print(f'Acertou com {cont}. Parabéns!')
        