maior=menor=peso=float(input(f'Peso da 1 pessoa: '))

for i in range(2,6):
    peso=float(input(f'Peso da {i} pessoa: '))

    if peso>maior:
        maior=peso
    elif peso<menor:
        menor=peso

print(f'O maior peso lido foi de {maior}kg')
print(f'O menor peso lido foi de {menor}kg')