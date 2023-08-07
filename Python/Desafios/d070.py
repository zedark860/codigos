resul=cont=0
menor=float('inf')
menorprot=''

print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)

while True:
    produto=input('Nome do Produto: ').strip()
    if produto.lower() == 'fim':
        break
    preco=float(input('Preço: R$'))
    
    opcao=input('Quer continuar? [S/N]').strip().upper()
    if opcao=='N':
        break
    elif opcao!='S' and 'N':
        print('Caractér inválido, digite novamente!')
    
    resul+=preco
    if preco > 1000:
        cont+=1
    
    if preco < menor:
        menor=preco
        menorprot=produto

print('-'*10, 'FIM DO PROGRAMA' ,'-'*10)

print(f'O total de compra foi R${resul:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {menorprot} que custa R${menor}')  