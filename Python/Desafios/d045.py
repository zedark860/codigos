import random
import socket

def jogo_pedra_papel_tesoura(num):
    itens=('Pedra', 'Papel', 'Tesoura')
    computador=random.randint(0,2)
    nome_maquina=socket.gethostname()
    if num==0:
        if itens[computador]=='Pedra':
            return 'IMPATE!', f'Eu(computador) e você({nome_maquina}) escolhemos PEDRA!'
        elif itens[computador]=='Papel':
            return 'PERDEU!', 'Eu(computador) escolhi PAPEL!'
        else:
            return 'GANHOU!', 'Eu(computador) escolhi TESOURA!'
    
    elif num==1:
        if itens[computador]=='Tesoura':
            return 'IMPATE!', f'Eu(computador) e você({nome_maquina}) escolhemos TESOURA!'
        elif itens[computador]=='Pedra':
            return 'PERDEU!', 'Eu(computador) escolhi PEDRA!'
        else:
            return 'GANHOU!', 'Eu(computador) escolhi PAPEL'
    
    elif num==2:
        if itens[computador]=='Papel':
            return 'IMPATE', f'Eu(computador) e você({nome_maquina}) escolhemos PAPEL!'
        elif itens[computador]=='Tesoura':
            return 'PERDEU!', 'Eu(computador) escolhi TESOURA!'
        else:
            return 'GANHOU!', 'Eu(computador) escolhi PEDRA!'
    
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