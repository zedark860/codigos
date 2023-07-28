import time
import random
import pyautogui
import threading
import keyboard

# Função que realiza a contagem regressiva antes de iniciar o programa
def contagem(sec):
    for i in range(sec, 0, -1):
        print(f'Começando em {i} segundos...') # Contagem regressiva antes de iniciar
        time.sleep(1) # Intervalo de tempo da contagem
    print('Iniciando programa! Para parar digite [P ou p]')

# Função que gera um número aleatório entre 0 e 10
def gerar_random_num():
    return random.randint(0, 10)

# Função que realiza a geração de números aleatórios
def num_random(stop_event):
    pyautogui.FAILSAFE = False
    try:
        while not stop_event.is_set():
            numero = gerar_random_num()
            print(f'Digitando número: {numero}') # Número randozimado que foi digitado sendo mostrado ao usuário
            pyautogui.typewrite(str(numero)) # Número randomizado sendo digitado
            time.sleep(0.01) # Intervalo de tempo em que os números são mostrados

    except KeyboardInterrupt:
        print('\nPrograma interrompido pelo usuário.')

# Função que realiza o clique automático em um determinado intervalo de tempo
def auto_click(interval, stop_event):
    try:
        while not stop_event.is_set():
            pyautogui.click() # Executa o clique automático
            time.sleep(interval) # Intervalo de tempo entre os cliques

    except KeyboardInterrupt:
        print('\nAutoclick interrompido pelo usuário.')

# Função que aguarda o pressionamento da tecla "P" ou "p" para parar o programa
def stop_program(stop_event):
    keyboard.wait('p')  # Aguarda o pressionamento da tecla "P" ou "p"
    stop_event.set()  # Define o sinalizador para parar as threads
    print('\nPrograma parado pelo usuário.')

def main():
    intervalo_autoclick = 1  # Defina o intervalo do autoclick em segundos
    stop_event = threading.Event()  # Evento para sinalizar a parada do programa

    # Criação das threads para cada funcionalidade
    contagem_thread = threading.Thread(target=contagem, args=(10,))
    thread_autokeyboard = threading.Thread(target=num_random, args=(stop_event,))
    thread_autoclick = threading.Thread(target=auto_click, args=(intervalo_autoclick, stop_event))
    stop_thread = threading.Thread(target=stop_program, args=(stop_event,))

    # Início da contagem regressiva antes de iniciar o programa
    contagem_thread.start()
    stop_thread.start() 
    contagem_thread.join() # Aguarda a finalização da contagem regressiva

    # Início das threads para geração de números aleatórios e autoclick
    thread_autokeyboard.start()
    thread_autoclick.start()

    # Início da thread para parar o programa ao pressionar "P" ou "p"
    stop_thread.join() # Aguarda a finalização da thread de parada do programa
    # Aguardar o término das threads de geração de números aleatórios e autoclick
    thread_autokeyboard.join()
    thread_autoclick.join()

if __name__ == '__main__':
    main()