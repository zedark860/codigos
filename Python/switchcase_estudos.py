
print(' Java\n Python\n Ruby\n')

option=str(input('Digite uma das opções acima: '))

match option:
    case 'Java':
        print('Você escolheu estudar Java.')
    case 'Python':
        print('Você escolheu estudar Python.')
    case 'Ruby':
        print('Você escolheu estudar Ruby.')
    case _:
        print('Nenhuma das opções foi escolhida>')