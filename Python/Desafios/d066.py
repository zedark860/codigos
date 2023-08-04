n=s=0
cont=0
while True:
    n=int(input(f'Digite o número {cont+1} (Para parar digite 999): '))
    if n==999:
        break
    s+=n
    cont+=1
print(f'A soma dos {cont} valores foi {s}!')
