print('='*21)
print('10 TERMOS DE UMA P.A')
print('='*21)

p_termo=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razão: '))

for i in range(p_termo,p_termo+10):
    print(f'{p_termo}-> ', end='')
    p_termo+=razao

print('ACABOU!')