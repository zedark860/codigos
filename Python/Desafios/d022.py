nome=str(input('Digite seu nome aqui: '))
split=nome.split()

print('Seu nome é: {}'.format(nome))
print('Seu nome em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome em minúsculo é: {}'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome.replace(' ',''))))
print('Seu primeiro nome {} tem {} letras'.format(split[0],len(split[0])))