nota1=float(input('Primeira nota: '))
nota2=float(input('Segunda nota: '))

media=(nota1+nota2)/2

if media < 5:
    print('Reprovado!')
elif media >= 5 and media <= 6.9:
    print('Recuperação!')
else:
    print('Aprovado!')
