def bases(num):

    if opcao==1:
        binario=bin(num)[2:]
        return f'O seu número em é binario {binario}'
    elif opcao==2:
        octal=oct(num)[2:]
        return f'O seu número em é decimal {octal}'
    elif opcao==3:
        hexadecimal=hex(num)[2:]
        return f'O seu número em é hexadecimal {hexadecimal}'
    else:
        return 'Você não escolheu nenhuma das opções acima, escolha novamente!'

while True:
    num=int(input('Digite um número: '))
    print('Escolha uma das opções abaixo para converter o número:\n[1] Binário\n[2] Octal\n[3] Hexadecimal')
    opcao=int(input('Digite uma das opções: '))
    print('Caso queira sair do programa digite 0.')

    if opcao==0:
        print('Programa encerrado!')
        break

    resultado=bases(num)
    print(resultado)
