'''developed by: CaleIsaCh and another person'''
from solver_backtracker import *
def seleccionar_tablero_facil():
    '''Selecciona un tablero facil al azar'''
    import random
    tablero1 = [[5, 0, 0, 0, 2, 7, 0, 0, 1], [8, 0, 0, 0, 0, 0, 0, 7, 5], [6, 0, 2, 0, 3, 0, 9, 4, 0], [1, 5, 0, 4, 9, 0, 0, 0, 3], [0, 8, 0, 7, 0, 0, 0, 0, 9], [0, 0, 0, 2, 1, 8, 0, 0, 0], [4, 0, 5, 9, 0, 2, 0, 8, 7], [9, 2, 8, 3, 9, 9, 9, 1, 6], [0, 6, 3, 1, 8, 5, 0, 0, 0]]
    tablero2 = [[1, 0, 7, 4, 5, 2, 0, 3, 0], [0, 0, 0, 7, 8, 0, 0, 5, 0], [0, 6, 8, 3, 0, 9, 4, 7, 2], [0, 7, 0, 0, 9, 0, 0, 6, 0], [8, 5, 1, 6, 9, 9, 3, 9, 0], [0, 2, 0, 5, 4, 0, 0, 0, 7], [6, 8, 0, 0, 0, 4, 0, 0, 3], [0, 0, 4, 0, 0, 1, 0, 0, 9], [2, 0, 0, 0, 0, 0, 7, 0, 0]]
    tablero3 = [[1, 0, 7, 6, 8, 3, 0, 4, 0], [0, 4, 2, 9, 1, 0, 0, 0, 6], [0, 6, 8, 0, 0, 7, 0, 3, 0], [0, 0, 0, 1, 3, 2, 7, 9, 0], [0, 0, 0, 0, 0, 8, 0, 2, 1], [2, 0, 9, 7, 6, 0, 3, 8, 0], [4, 7, 3, 0, 0, 0, 0, 0, 8], [8, 0, 0, 0, 0, 0, 0, 6, 0], [9, 0, 0, 0, 7, 0, 0, 0, 3]]
    tablero4 = [[0, 6, 0, 0, 5, 1, 0, 7, 0], [3, 7, 4, 9, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 2], [4, 9, 0, 0, 0, 0, 0, 3, 2], [2, 0, 8, 0, 6, 9, 7, 0, 5], [7, 0, 3, 2, 0, 0, 1, 9, 0], [5, 0, 1, 6, 2, 7, 0, 0, 4], [6, 4, 0, 8, 1, 0, 0, 0, 7], [0, 0, 0, 0, 0, 4, 6, 0, 3]]
    tablero5 = [[9, 0, 6, 0, 4, 5, 0, 8, 1], [0, 0, 0, 0, 2, 0, 4, 3, 0], [4, 0, 0, 8, 0, 1, 0, 2, 6], [0, 6, 8, 9, 1, 0, 0, 0, 7], [0, 0, 0, 0, 0, 4, 0, 6, 3], [0, 0, 0, 6, 0, 7, 1, 9, 0], [6, 0, 0, 4, 7, 0, 3, 1, 2], [2, 1, 0, 5, 0, 0, 6, 0, 0], [0, 0, 4, 1, 0, 0, 0, 0, 0]]
    tablero6 = [[0, 1, 5, 8, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 5, 6, 0, 0], [3, 9, 0, 2, 0, 0, 0, 8, 0], [0, 0, 0, 0, 0, 2, 0, 5, 3], [5, 4, 0, 0, 0, 0, 2, 0, 6], [0, 0, 3, 9, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 9, 4, 0, 0], [0, 5, 2, 0, 3, 7, 9, 6, 8], [9, 7, 4, 0, 2, 8, 0, 1, 5]]
    tablero7 = [[0, 0, 0, 0, 8, 0, 9, 6, 2], [0, 0, 8, 5, 1, 0, 0, 0, 0], [0, 6, 0, 0, 9, 0, 1, 0, 0], [0, 8, 4, 1, 6, 9, 7, 0, 3], [3, 0, 0, 7, 0, 0, 2, 1, 0], [0, 0, 7, 0, 2, 0, 4, 0, 0], [0, 0, 1, 2, 7, 5, 6, 4, 0], [0, 7, 2, 9, 0, 0, 0, 0, 1], [5, 4, 0, 6, 0, 0, 8, 0, 0]]
    tablero8 = [[0, 0, 0, 2, 7, 0, 1, 8, 0], [0, 0, 9, 0, 0, 5, 0, 0, 0], [8, 0, 0, 0, 0, 0, 5, 0, 7], [9, 3, 0, 0, 0, 0, 0, 2, 0], [4, 5, 0, 7, 0, 8, 6, 9, 1], [6, 8, 0, 4, 9, 2, 7, 0, 3], [0, 0, 8, 9, 5, 0, 0, 0, 6], [7, 0, 0, 0, 0, 0, 0, 1, 0], [2, 0, 6, 3, 0, 7, 0, 0, 0]]
    tablero9 = [[0, 0, 0, 4, 0, 9, 8, 0, 2], [5, 7, 0, 3, 8, 0, 0, 0, 4], [0, 0, 0, 0, 0, 2, 5, 0, 0], [3, 2, 8, 0, 1, 7, 0, 6, 0], [0, 5, 7, 9, 3, 0, 0, 0, 0], [9, 0, 0, 0, 2, 0, 7, 3, 0], [7, 8, 0, 1, 0, 0, 0, 0, 0], [6, 0, 5, 2, 0, 8, 0, 0, 0], [0, 9, 4, 0, 7, 3, 0, 5, 0]]
    tablero10 = [[8, 4, 0, 3, 6, 5, 2, 0, 9], [3, 1, 0, 7, 0, 0, 0, 0, 0], [6, 9, 0, 0, 2, 1, 8, 3, 7], [0, 0, 3, 0, 0, 0, 0, 0, 4], [0, 0, 0, 9, 5, 0, 7, 2, 0], [9, 0, 0, 0, 4, 2, 0, 0, 0], [2, 0, 0, 5, 0, 0, 0, 0, 0], [0, 0, 9, 0, 0, 6, 3, 4, 0], [7, 0, 6, 0, 0, 0, 1, 0, 2]]
    tableros= [tablero1,tablero2,tablero3,tablero4,tablero5,tablero6,tablero7,tablero8,tablero9,tablero10]
    tablero_seleccionado = random.choice(tableros)
    return tablero_seleccionado

