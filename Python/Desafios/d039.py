from datetime import date

ano=int(input('Digite o seu ano de nascimento:\n(Para encerra o programa digite 0!)'))
ano_atual=date.today().year
idade=ano_atual - ano 
print(f'Quem nasceu em {ano} tem {idade} em {ano_atual}.')

if idade < 18:
    dimi=18-idade
    print(f'Ainda faltam {dimi} para o alistamento.')
    print(f'Seu alistamento será em {ano_atual+dimi}')
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!') 
else:
    dimi=idade-18
    print(f'Você já deveria ter se alistado há {dimi} anos.')
    print(f'Seu alistamento foi em {ano_atual-dimi}')
