'''developed by: CaleIsaCh and another person'''
from solver_backtracker import *
import json
import os

if not os.path.exists('package.json'):
    with open('package.json', 'w') as z:
        json.dump({}, z)
with open("package.json", "r") as z:
    if z != "":
        datos = z.read()
        diccionario = json.loads(datos)
    else:
        diccionario = {}
with open("package.json", "w") as f:
    json.dump(diccionario, f)

def print_tablero(tablero_seleccionado,nombre_tablero,tablero_bool):
  '''Imprime el tablero seleccionado mediante un random'''
  print(f'\033[1;36m{nombre_tablero}\033[0;0m'.center(40))
  print("  | 1 2 3 | 4 5 6 | 7 8 9 |")
  for i in range(9):
      if i%3==0:
          print("−−−−−−−−−−−−−−−−−−−−−−−−−−−")
      print(i+1, end=" ")
      for j in range(9):
          if j%3==0:
              print("|", end=" ")
          if tablero_seleccionado[i][j] == 0:
              print(".", end=" ")
          else:
              if (tablero_bool[i][j] and tablero_seleccionado[i][j]) != 0:
                  print(tablero_seleccionado[i][j], end=" ")
              else:
                  print(f"\033[1;34;40m{tablero_seleccionado[i][j]}\033[0;0m", end=" ")
      print("|")
  print("−−−−−−−−−−−−−−−−−−−−−−−−−−−")
  print('\033[1;36mexit\033[0;0m')
############## 
def print_tablero_solu(tablero_seleccionado,nombre_tablero,tablero_bool):
  '''Imprime el tablero seleccionado mediante un random'''
  print(f'\033[1;36m{nombre_tablero} SOLUCION .__.\033[0;0m'.center(40))
  print("  | 1 2 3 | 4 5 6 | 7 8 9 |")
  for i in range(9):
      if i%3==0:
          print("−−−−−−−−−−−−−−−−−−−−−−−−−−−")
      print(i+1, end=" ")
      for j in range(9):
          if j%3==0:
              print("|", end=" ")
          if tablero_seleccionado[i][j] == 0:
              print(".", end=" ")
          else:
              if (tablero_bool[i][j] and tablero_seleccionado[i][j]) != 0:
                  print(tablero_seleccionado[i][j], end=" ")
              else:
                  print(f"\033[1;34;40m{tablero_seleccionado[i][j]}\033[0;0m", end=" ")
      print("|")
  print("−−−−−−−−−−−−−−−−−−−−−−−−−−−")
  print('\033[1;36mregresar | guardar\033[0;0m')

def casilla_ocupada(tablero_seleccionado,entrada_fila,entrada_columna):
    '''Verifica si la casilla esta ocupada'''
    if tablero_seleccionado[entrada_fila-1][entrada_columna-1]!=0:
        return True
    else:
        return False
def se_repite_cifra_en_fila(tablero_seleccionado,entrada_fila,entrada_columna,digito):
    '''Verifica si el digito se repite en la fila'''
    for i in range(9):
        if tablero_seleccionado[entrada_fila-1][i]==digito:
            return True
    return False
def se_repite_cifra_en_columna(tablero_seleccionado,entrada_fila,entrada_columna,digito):
    '''Verifica si el digito se repite en la columna'''
    for i in range(9):
        if tablero_seleccionado[i][entrada_columna-1]==digito:
            return True
    return False
