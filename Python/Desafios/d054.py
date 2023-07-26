from datetime import date
contM=0
contm=0
anoatual=date.today().year
for i in range(1,8):
    ano=int(input(f'Em que ano nasceu a {i} pessoa? '))
    if anoatual-ano >= 18:
        contM+=1
    else:
        contm+=1

print(f'Ao todo tivemos {contM} pessoas maiores de idade.')
print(f'Ao todo tivemos {contm} pessoas menores de idade.')