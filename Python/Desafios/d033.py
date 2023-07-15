n1,n2,n3=list(map(int, input('Digite 3 valores: ').split()))

menor=n1
maior=n1

if n2<n1 and n2<n3:
    menor=n2
elif n3<n1 and n3<n2:
    menor=n3
elif n2>n1 and n2>n3:
    maior=n2
elif n3>n1 and n3>n2:
    maior=n3

print(f'O menor valor é {menor}\nO maior valor é {maior}')
