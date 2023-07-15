distanciaV=float(input('Qual é a distância da sua viagem? (Em KM) '))

if distanciaV<=200:
    resul=distanciaV*0.50
    print(f'Você está prestes a começar uma viagem de {distanciaV:.2f}Km.\nE o preço da sua passagem será de R${resul}.')
else:
    resul=distanciaV*0.45
    print(f'Você está prestes a começar uma viagem de {distanciaV:.2f}Km.\nE o preço da sua passagem será de R${resul}.')