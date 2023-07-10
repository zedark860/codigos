list=[1,2,3,4,5,6,7,8,9,10]
n=int(input('Digite um número para ser feita a tabuada: '))

for i in list:
    tab=n*i
    print('{} x {} = {}'.format(n,i,tab))