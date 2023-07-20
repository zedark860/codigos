valor_casa=float(input('Digite o valor da casa: R$'))
salario=float(input('Digite também o valor do seu salário: R$'))
anos=int(input('Digite em quantos anos você irá pagar isso tudo: '))

prestacao=valor_casa/(anos*12)
porcent=salario*0.30

print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}!')

if prestacao <= porcent:
    print('Empréstimo ACEITO!')
else:
    print('Empréstimo NEGADO!')

