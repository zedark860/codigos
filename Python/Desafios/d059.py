def switch(opcao,n1,n2):
    while opcao!=5:
        print('''
        [1] somar\n
        [2] multiplicar\n
        [3] maior\n
        [4] novos números\n
        [5] sair do programa''')

        opcao=int(input('Qual será sua escolha? '))

        if opcao==1:
            soma=n1+n2
            print(f'A soma entre {n1} + {n2} é {soma}')
    
        elif opcao==2:
            multiplicar=n1*n2
            print(f'O resultado de {n1} x {n2} é {multiplicar}')

        elif opcao==3:
            if n1>n2:
                print(f'O maior número é {n1}')
            else:
                print(f'O maior número é {n2}')

        elif opcao==4:
            print('Informe os números novamente!')
            n1,n2=list(map(int, input('Digite os 2 valores: ').split()))
        
        elif opcao==5:
            print('Finalizando...')
            print('Fim do programa! Volte sempre!')

        else:
            print('Opção inválida. Tente novamente.\n')

n1,n2=list(map(int , input('Digite 2 valores: ').split()))
opcao=0
switch(opcao,n1,n2)
