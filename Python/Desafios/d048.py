acumulador=0
contador=0

for i in range(1, 501, 2):
    if i%3==0:
        acumulador+=i
        contador+=1
print(f'{acumulador} e {contador}', end=' ')