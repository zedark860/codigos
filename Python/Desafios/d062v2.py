print('Gerador de PA')
print('-='*10)
p1,rz=list(map(int, input('Digite o primeiro termo e a razão:\n').split()))

cont=0
termos=0

while cont < 10:
    print(f'{p1} -> ', end='')
    p1+=rz
    cont+=1
    termos+=1
print('PAUSA')

fim=int(input('Quantos termos você quer mostrar a mais? '))

while fim > 0:
    cont=0
    while cont < fim:
        print(f'{p1} -> ', end='')
        p1+=rz
        cont+=1
        termos+=1
    fim=int(input('Quantos termos você quer mostrar a mais? '))
    print('PAUSA')
print(f'Progressão finalizada com {termos} mostrados.')