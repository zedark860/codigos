
contador=0
soma=0

while True:
    opcao=str(input('Digite se você quer fazer a conta sim ou nao: '))

    if opcao=='sim':

        while contador < 2:
            contador += 1
            n=int(input('Digite o {}: '.format(contador)))
            soma+=n
        
        print('A soma dos números é {}.'.format(soma))
        break

    elif opcao=='nao':
        print('O programa acabou')
        break

    else:
        print('Nenhuma das duas opções foi digitada.')






