print('='*5, 'LOJAS GUANABARA', '='*5)
pcompras=float(input('Preço das compras: R$'))

while True:
    print('FORMAS DE PAGAMENTO\n [ 1 ] à vista dinheiro/cheque\n [ 2 ] à vista cartão\n [ 3 ] 2x no cartão\n [ 4 ] 3x ou mais no cartão')
    opcao=int(input('Qual é a opção? '))

    if opcao==1:
        desconto=pcompras*0.10
        novo_preço=pcompras-desconto
        print(f'Sua compra de R${pcompras} vai custar R${novo_preço} no final.')
        break
    elif opcao==2:
        desconto=pcompras*0.5
        novo_preço=pcompras-desconto
        print(f'Sua compra de R${pcompras} vai custar R${novo_preço} no final.')
        break
    elif opcao==3:
        div=pcompras/2
        print(f'Sua compra será parcelada em 2x de R${div:.2f}')
        print(f'Sua compra de R${pcompras} vai custar o mesmo preço no final.')
        break
    elif opcao==4:
        desconto=pcompras*0.20
        novo_preço=pcompras+desconto
        parcelas=int(input('Quantas parcelas? '))
        div=novo_preço/parcelas
        print(f'Sua compra será parcelada em {parcelas}x de R${div:.2f}')
        print(f'Sua compra de R${pcompras} vai custar R${novo_preço} no final.')
        break
    else:
        print('Você não digitou nenhuma das opções acima, favor escolher novamente!')