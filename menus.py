'''developed by: CaleIsaCh and another person'''
from reglas import *
def logo():
    '''Funcion que imprime el logo del juego'''
    import time
    logo = "╱╱╱╱╱╱╱╱╭╮╱╱╭╮\n╱╱╱╱╱╱╱╱┃┃╱╱┃┃\n╭━━┳╮╭┳━╯┣━━┫┃╭┳╮╭╮\n┃━━┫┃┃┃╭╮┃╭╮┃╰╯┫┃┃┃\n┣━━┃╰╯┃╰╯┃╰╯┃╭╮┫╰╯┃\n╰━━┻━━┻━━┻━━┻╯╰┻━━╯\n Grupo 'Real de programadores'"
    for i in logo.splitlines():
        print('\033[1;32m' + i + '\033[0m'.center(50))
        time.sleep(0.1)
def menu_principal():
    '''Funcion que imprime el menu principal'''
    import time
    logo()
    print('''
    \033[1;32m[1]\033[0m Jugar tablero nuevo
    \033[1;32m[2]\033[0m Ver/Jugar tablero guardado
    \033[1;31m[3] Finalizar\033[0m
    ''')
def bienbenida():
    '''Funcion que imprime el mensaje de bienvenida'''
    from reglas import retardar_impresion_string
    import os
    import time
    time.sleep(0.1)
    os.system('cls')
    logo()
    retardar_impresion_string("\n[*] Bienvenido jugador")
    retardar_impresion_string('\033[1;32m[*] Preciona ENTER para continuar... \033[0m')
    input()
    time.sleep(0.5)
    os.system('cls')
def menu_pause():
    '''Funcion que imprime el menu de pausa'''
    import os
    import time
    import json
    os.system('cls')
    logo()
    print('''
    \033[1;32m[1]\033[0m Continuar
    \033[1;32m[2]\033[0m Guardar y salir
    \033[1;32m[3]\033[0m Eliminar tablero
    \033[1;31m[4] Regresar al menu principal\033[0m
    ''')
    opcion=input('\033[1;33mSeleccione una opcion: \033[0m')
    time.sleep(0.5)
    os.system('cls')
    if opcion == '1':
        return False
    elif opcion == '2':
        exit()
    elif opcion == '3':
        with open("package.json", "r") as z:
            datos = z.read()
            diccionario = json.loads(datos)
            nombre_tablero = input("\033[0mIntrodusca nombre del tablero a eliminar \033[0m")
        del diccionario[nombre_tablero]
        with open("package.json", "w") as f:
            json.dump(diccionario, f)
        return False
    elif opcion == '4':
        iniciar_juego()
def iniciar_juego():
  '''Funcion que inicia el juego y llama a las funciones necesarias
  para que el juego funcione. Menus y demas impresos con colores y 
  retardados para darle un toque de estilo''' 
  from reglas import retardar_impresion_string
  from reglas import easter_egg
  import os
  import time
  # bienbenida() ############# comemtar o descomentar esta linea para evitar contratiempos
  # menu_principal() ########## same.
  opcion_seleccionada=input('\033[1;33mSeleccione una opcion: \033[0m')
  opcion_seleccionada = opcion_seleccionada.strip()
  while not opcion_seleccionada in ['1', '2', '3', '0']: ### Planeo poner el cero como activador de el easter egg
    print("\033[1;31m\n[!] Opcion invalida\n\033[0m")
    time.sleep(0.5)
    os.system('cls')
    menu_principal()
    opcion_seleccionada=input('\033[1;33mSeleccione una opcion correcta: \033[0m')
    opcion_seleccionada = opcion_seleccionada.strip()
  if opcion_seleccionada=='1':
    empezar_partida()
  elif opcion_seleccionada=='2':
    print("\033[1;31m\n[!] Opcion aun no disponible\033[0m")
    # regresando al menu principal
    retardar_impresion_string('\033[1;32m[*] Preciona ENTER para regresar... \033[0m')
    input()
    time.sleep(0.8)
    empezar_partida() ################################ Esta oarte es provicional que entre directo al juego
  elif opcion_seleccionada=='3':
    retardar_impresion_string("\033[1;31m[*] Finalizando...\033[0m")
    time.sleep(0.5)
    exit()
  elif opcion_seleccionada=='0':
    easter_egg()