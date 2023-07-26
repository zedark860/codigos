print('Gerador de PA')
print('-='*10)
p1,rz=list(map(int, input('Digite o primeiro termo e a razão:\n').split()))

cont=0
mais=10
tot=0
termos=0

while mais != 0:
    tot+=mais
    while cont < tot:
        print(f'{p1} -> ', end='')
        p1+=rz 
        cont+=1
        termos+=1
    print('PAUSA')
    mais=int(input('Quantos termos a mais quer mostrar?'))
print(f'Progressão finalizada com {termos} termos mostrados.')
