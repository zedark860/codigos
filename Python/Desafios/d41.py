from datetime import date

ano=int(input('Digite sua idade: '))
atual=date.today().year
idade=ano-atual

if idade <= 9:
    print('O atleta é Mirim')
elif idade <=14:
    print('O atleta é Infantil')
elif idade <=19:
    print('O atleta é Junior')
elif idade <=25:
    print('O atleta é Sênior')
else:
    print('O atleta é Master')