
vermelho='\33[91m'
amarelo='\33[93m'
reset='\33[0m'

velocidade=float(input('Digite a velocidade do seu carro(RADAR): '))

if velocidade >= 80:

    mutiplicacao=(velocidade-80)*7.00

    print(vermelho + 'Você foi multado! Sua multa é de R${}'.format(mutiplicacao) + reset)
    print(amarelo + 'Tenha um bom dia! Dirija com segurança!' + reset)

else:
    print(amarelo + 'Tenha um bom dia! Dirija com segurança!' + reset)