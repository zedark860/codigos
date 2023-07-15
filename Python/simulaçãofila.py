ultimo=10
fila=list(range(1,ultimo+1))
while True:
    print(f'Existem {len(fila)} clientes na fila')
    print(f'Fila atual: {fila}')
    print('''Digite F para dicionar um cliente ao fim da fila,\nou A para realizar o atendimento. S para sair.''')
    
    operacao=str(input('Operação (F, A ou S): ')).upper().strip()
    
    if operacao=='A':

        if len(fila)>0:
            atendido=fila.pop(0)
            print(f'Cliente {atendido} atendido.')
        else:
            print('Fila vazia! Ninguém para atender.')
    
    elif operacao=='F':
        ultimo+=1
        fila.append(ultimo)
    elif operacao=='S':
        print('Programa finalizado!')
        break
    else:
        print('Operação inválida! Digite apenas F, A ou S!')
    
