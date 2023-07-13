
roxo='\33[95m'
azul='\33[94m'
reset='\33[0m'

n=int(input(roxo + 'Me diga qualquer número: ' + reset))

if n%2==0:
    print('O número {} é'.format(n), azul + 'PAR' + reset)
else:
    print('O número {} é'.format(n), azul + 'ÍMPAR' + reset)