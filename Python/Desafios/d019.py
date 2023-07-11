import random

a1,a2,a3,a4=list(map(str, input('Digite o nome de 4 alunos: \n').split()))
sorteio=random.choice([a1,a2,a3,a4])
print('O sorteado foi: {}.'.format(sorteio))