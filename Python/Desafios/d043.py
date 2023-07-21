def pesos(imc):
    if imc<18.5:
        return 'Você está ABAIXO do peso!'
    elif imc>=18.5 and imc<=25:
        return 'Você está no peso IDEAL!'
    elif imc>25 and imc<=30:
        return 'Você está com SOBREPESO!'
    elif imc>30 and imc<=40:
        return 'Você está com OBSIDADE!'
    elif imc>40:
        return 'Você está com OBESIDADE MÓRBIDA!'

peso,altura=list(map(float, input('Digite seu peso e altura: ').split()))
imc=peso/(altura**2)

print(f'Seu IMC é {imc:.1f}.')

resultado=pesos(imc)
print(resultado)

    