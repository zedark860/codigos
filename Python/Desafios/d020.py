import random

a1,a2,a3,a4=list(map(str, input('Digite o nome de 4 alunos: \n').split()))
list=[a1,a2,a3,a4]
random.shuffle(list)
print('Ordem de apresentação sorteada: {}.'.format(list))