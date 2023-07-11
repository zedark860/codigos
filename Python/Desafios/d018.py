import math

angulo=float(input('Digite o angulo:'))
rad=math.radians(angulo)
sen=math.sin(rad)
cos=math.cos(rad)
tan=math.tan(rad)
print('O seno de {} é: {:.2f}.\n O cosseno de {} é: {:.2f}.\n A tangente é {}: {:.2f}.\n'.format(angulo,sen,angulo,cos,angulo,tan))