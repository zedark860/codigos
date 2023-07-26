soma=0
cont=0
num=0

while num != 999:
    num=int(input('Digite um número [999 para parar]: '))
    soma+=num
    cont+=1
cont-=1
soma-=999
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')