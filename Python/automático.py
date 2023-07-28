import time
import random
import pyautogui
import threading
import keyboard

def contagem(sec):
    for i in range(sec, 0, -1):
        print(f'Começando em {i} segundos...')
        time.sleep(1)
    print('Iniciando programa! Para parar digite [P ou p]')

def gerar_random_num():
    return random.randint(0, 10)

def num_random():
    pyautogui.FAILSAFE = False  
    contagem(10)
    try:
        while True:
            if keyboard.is_pressed('P') or keyboard.is_pressed('p'):
                print('\nPrograma parado pelo usuário.')
                break

            numero = gerar_random_num()
            print(f'Digitando número: {numero}')
            pyautogui.typewrite(str(numero))
            time.sleep(0.01)

    except KeyboardInterrupt:
        print('\nPrograma interrompido pelo usuário.')

def main():
    thread_autokeyboard = threading.Thread(target=num_random)
    thread_autokeyboard.start()
    thread_autokeyboard.join()

if __name__ == '__main__':
    main()
