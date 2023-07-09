range=[1,2,3,4,5]
maior=menor=int(input('Digite o primeiro número'))

for i in range[1:]:
    n1=int(input('Digite mais números: '))

    if n1 > maior:
        maior=n1
    
    if n1 < menor:
        menor=n1
        
print('O número {} é o maior número\n'.format(maior))
print('O número {} é o menor número\n'.format(menor))
