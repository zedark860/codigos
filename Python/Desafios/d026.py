import unicodedata

frase=str(input('Digite uma frase:')).strip()
frase1=frase.upper()
frase1_unicode=unicodedata.normalize('NFKD',frase1)
frase2=frase1_unicode.find('A')+1
frase3=frase1_unicode.rfind('A')+1
contagem_a=frase1_unicode.count('A')
print('A letra A apareceu {} vezes na frase.'.format(contagem_a))
print('A primeira letra A aparece na posição {}.'.format(frase2))
print('A última letra A aparece na posição {}.'.format(frase3))