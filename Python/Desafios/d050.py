acumulador=0
cont=0

for i in range(6):
    num=int(input('Digite um número: '))
    if num%2==0:
        acumulador+=num
        cont+=1

print(f'A sua soma é: {acumulador} e você havia informado pares {cont}')