def seleccionar_tablero_normal():
    '''Selecciona un tablero de la lista de tableros de dificultad normal'''
    import random
    tablero1 = [[4, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6], [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    tablero2 = [[6, 5, 3, 1, 8, 7, 4, 0, 0], [8, 9, 2, 6, 4, 3, 1, 7, 5], [0, 7, 0, 9, 0, 0, 0, 8, 0], [3, 0, 8, 0, 0, 9, 0, 0, 1], [1, 0, 7, 0, 3, 2, 0, 0, 8], [5, 0, 9, 8, 0, 1, 4, 6, 0], [7, 1, 6, 3, 9, 8, 2, 5, 4], [0, 8, 4, 0, 5, 6, 0, 1, 3]]
    tablero3 = [[0, 0, 0, 3, 8, 5, 0, 6, 0], [3, 8, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 5], [5, 0, 0, 8, 0, 0, 9, 0, 0], [6, 3, 9, 5, 0, 7, 2, 8, 1], [0, 0, 1, 0, 0, 3, 0, 0, 6], [7, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 2, 8], [0, 4, 0, 9, 3, 2, 0, 0, 0]]
    tablero4 = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6], [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    tablero5 = [[3, 0, 0, 2, 4, 0, 0, 6, 0], [0, 4, 0, 0, 0, 0, 0, 5, 3], [1, 8, 9, 6, 3, 5, 4, 0, 0], [5, 3, 4, 8, 0, 1, 0, 7, 6], [7, 0, 1, 6, 0, 5, 4, 0, 8], [2, 8, 0, 7, 0, 3, 5, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 2], [0, 0, 8, 0, 0, 0, 7, 9, 0], [0, 0, 7, 4, 0, 9, 0, 0, 3]]
    tablero6 = [[5, 0, 0, 0, 8, 6, 0, 0, 1], [0, 0, 2, 7, 0, 1, 6, 0, 0], [0, 7, 1, 0, 0, 0, 2, 5, 0], [9, 1, 0, 0, 2, 0, 0, 7, 0], [3, 0, 0, 1, 4, 5, 0, 0, 6], [0, 6, 0, 0, 9, 0, 0, 2, 4], [0, 5, 3, 0, 0, 0, 4, 6, 0], [0, 0, 8, 9, 0, 3, 5, 0, 0], [2, 0, 0, 5, 1, 0, 0, 0, 7]] # Bien
    tablero7 = [[0, 9, 0, 0, 7, 4, 8, 3, 1], [0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 7, 6, 0, 0, 2, 9, 0, 0], [0, 8, 0, 7, 0, 5, 6, 0, 1], [7, 6, 0, 0, 3, 0, 0, 8, 9], [9, 0, 3, 8, 0, 4, 0, 2, 0], [0, 0, 8, 1, 0, 0, 2, 9, 2], [0, 0, 0, 0, 0, 0, 3, 0, 0], [0, 3, 0, 4, 0, 7, 1, 0, 6]]
    tablero8 = [[0, 8, 0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 8, 4, 0, 9, 0], [0, 0, 6, 3, 2, 0, 0, 1, 0], [0, 9, 7, 0, 0, 0, 0, 8, 0], [8, 0, 0, 9, 0, 3, 0, 0, 2], [0, 1, 0, 0, 0, 0, 9, 5, 0], [0, 7, 0, 0, 4, 5, 8, 0, 0], [0, 3, 7, 1, 0, 0, 0, 0, 0], [0, 0, 8, 0, 0, 0, 0, 4, 0]] # error
    tablero9 = [[0, 3, 0, 0, 0, 7, 0, 0, 2], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 0, 0, 0, 0, 6], [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [5, 0, 0, 0, 8, 0, 0, 7, 9]] # Error
    tablero10 = [[0, 0, 0, 0, 0, 0, 4, 5, 0], [0, 9, 5, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 3, 0, 9, 0], [0, 0, 0, 0, 8, 1, 0, 7, 0], [5, 0, 8, 0, 0, 2, 0, 0, 0], [0, 1, 0, 0, 9, 7, 0, 3, 0], [7, 6, 0, 0, 0, 0, 0, 0, 4], [0, 3, 0, 1, 0, 0, 0, 0, 0], [4, 0, 0, 2, 0, 0, 0, 0, 6]] # BIEN!
    tableros= [tablero1,tablero2,tablero3,tablero4,tablero5,tablero6,tablero7,tablero8,tablero9,tablero10]
    tablero_seleccionado = random.choice(tableros)
    return tablero_seleccionado

def seleccionar_tablero_dificil():
    '''Selecciona un tablero de la lista de tableros dificiles'''
    import random
    tablero1 = [[0, 0, 0, 0, 8, 1, 0, 7, 0], [0, 0, 0, 0, 0, 8, 3, 6, 2], [0, 0, 0, 0, 9, 0, 0, 0, 0], [6,5, 3, 1, 0, 0, 0, 0, 0], [0, 3, 0, 2, 1, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0, 6, 9], [0, 0, 0, 0, 4, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 2, 0, 0, 8, 0, 3]]
    tablero2 = [[6, 0, 0, 0, 0, 0, 0, 0, 9], [0, 0, 9, 3, 6, 2, 0, 4, 0], [0, 0, 7, 0, 8, 0, 0, 0, 0], [0, 0, 0, 4, 0, 0, 9, 0, 0], [8, 4, 0, 0, 0, 0, 0, 0, 5], [0, 0, 0, 1, 0, 3, 0, 0, 6], [0, 0, 0, 0, 2, 0, 0, 0, 0], [6, 0, 8, 7, 0, 5, 0, 0, 0], [5, 0, 0, 3, 0, 9, 1, 6, 0]]
    tablero3 = [[0, 8, 7, 6, 9, 4, 0, 0, 0], [0, 4, 0, 8, 0, 0, 2, 0, 1], [0, 0, 1, 0, 0, 3, 0, 0, 6], [0, 8, 0, 2, 0, 0, 0, 0, 4], [0, 9, 0, 0, 0, 2, 0, 0, 3], [6, 0, 0, 4, 0, 0, 0, 2, 0], [2, 0, 0, 0, 0, 9, 0, 3, 0], [8, 0, 0, 3, 0, 0, 7, 0, 0], [7, 0, 5, 0, 0, 8, 0, 4, 0]]
    tablero4 = [[0, 0, 7, 1, 0, 0, 0, 9, 0], [0, 8, 2, 0, 0, 9, 6, 1, 0], [4, 0, 0, 0, 0, 0, 0, 0, 0], [7, 0, 0, 0, 0, 3, 9, 0, 0], [0, 0, 0, 0, 8, 1, 0, 0, 0], [0, 0, 2, 0, 0, 0, 0, 5, 0], [0, 0, 2, 0, 0, 0, 0, 5, 0], [0, 4, 0, 0, 0, 0, 3, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 2]]
    tablero5 = [[4, 0, 0, 0, 6, 0, 2, 0, 9], [0, 0, 0, 0, 3, 9, 4, 0, 0], [9, 1, 0, 0, 8, 0, 0, 0, 0], [0, 0, 1, 0, 0, 2, 0, 0, 8], [3, 0, 2, 7, 0, 0, 0, 0, 5], [0, 0, 0, 0, 4, 8, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 1, 0], [8, 0, 0, 0, 0, 4, 6, 0, 9]]
    tablero6 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 1, 0], [0, 0, 2, 0, 0, 0, 0, 5, 0], [0, 4, 0, 0, 0, 0, 3, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 2], [9, 0, 8, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 3, 4, 0, 0, 1], [0, 0, 0, 7, 0, 0, 3, 0, 0], [0, 1, 0, 0, 0, 8, 0, 9, 2]]
    tablero7 = [[0, 0, 0, 4, 3, 0, 2, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 6], [0, 0, 0, 5, 0, 9, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 1, 8], [0, 0, 0, 0, 8, 1, 0, 0, 0], [0, 4, 0, 0, 0, 0, 3, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 2], [0, 0, 0, 0, 0, 0, 0, 0, 3], [0, 0, 2, 3, 0, 0, 4, 0, 0]]
    tablero8 = [[0, 0, 1, 8, 0, 0, 0, 0, 5], [0, 6, 0, 0, 7, 0, 8, 0, 0], [4, 0, 0, 0, 0, 0, 0, 0, 0], [7, 0, 0, 0, 0, 8, 9, 0, 0], [0, 0, 0, 5, 0, 7, 0, 0, 0], [0, 0, 1, 3, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 8], [0, 4, 5, 8, 0, 0, 1, 6, 0], [0, 2, 0, 0, 0, 5, 7, 0, 0]]
    tablero9 = [[2, 0, 5, 0, 1, 0, 0, 0, 7], [0, 0, 0, 0, 0, 2, 6, 0, 0], [6, 0, 7, 1, 0, 0, 0, 8, 0], [5, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 7, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 4, 3, 0, 2, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 6], [0, 0, 0, 5, 0, 9, 0, 0, 0]]
    tablero10 = [[0, 0, 7, 1, 0, 0, 0, 9, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 8, 2, 0, 0, 9, 6, 1, 0], [4, 0, 0, 0, 0, 0, 0, 0, 0], [7, 0, 0, 0, 0, 8, 9, 0, 0], [0, 2, 0, 0, 0, 5, 7, 0, 0], [0, 9, 3, 0, 0, 0, 6, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 4, 0, 0, 0, 5, 0]]
    tableros= [tablero1,tablero2,tablero3,tablero4,tablero5,tablero6,tablero7,tablero8,tablero9,tablero10]
    tablero_seleccionado = random.choice(tableros)
    return tablero_seleccionado

