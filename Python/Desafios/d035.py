azul='\33[94m'
reset='\33[0m'

print(azul+'=-='*20+reset)
print(azul+'Analisador de Triângulos'+reset)
print(azul+'=-='*20+reset)

r1,r2,r3=list(map(float, input('Digite os valores de comprimento dos 3 segmentos: ').split()))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')