distanciaV=float(input('Qual é a distância da sua viagem? (Em KM) '))

print(f'Você está prestes a começar uma viagem de {distanciaV}')
preço=distanciaV*0.50 if distanciaV<=200 else distanciaV*0.45
print(f'E o preço da sua passagem será de R${preço:.2f}')