def seleccionar_tablero_experto():
    '''Selecciona un tablero de la lista de tableros expertos'''
    import random
    tablero1 = [[0, 0, 5, 7, 0, 0, 2, 4, 0], [0, 0, 0, 0, 0, 4, 6, 0, 7], [2, 0, 0, 0, 0, 3, 0, 0, 0], [5, 8, 0, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 3, 0], [0, 1, 0, 0, 0, 0, 0, 0, 4], [0, 0, 9, 1, 0, 0, 0, 0, 0], [0, 4, 0, 0, 2, 0, 0, 0, 1], [0, 8, 0, 0, 0, 0, 5, 2, 0]]
    tablero2 = [[9, 6, 0, 0, 0, 0, 4, 0, 0], [3, 0, 0, 0, 2, 0, 0, 0, 0], [8, 0, 1, 3, 0, 0, 0, 0, 0], [5, 0, 0, 0, 0, 9, 0, 0, 0], [0, 0, 0, 0, 0, 4, 6, 8, 0], [0, 2, 7, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 5, 0, 0, 0, 0], [1, 6, 2, 4, 0, 0, 0, 0, 0], [0, 9, 8, 1, 0, 0, 0, 0, 0]]
    tablero3 = [[9, 0, 0, 0, 8, 0, 0, 0, 0], [8, 5, 0, 0, 0, 0, 7, 0, 9], [0, 2, 0, 0, 0, 0, 3, 0, 6], [0, 0, 0, 0, 6, 0, 0, 0, 0], [0, 2, 0, 0, 0, 3, 0, 0, 0], [4, 0, 0, 8, 0, 0, 0, 0, 1], [0, 0, 5, 7, 2, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 0, 4, 7], [0, 0, 0, 0, 0, 0, 6, 0, 0]]
    tablero4 = [[0, 0, 0, 0, 1, 8, 0, 0, 0], [0, 0, 0, 0, 0, 0, 8, 0, 4], [0, 3, 2, 0, 0, 0, 0, 0, 6], [0, 0, 0, 0, 8, 0, 3, 7, 0], [1, 4, 0, 0, 7, 0, 2, 0, 0], [0, 0, 0, 4, 0, 0, 0, 0, 0], [0, 0, 1, 6, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 5, 7, 6, 0, 3]]
    tablero5 = [[0, 0, 5, 0, 0, 0, 0, 2, 0], [0, 6, 0, 1, 0, 0, 3, 0, 0], [0, 3, 0, 0, 0, 9, 0, 5, 0], [1, 0, 0, 0, 0, 6, 0, 0, 4], [0, 0, 0, 0, 0, 8, 0, 0, 0], [0, 0, 2, 4, 0, 5, 0, 1, 0], [0, 7, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 4, 9, 8, 0, 7], [8, 0, 0, 0, 0, 0, 1, 0, 0]]
    tablero6 = [[0, 1, 0, 6, 0, 0, 0, 5, 0], [0, 7, 0, 0, 5, 0, 0, 3, 0], [0, 0, 5, 0, 4, 0, 0, 0, 0], [0, 0, 8, 0, 0, 0, 0, 0, 9], [0, 0, 6, 0, 0, 0, 1, 0, 3], [0, 0, 2, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 0, 6, 8, 0, 0], [0, 0, 0, 0, 0, 4, 0, 0, 5], [0, 0, 0, 1, 0, 0, 3, 0, 4]]
    tablero7 = [[0, 6, 0, 0, 4, 2, 1, 9, 0], [0, 0, 0, 0, 0, 5, 0, 0, 0], [0, 0, 3, 6, 0, 0, 0, 0, 4], [0, 8, 0, 7, 0, 0, 0, 0, 0], [1, 3, 0, 0, 0, 0, 0, 6, 4], [0, 0, 0, 0, 0, 2, 5, 0, 0], [0, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 3, 4, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 8, 9, 0]]
    tablero8 = [[0, 0, 5, 9, 0, 2, 0, 7, 0], [3, 0, 7, 5, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0, 0, 1, 6], [0, 3, 0, 6, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 9, 0, 5], [0, 4, 0, 2, 0, 0, 0, 0, 0], [0, 9, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 8, 2], [0, 0, 3, 7, 0, 4, 0, 0, 0]]
    tablero9 = [[2, 4, 7, 0, 0, 0, 0, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [9, 0, 1, 0, 0, 8, 0, 0, 5], [0, 5, 0, 0, 0, 0, 0, 0, 0], [7, 3, 4, 6, 8, 0, 2, 0, 0], [0, 2, 0, 4, 0, 0, 0, 0, 0], [4, 3, 0, 0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 7, 0, 0, 0], [0, 6, 0, 0, 0, 9, 0, 0, 0]]
    tablero10 = [[0, 7, 2, 0, 3, 0, 0, 0, 0], [5, 0, 0, 0, 0, 4, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 4, 1, 5, 7], [0, 0, 0, 7, 3, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [9, 0, 8, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 9, 0, 0], [5, 0, 0, 4, 2, 0, 3, 7, 0]]
    tableros= [tablero1,tablero2,tablero3,tablero4,tablero5,tablero6,tablero7,tablero8,tablero9,tablero10]
    tablero_seleccionado = random.choice(tableros)
    return tablero_seleccionado

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
  print('\033[1;36mpause\033[0;0m')
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
  print('\033[1;36mpause\033[0;0m')


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
    # if casilla_ocupada(tablero_seleccionado,entrada_fila,entrada_columna):
    #    print('Jugada invalida: \033[1;31mLa casilla esta ocupada\033[0;0m')
    #    return False
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
    # if tablero_seleccionado[entrada_fila-1][entrada_columna-1]!=0:
    #     print('\033[1;31m'+"La casilla ya está ocupada, por favor seleccione otra casilla"+'\033[0;m')
    #     return False
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

def guardar_tablero(tablero_guardado, nombre):
    import json
    with open("package.json", "r") as z:
        if z.read == "":
            datos = z.read()
            diccionario = json.loads(datos)
        else:
            diccionario = {}
    diccionario[nombre] = tablero_guardado
    with open("package.json", "w") as f:
        json.dump(diccionario, f)

def mostrar_tablero_guardado(clave):
    import json
    with open("package.json", "r") as f:
        datos = f.read()
    dicc = json.loads(datos)
    lista = dicc[clave]
    return lista


def empezar_partida(): ################ Aqui esta toda la logica del juego
    '''Funcion que inicia el juego'''
    import os
    import time
    from menus import menu_pause
    time.sleep(0.5)
    os.system('cls')
    print('''\033[1;35m\n[*] DIFICULTAD DEL TABLERO: \033[1;m
      \033[1;36m[1] Fácil\033[0;m
      \033[1;32m[2] Normal\033[0;m
      \033[1;33m[3] Difícil\033[0;m
      \033[1;31m[4] Experto\033[0;m
    Si preciona ENTER sin ingresar un numero,
    se seleccionara la dificultad por defecto (Facil)...
''')
    dificultad_tablero = input('\033[1;35m\n[*] Seleccione una dificultad: \033[1;m')
    while dificultad_tablero not in ['1','2','3','4','','prueba']:
        dificultad_tablero = input('\033[1;35m\n[*] Seleccione una dificultad: \033[1;m')
    time.sleep(0.5)
    os.system('cls')
    nombre_jugador = input("\033[1;32;40m \n Nombre del jugador: \033[0;37;40m")
    nombre_tablero = input("\033[1;36;40m Nombre del tablero: \033[0;37;40m")
    time.sleep(0.5)
    os.system('cls')
    #retardar_impresion_string('\033[1;34m\n[*] Cargando tablero...\033[0m') #### Descomentar estas lineas
    #retardar_impresion_string('\033[1;34m\n[?] ¿Preparado?\033[0m')
    #retardar_impresion_string('\033[1;34m\n[!] Prepara tus pantalones\033[0m')
    time.sleep(0.6)
    print('\033[1;32m\n[*] ¡Comencemos!\033[0m')
    time.sleep(0.3)
    os.system('cls')

    if dificultad_tablero == '1' or dificultad_tablero == '':
        tablero_seleccionado = seleccionar_tablero_facil()
    elif dificultad_tablero == '2':
        tablero_seleccionado = seleccionar_tablero_normal()
    elif dificultad_tablero == '3':
        tablero_seleccionado = seleccionar_tablero_dificil()
    elif dificultad_tablero == '4':
        tablero_seleccionado = seleccionar_tablero_experto()
    elif dificultad_tablero == 'prueba':
        tablero_seleccionado=[ [5, 3, 9, 0, 7, 0, 4, 1,3], [6, 2, 8, 3, 1, 4, 9, 6, 5], [7, 4, 1, 0, 9, 0, 7, 2, 8], [4, 6, 2, 5, 3, 9, 8, 7, 1], [3, 8, 5, 7, 2, 1, 6, 4, 9], [1, 9, 7, 4, 6, 8, 2, 5, 3], [2, 5, 6, 1, 8, 7, 3, 9, 4], [9, 1, 3, 2, 4, 6, 5, 8, 7], [8, 7, 4, 9, 5, 3, 1, 2, 6] ] 
    else:
        print('\033[1;31m\n[!] Opción inválida\033[0m')
        time.sleep(0.5)
        os.system('cls')
        empezar_partida()
    tablero_bool = convertir_tablero_a_bool(tablero_seleccionado)
    print_tablero(tablero_seleccionado,nombre_tablero,tablero_bool)
    while not tablero_completo(tablero_seleccionado):
        entrada_datos = input("Ingrese la fila, columna y digito: ")
        entrada_datos = entrada_datos.strip()
        if entrada_datos == 'pause':
            menu_pause()
            if menu_pause() == '1':
                empezar_partida()
            elif menu_pause() == '2':
                return
            elif menu_pause() == '3':
                return
        elif entrada_datos == 'nosabo_aiuda_pe':
            tablero_solu_temp = tablero_seleccionado.copy()
            tablero_bool_temp = tablero_bool.copy()
            tablero_solu_temp = resolver_tablero(tablero_solu_temp)
            print_tablero_solu(tablero_solu_temp,nombre_tablero,tablero_bool_temp)
            print('El pueblo pide awa')
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
            guardar_tablero(tablero_seleccionado, nombre_tablero)
            time.sleep(0.5)
            os.system('cls')
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
    nombre_jugador = input("\033[1;32;40m \n Nombre del jugador: \033[0;37;40m")
    nombre_tablero = input("\033[1;36;40m Nombre del tablero: \033[0;37;40m")
    time.sleep(0.5)
    os.system('cls')
    tablero_continuado = mostrar_tablero_guardado(nombre_tablero)
    os.system('cls')
    tablero_bool = convertir_tablero_a_bool(tablero_continuado)
    print_tablero(tablero_continuado, nombre_tablero, tablero_bool)
    while not tablero_completo(tablero_continuado):
        entrada_datos = input("Ingrese la fila, columna y digito: ")
        entrada_datos = entrada_datos.strip()
        if entrada_datos == 'pause':
            menu_pause()
            if menu_pause() == '1':
                empezar_partida()
            elif menu_pause() == '2':
                return
            elif menu_pause() == '3':
                return
        elif entrada_datos == 'nosabo_aiuda_pe':
            tablero_solu_temp = tablero_continuado.copy()
            tablero_bool_temp = tablero_bool.copy()
            tablero_solu_temp = resolver_tablero(tablero_solu_temp)
            print_tablero_solu(tablero_solu_temp, nombre_tablero, tablero_bool_temp)
            print('El pueblo pide awa')
            time.sleep(5.5)
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
            guardar_tablero(tablero_continuado, nombre_tablero)
            time.sleep(0.5)
            os.system('cls')
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
    os.system('cls')
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
    os.system('cls')
    retardar_impresion_string('''\033[1;32mdeveloped by: CaleIsaCh and another person\033[0m'''.center(70))
    retardar_impresion_string('''\033[1;36mwith the help of: Ramos, Gonzalo, Angel, Naoki y Chipana.\033[0m'''.center(70))
    time.sleep(0.5)
    retardar_impresion_string('''\033[1;33mThanks to: The internet, google, stackoverflow, youtube, etc.\033[0m'''.center(70))
    time.sleep(0.5)
    retardar_impresion_string('\033[1;31m\n[*] Finalizando programa...\033[0m '.center(70))
    time.sleep(0.5)
    os.system('cls')
    exit()