def se_repite_cifra_en_cuadricula(tablero_seleccionado,entrada_fila,entrada_columna,digito):
    '''Verifica si el digito se repite en la cuadricula'''
    for i in range(3):
        for j in range(3):
            if tablero_seleccionado[(entrada_fila-1)//3*3+i][(entrada_columna-1)//3*3+j]==digito:
                return True
    return False
def tablero_completo(tablero_seleccionado):
  '''Chequea si el tablero esta completo'''
  for i in range(9):
    for j in range(9):
      if tablero_seleccionado[i][j]==0:
        return False
  return True
def entrada_fuera_de_rango(entrada_datos):
    '''Verifica si la entrada esta fuera de rango'''
    entrada_fila,entrada_columna,digito=entrada_datos.split(' ') #separo la entrada en fila, columna y digito
    if int(entrada_fila)<1 or int(entrada_fila)>9 or int(entrada_columna)<1 or int(entrada_columna)>9 or int(digito)<1 or int(digito)>9:
        return True
    else:
        return False
def entrada_invalida(entrada_datos):
    '''Verifica si se introdugeron valores invalidos'''
    if entrada_datos[1]!=" " or entrada_datos[3]!=" " or entrada_datos[0].isnumeric()==False or entrada_datos[2].isnumeric()==False or entrada_datos[4].isnumeric()==False or entrada_datos[0]=="0" or entrada_datos[2]=="0" or entrada_datos[4]=="0":
        return True
    else:
        return False
def entrada_vacia(entrada_datos):
    '''Verifica si la entrada esta vacia'''
    if entrada_datos=="":
        return True
    else:
        return False
def cumple_reglas_del_juego(tablero_bool,tablero_seleccionado,entrada_fila,entrada_columna,digito):
    '''Verifica si el digito cumple las reglas del juego'''
    if not puede_modificar_el_digito(tablero_bool,entrada_fila,entrada_columna) and casilla_ocupada(tablero_seleccionado,entrada_fila,entrada_columna):
        print('\033[1;31m[!] Esta casilla no es modificable\033[0;m')
        return False
    elif se_repite_cifra_en_fila(tablero_seleccionado,entrada_fila,entrada_columna,digito) and se_repite_cifra_en_columna(tablero_seleccionado,entrada_fila,entrada_columna,digito) and se_repite_cifra_en_cuadricula(tablero_seleccionado,entrada_fila,entrada_columna,digito):
        print('Jugada invalida: \033[1;31mLa cifra se repite en la fila, columna y cuadricula\033[0;0m')
        return False
    elif se_repite_cifra_en_fila(tablero_seleccionado,entrada_fila,entrada_columna,digito) and se_repite_cifra_en_columna(tablero_seleccionado,entrada_fila,entrada_columna,digito):
        print('Jugada invalida: \033[1;31mLa cifra se repite en la fila y columna\033[0;0m')
        return False
    elif se_repite_cifra_en_fila(tablero_seleccionado,entrada_fila,entrada_columna,digito) and se_repite_cifra_en_cuadricula(tablero_seleccionado,entrada_fila,entrada_columna,digito):
        print('Jugada invalida: \033[1;31mLa cifra se repite en la fila y cuadricula\033[0;0m')
        return False
    elif se_repite_cifra_en_columna(tablero_seleccionado,entrada_fila,entrada_columna,digito) and se_repite_cifra_en_cuadricula(tablero_seleccionado,entrada_fila,entrada_columna,digito):
        print('Jugada invalida: \033[1;31mLa cifra se repite en la columna y cuadricula\033[0;0m')
        return False
    elif se_repite_cifra_en_fila(tablero_seleccionado,entrada_fila,entrada_columna,digito):
        print('Jugada invalida: \033[1;31mLa cifra se repite en la fila\033[0;0m')
        return False
    elif se_repite_cifra_en_columna(tablero_seleccionado,entrada_fila,entrada_columna,digito):
        print('Jugada invalida: \033[1;31mLa cifra se repite en la columna\033[0;0m')
        return False
    elif se_repite_cifra_en_cuadricula(tablero_seleccionado,entrada_fila,entrada_columna,digito):
        print('Jugada invalida: \033[1;31mLa cifra se repite en la cuadricula\033[0;0m')
        return False
    for i in range(9):
        if tablero_seleccionado[entrada_fila-1][i]==digito:
            print("Jugada invalida:\033[1;31m Se repite cifra en la misma fila\033[0m")
            return False
    for i in range(9):
        if tablero_seleccionado[i][entrada_columna-1]==digito:
            print("Jugada invalida:\033[1;31m Se repite cifra en la misma columna\033[0m")
            return False
    for i in range(3):
        for j in range(3):
            if tablero_seleccionado[(entrada_fila-1)//3*3+i][(entrada_columna-1)//3*3+j]==digito:
                print("Jugada invalida:\033[1;31m Se repite cifra en la misma cuadricula\033[0m")
                return False
    return True
def retardar_impresion_string(string):
    '''Funcion que imprime letra por letra un string'''
    import time
    for caracter in string:
        print(caracter, end='', flush=True)
        time.sleep(0.1)
    print()
def convertir_tablero_a_bool(tablero_seleccionado):
    temp = tablero_seleccionado.copy()
    tablero_bool=[]
    for i in temp:
        fila_bool = list(map(bool,i))
        tablero_bool.append(fila_bool)
    return tablero_bool
def puede_modificar_el_digito(tablero_bool,entrada_fila,entrada_columna):
    if tablero_bool[entrada_fila-1][entrada_columna-1]==False:
        return True
    else:
        return False


def guardardatos(tablero_guardado, nombre):
    import os
    # si el archivo package.json no existe, lo crea
    if not os.path.exists('package.json'):
        with open('package.json', 'w') as f:
            f.write('{}')
    with open("package.json", "r") as z:
                datos = z.read()
                diccionario = json.loads(datos)
    diccionario[nombre] = tablero_guardado
    with open("package.json","w") as f:
            json.dump(diccionario, f)
def guardardatosbool(tablero_bool,nombre_bool):
    import os
    with open("package.json", "r") as z:
            datos = z.read()
            diccionario = json.loads(datos)
    diccionario[nombre_bool] = tablero_bool
    with open("package.json","w") as f:
        json.dump(diccionario, f)

def leerdatos(clave):
    import os
    with open("package.json", "r") as f:
        datos = f.read()
    dicc = json.loads(datos)
    lista = dicc[clave]
    return lista


def leerdatosbool(clavebool):
    import os
    with open("package.json", "r") as f:
        datos = f.read()
        dicc = json.loads(datos)
    lista = dicc[clavebool]
    return lista

def mostrar_tablero_guardado(clave):
    import json
    import os
    if os.path.exists("package.json"):
        with open("package.json", "r") as f:
            datos = f.read()
        dicc = json.loads(datos)
        lista = dicc[clave]
        return lista
    else:
        print("No existe el archivo")
        return False

def menu_previo():
    import os
    import time
    from menus import menu_pause
    time.sleep(0.5)
    os.system('clear')
    print('''\033[1;35m\n[*] DIFICULTAD DEL TABLERO: \033[1;m
      \033[1;36m[1] Fácil\033[0;m
      \033[1;32m[2] Normal\033[0;m
      \033[1;33m[3] Difícil\033[0;m
      \033[1;31m[4] Experto\033[0;m
    Si preciona ENTER sin ingresar un numero,
    se seleccionara la dificultad por defecto (Facil)...''')
    dificultad_tablero = input('\033[1;35m\n[*] Seleccione una dificultad: \033[1;m')
    while dificultad_tablero not in ['1','2','3','4','', 'prueba']:
        print('\033[1;31m\n[!] Opción inválida\033[0m')
        time.sleep(0.5)
        os.system('clear')
        menu_previo()
    time.sleep(0.5)
    os.system('clear')
    nombre_jugador = input("\033[1;32;40m \n Nombre del jugador: \033[0;37;40m")
    nombre_tablero = input("\033[1;36;40m Nombre del tablero: \033[0;37;40m")
    time.sleep(0.5)
    os.system('clear')
    time.sleep(0.6)
    print('\033[1;32m\n[*] ¡Comencemos!\033[0m')
    time.sleep(0.3)
    os.system('clear')
    return dificultad_tablero, nombre_jugador, nombre_tablero
def mostraropciones():
    import os
    with open("package.json", "r") as z:
        datos = z.read()
        diccionario = json.loads(datos)
    print('\nNombres de los tableros disponibles:' ) 
    contador=0
    for key in diccionario:
        if contador%2==0:
          print(key)
        contador+=1

def empezar_partida(): ################ Aqui esta toda la logica del juego
    '''Funcion que inicia el juego'''
    import os
    import time
    from menus import menu_pause
    from menus import iniciar_juego
    dificultad_tablero, nombre_jugador, nombre_tablero = menu_previo()
    nombre_bool = nombre_tablero + '.bool'
    tablero_seleccionado = generar_tablero_incompleto_valido(dificultad_tablero)
    tablero_bool = convertir_tablero_a_bool(tablero_seleccionado)
    guardardatos(tablero_seleccionado, nombre_tablero)
    guardardatosbool(tablero_bool,nombre_bool)
    print_tablero(tablero_seleccionado,nombre_tablero,tablero_bool)
    while not tablero_completo(tablero_seleccionado):
        entrada_datos = input("Ingrese la fila, columna y digito: ")
        entrada_datos = entrada_datos.strip()
        if entrada_datos == 'exit':
            print('Guardando tablero...')
            time.sleep(1.5)
            os.system('clear')
            print('Tablero guardado')
            time.sleep(1.5)
            os.system('clear')
            iniciar_juego()
        elif entrada_datos == 'el pueblo pide awa':
            tablero_solu_temp = tablero_seleccionado.copy()
            tablero_bool_temp = tablero_bool.copy()
            tablero_solu_temp = resolver_tablero(tablero_solu_temp)
            print_tablero_solu(tablero_solu_temp,nombre_tablero,tablero_bool_temp)
            return
            time.sleep(5.5)
            continue
        elif entrada_vacia(entrada_datos):
            print("Jugada invalida: \033[1;31mNo se ingresaron datos\033[0m")
            continue
        elif len(entrada_datos) != 5:
            print("Jugada invalida: \033[1;31m[!] La entrada debe contener tres numeros\033[0m") ###### Corregir aqui el mensaje
            continue
        elif entrada_fuera_de_rango(entrada_datos)==True:
            print('Jugada invalida: \033[1;31m[!] Entradas numericas fuera del rango\033[0;0m')
            continue
        elif entrada_invalida(entrada_datos):
            print("Jugada invalida: \033[1;31m[!] La entrada no es valida\033[0m")
            continue
        entrada_fila,entrada_columna,digito = entrada_datos.split(' ')
        entrada_fila = int(entrada_fila.strip())
        entrada_columna = int(entrada_columna.strip())
        digito = int(digito.strip())
        if cumple_reglas_del_juego(tablero_bool,tablero_seleccionado,entrada_fila,entrada_columna,digito) and puede_modificar_el_digito(tablero_bool,entrada_fila,entrada_columna):
            tablero_seleccionado[entrada_fila-1][entrada_columna-1]=digito
            guardardatos(tablero_seleccionado, nombre_tablero)
            guardardatosbool(tablero_bool, nombre_bool)
            time.sleep(0.5)
            os.system('clear')
            print_tablero(tablero_seleccionado,nombre_tablero,tablero_bool)
    print('''\033[1;36m
    █▀▀ █▀▀ █░░ █ █▀▀ █ █▀▄ ▄▀█ █▀▄ █▀▀ █▀ █ █ █
    █▀░ ██▄ █▄▄ █ █▄▄ █ █▄▀ █▀█ █▄▀ ██▄ ▄█ ▄ ▄ ▄\033[0m''')
    print("Felicidades, has ganado!")
    print("Nombre del jugador: ",nombre_jugador)
    print("Nombre del tablero: ",nombre_tablero)
    print("Dificultad del tablero: ",dificultad_tablero)

def continuar_partida():
    import os
    import time
    from menus import menu_pause
    from menus import iniciar_juego
    mostraropciones()
    nombre_jugador = input("\033[1;32;40m \n Nombre del jugador: \033[0;37;40m")
    nombre_tablero = input("\033[1;31m\n[!] Coloque el nombre del tablero que desea jugar: \033[0m")
    nombre_bool= nombre_tablero +".bool"
    tablero_continuado = leerdatos(nombre_tablero)
    tablero_bool = leerdatosbool(nombre_bool)
    guardardatos(tablero_continuado, nombre_tablero)
    guardardatosbool(tablero_bool, nombre_bool)
    #print_tablero(tablero_continuado, nombre_tablero, tablero_bool)
    print_tablero(tablero_continuado, nombre_tablero, tablero_bool)
    while not tablero_completo(tablero_continuado):
        entrada_datos = input("Ingrese la fila, columna y digito: ")
        entrada_datos = entrada_datos.strip()
        if entrada_datos == 'exit':
            print('Guardando tablero...')
            time.sleep(1.5)
            os.system('clear')
            print('Tablero guardado')
            time.sleep(1.5)
            os.system('clear')
            iniciar_juego()
        elif entrada_datos == 'el pueblo pide awa':
            tablero_solu_temp = tablero_continuado.copy()
            tablero_bool_temp = tablero_bool.copy()
            tablero_solu_temp = resolver_tablero(tablero_solu_temp)
            print_tablero_solu(tablero_solu_temp, nombre_tablero, tablero_bool_temp)
            continue
        elif entrada_vacia(entrada_datos):
            print("Jugada invalida: \033[1;31mNo se ingresaron datos\033[0m")
            continue
        elif len(entrada_datos) != 5:
            print(
                "Jugada invalida: \033[1;31m[!] La entrada debe contener tres numeros\033[0m")  ###### Corregir aqui el mensaje
            continue
        elif entrada_fuera_de_rango(entrada_datos) == True:
            print('Jugada invalida: \033[1;31m[!] Entradas numericas fuera del rango\033[0;0m')
            continue
        elif entrada_invalida(entrada_datos):
            print("Jugada invalida: \033[1;31m[!] La entrada no es valida\033[0m")
            continue
        entrada_fila, entrada_columna, digito = entrada_datos.split(' ')
        entrada_fila = int(entrada_fila.strip())
        entrada_columna = int(entrada_columna.strip())
        digito = int(digito.strip())
        if cumple_reglas_del_juego(tablero_bool, tablero_continuado, entrada_fila, entrada_columna,
                                   digito) and puede_modificar_el_digito(tablero_bool, entrada_fila, entrada_columna):
            tablero_continuado[entrada_fila - 1][entrada_columna - 1] = digito
            guardardatos(tablero_continuado,nombre_tablero)
            guardardatosbool(tablero_bool, nombre_bool)
            time.sleep(0.5)
            os.system('clear')
            # guardar_tablero(tablero_seleccionado,nombre_tablero)
            print_tablero(tablero_continuado, nombre_tablero, tablero_bool)
    print('''\033[1;36m
        █▀▀ █▀▀ █░░ █ █▀▀ █ █▀▄ ▄▀█ █▀▄ █▀▀ █▀ █ █ █
        █▀░ ██▄ █▄▄ █ █▄▄ █ █▄▀ █▀█ █▄▀ ██▄ ▄█ ▄ ▄ ▄\033[0m''')
    print("Felicidades, has ganado!")
    print("Nombre del jugador: ", nombre_jugador)
    print("Nombre del tablero: ", nombre_tablero)

def easter_egg():
    from menus import retardar_impresion_string
    import os
    import time
    time.sleep(0.8)
    os.system('clear')
    print('''                                                                   
                           .**********,,.                             
                        .*/////***********,                           
                     .///(////**********/**,*,,                       
                    /((((/(#************///*///.                      
                   .//((((&&%//**/*/*/*#&&//(#(/*                     
                    *(/((/*//////***///*****//(//                     
                     .//(/*/(//*/(((*/*//***//*/                      
                      //(((////&&##&&(,**////*,(                      
                    ,///*/*/**(#%&&##/***/*****,.                     
                  .*/******/////*/*//////////**,,.                    
                 ***///(//*/******//***/**///**/**,.                  
                *////////*****************///(/**/*,,                 
               /////////**/(/**************//((///*..*                
              ///////////(((**************/////////*****..            
             ,/*****/////#(//*************////*//////(///(            
             /*******//((/#((*****************/(/(((/(#(//            
           ***********((((////********//*//*****,(/.                  
         (/*****//*/*/(////////*******///////*****                    
         ##((/**///(#((////////******///////////**                    
             ///*((((((((///////*/////((//(((///**                    
                    /#####((((/////////(((((((///,                    
                   /(######((((##(((/(((((##((//(,                    
                     ,##%#####(###((((((####(((/*                     
                      *(############(#######(#(/                      
            ''')
    time.sleep(0.8)
    retardar_impresion_string('\033[1;31mTe quiero mucho profe Nuñez:)\033[0m'.center(70))
    time.sleep(0.5)
    os.system('clear')
    retardar_impresion_string('''\033[1;32mdeveloped by: CaleIsaCh and another person\033[0m'''.center(70))
    retardar_impresion_string('''\033[1;36mwith the help of: Ramos, Gonzalo, Angel, Naoki y Chipana.\033[0m'''.center(70))
    time.sleep(0.5)
    retardar_impresion_string('''\033[1;33mThanks to: The internet, google, stackoverflow, youtube, etc.\033[0m'''.center(70))
    time.sleep(0.5)
    retardar_impresion_string('\033[1;31m\n[*] Finalizando programa...\033[0m '.center(70))
    time.sleep(0.5)
    os.system('clear')
    exit()