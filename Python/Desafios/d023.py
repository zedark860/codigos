n=int(input('Digite um número: '))
num=n//1%10
d=n//10%10
c=n//100%10
m=n//1000%10
print('''Analisando seu número {}
      Unidade: {}
      Dezena: {}
      Centena: {}
      Milhar: {}
      '''.format(n,num,d,c,m))