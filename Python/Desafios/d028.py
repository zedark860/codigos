import random

azul='\33[94m'
vermelho='\33[91m'
amarelo='\33[93m'
roxo='\33[95m'
reset='\33[0m'

print(azul + '========================Digite um número de 0 a 5 para descobrir qual o computador escolheu:====================================' + reset)

while True:
    n=int(input('Em que número pensei? '))
    nummaquina=random.randint(0,5)

    print(roxo + 'PROCESSANDO...' + reset)

    if n > 5:
        print(vermelho + 'O número digitado não está entre 0 a 5. DIGITE NOVAMENTE!' + reset)

    elif nummaquina==n:
        print(amarelo + 'PARABÉNS! Você conseguiu me vencer!' + reset)
        break

    else:
        print(vermelho + 'GANHEI! Eu pensei no número {} e não no {}'.format(nummaquina,n) + reset)
        break
    

    
