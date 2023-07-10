def get_choices():
    player_choice=str(input('Digite Pedra, Papel ou Tesoura: '))
    computer_choice='paper'
    option={'player': player_choice, 'computer': computer_choice}
    return option

option=get_choices()

print(option)

