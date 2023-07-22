import random
import socket

def jogo_pedra_papel_tesoura(num):
    itens=('Pedra', 'Papel', 'Tesoura')
    computador=random.choice(itens)
    nome_maquina=socket.gethostname()
    if num==0:
        if computador=='Pedra':
            return 'IMPATE!', f'Eu({nome_maquina}) e você(Player) escolhemos PEDRA!'
        elif computador=='Papel':
            return 'PERDEU!', f'Eu({nome_maquina}) escolhi PAPEL!'
        else:
            return 'GANHOU!', f'Eu({nome_maquina}) escolhi TESOURA!'
    
    elif num==1:
        if computador=='Tesoura':
            return 'IMPATE!', f'Eu({nome_maquina}) e você(Player) escolhemos TESOURA!'
        elif computador=='Pedra':
            return 'PERDEU!', f'Eu({nome_maquina}) escolhi PEDRA!'
        else:
            return 'GANHOU!', f'Eu({nome_maquina}) escolhi PAPEL'
    
    elif num==2:
        if computador=='Papel':
            return 'IMPATE', f'Eu({nome_maquina}) e você(Player) escolhemos PAPEL!'
        elif computador=='Tesoura':
            return 'PERDEU!', f'Eu({nome_maquina}) escolhi TESOURA!'
        else:
            return 'GANHOU!', f'Eu({nome_maquina}) escolhi PEDRA!'
    
    return 'Você não escolheu nenhuma das OPÇÕES!'

while True:
    print('Suas opções:\n [ 0 ] PEDRA\n [ 1 ] TESOURA\n [ 2 ] PAPEL\n')

    num=int(input('Qual sua jogada? '))
    print('JO\nKEN\nPO!!!')
    resultado=jogo_pedra_papel_tesoura(num)
    print(resultado)

    opcao=input('Quer jogar novamente? (S/N) ').upper().strip()
    if opcao!='S'and opcao!='SIM':
        print('Jogo finalizado!')
        break
    else:
        print('Jogo reiniciado!')