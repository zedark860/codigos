d,km=list(map(int, input('Digite quantos dias o carro foi alugado e quantos KM ele percorreu:').split()))
mult=d*60
mult1=km*0.15
print('O preço a pagar é igual a R${}'.format(mult+mult1))