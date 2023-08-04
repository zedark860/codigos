def tabuada():
    num=0
    while True:
        num=int(input('Digite um número para ser feito a tabuada: '))
        if num < 0:
            print(f'PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')
            break
        for i in range(1, 11):
            resultado=i*num
            print(f'{num} x {i} = {resultado}')

while True:
    opcao=input('Quer iniciar o programa?[S/N] ').upper().strip()
    if opcao == 'S':
        tabuada()
        break
    elif opcao == 'N':
        print('OK, programa encerrado!')
        break
    else:
        print('Digite novamente, caracter inválido.')