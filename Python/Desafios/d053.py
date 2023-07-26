frase=str(input('Digite uma frase')).upper().strip()
print(f'Voce digitou a frase: {frase}')
fcolada=frase.replace(' ', '')
palavra_invertida=fcolada[::-1]

if palavra_invertida == fcolada:
    print('É um palindromo.')
else:
    print('Não é um palindromo.')
