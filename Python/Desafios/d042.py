vermelho='\33[91m'
reset='\33[0m'

r1,r2,r3=0,0,0
valor=0

def segmentos(r1,r2,r3):

    if r1==r2 and r2==r3 and r3==r1:
        if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
            return 'Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!'
        
    elif r1==r2 or r2==r3 or r3==r1:
        if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
            return 'Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!'
    
    elif r1!=r2 and r2!=r3 and r3!=r1:
        if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
            return 'Os segmentos acima PODEM FORMAR um triângulo ESCALENO!'
        else:
            return 'Os segmentos acima NÃO PODEM FORMAR um triângulo!'

for i in range(3):
    valor=float(input(f'Digite o {i+1}º segmento: '))
    if i==0:
        r1=valor
    elif i==1:
        r2=valor
    else:
        r3=valor

resultado=segmentos(r1,r2,r3)
print(resultado)

