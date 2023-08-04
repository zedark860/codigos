p18=m=f=0

while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade=int(input('Idade: '))
    if idade >= 18:
        p18+=1

    sexo=input('Sexo: [M/F]').upper().strip()

    if sexo=='M':
        m+=1
    elif sexo=='F' and idade < 20:
        f+=1
    elif sexo not in ['M','F']:
        print('Caracter inválido, digite novamente!')
        continue
    
    print('-'*20)
    opcao=input('Quer continuar? [S/N]').upper().strip()

    while opcao not in ['S','N']:
        print('Caracter inválido, digite novamente!')
        opcao=input('Quer continuar? [S/N]').upper().strip()
    
    if opcao=='N':
        break

print(f'Total de pessoas com mais de 18 anos: {p18}')
print(f'Ao todo temos {m} homens cadastrados')
print(f'E temos {f} mulheres com menos 20 anos')