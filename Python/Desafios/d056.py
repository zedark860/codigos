media=0
maior=0
cont=0
for i in range(1,5):
    print(f'----- {i} PESSOA -----')
    nome=str(input('Nome: '))
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: ')).upper()

    media+=idade
    if i==1 and sexo=='M':
        maior=idade
        nomemaior=nome
    else:
        if idade>maior and sexo=='M':
            maior=idade
            nomemaior=nome
    
    if sexo=='F' and idade<20:
        cont+=1

print(f'A média de idade do grupo é de {media/4} anos')
print(f'O homem mais velho tem {maior} e se chama {nomemaior}.')
print(f'Ao todo são {cont} mulheres com menos de 20 anos.')

