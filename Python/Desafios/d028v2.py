import random

azul='\33[94m'
vermelho='\33[91m'
amarelo='\33[93m'
roxo='\33[95m'
reset='\33[0m'

def jogo_adivinhacao(n, nummaquina):

    if n > 5:
        return vermelho + 'O número digitado não está entre 0 a 5. DIGITE NOVAMENTE!' + reset

    elif nummaquina==n:
        return amarelo + 'PARABÉNS! Você conseguiu me vencer!' + reset

    else:
        return vermelho + 'GANHEI! Eu pensei no número {} e não no {}'.format(nummaquina,n) + reset

while True:

    print(azul + '========================Digite um número de 0 a 5 para descobrir qual o computador escolheu:====================================' + reset)

    n=int(input('Em que número pensei? '))
    nummaquina=random.randint(0,5)

    print(roxo + 'PROCESSANDO...' + reset)

    resultado=jogo_adivinhacao(n,nummaquina)

    print(resultado)

    jogar_novamente=str(input('Você deseja jogar novamente? (S/N)')).upper().strip()

    if jogar_novamente != 'S' and jogar_novamente != 'SIM':
        print('Você digitou NÃO. O programa será finalizado!')
        break

    else:
        print('O programa foi reiniciado. Jogue novamente!')
