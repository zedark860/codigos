salario=float(input('Qual é o sálario do funcionário? R$'))

if salario>=1250:
    conta=salario*0.10
    print(f'Quem ganhava R${salario} passa a ganhar R${salario+conta} agora')
else:
    conta=salario*0.15
    print(f'Quem ganhava R${salario} passa a ganhar R${salario+conta} agora')