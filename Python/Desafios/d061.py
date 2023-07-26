print('Gerador de PA')
print('-='*10)
p1,rz=list(map(int, input('Digite o primeiro termo e a razão:\n').split()))

cont=0

while cont < 10:
    print(f'{p1} -> ', end='')
    p1+=rz
    cont+=1
print('FIM')