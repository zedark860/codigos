def obter_resposta():
    while True:
        resposta=input('Quer continuar [S/N]? ').upper()
        if resposta in ('S','N'):
            return resposta
        else:
            print('Resposta inválida. Digite apenas S ou N.')
                    
cont=soma=0

n=int(input('Digite um número: '))
continuar=obter_resposta()
maior=menor=n

while continuar == 'S':
        soma+=n
        n=int(input('Digite um número: '))
        continuar=obter_resposta()
        cont+=1
        if n > maior:
            maior=n
        elif n < menor:
            menor=n
soma+=n
cont+=1

if cont > 0:
    media=soma/cont
else:
    media=0

print(f'Você digitou {cont} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')