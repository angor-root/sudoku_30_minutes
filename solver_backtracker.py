"""developed by: CaleIsaCh and another person"""
import time
def tablero_resuelto(sudoku):
    """Verifica si un sudoku está resuelto. Solo buca ceros en el tablero.
    Al igual que la funcion tablero_completo"""
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return False
    return True
def es_valido(sudoku, fila, columna, numero):
    """Verifica si un número es válido, de acuerdo a las reglas del sudoku."""
    # Verifica si el número está en la fila
    for i in range(9):
        if sudoku[fila][i] == numero:
            return False
    # Verifica si el número ya está en la columna
    for i in range(9):
        if sudoku[i][columna] == numero:
            return False
    # Verifica si el número ya está en el cuadrante
    cuadrante_fila = fila // 3
    cuadrante_columna = columna // 3
    for i in range(cuadrante_fila * 3, cuadrante_fila * 3 + 3):
        for j in range(cuadrante_columna * 3, cuadrante_columna * 3 + 3):
            if sudoku[i][j] == numero:
                return False
    # El número es válido
    return True
def resolver_tablero(sudoku):
    """Resuelve un sudoku.
    Devuelve True si se pudo resolver, False si no se pudo resolver."""
    # Verifica si el sudoku ya está resuelto
    if tablero_resuelto(sudoku):
        return sudoku
    # Busca la primera celda vacía
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                # Recorre los números del 1 al 9
                for k in range(1, 10):
                    # Verifica si el número es válido
                    if es_valido(sudoku, i, j, k):
                        # Asigna el número a la celda
                        sudoku[i][j] = k
                        # Resuelve el sudoku
                        sudoku = resolver_tablero(sudoku)
                        # Verifica si el sudoku está resuelto
                        if tablero_resuelto(sudoku):
                            return sudoku
                        # Restaura la celda
                        sudoku[i][j] = 0
                # No hay solución
                return sudoku
    # No hay solución
    return sudoku

def generar_tablero_completo():
    import random
    """Genera un tablero con algunas celdas completas validas."""
    # Genera un tablero válido
    sudoku = [[0 for i in range(9)] for j in range(9)] # tablero vacio
    for i in range(13): # numeros aleatorios, pero algunos se pierden al no ser validos
        a = random.randint(0, 8)
        b = random.randint(0, 8)
        c = random.randint(1, 9)
        sudoku[a][b] = c if es_valido(sudoku, a, b, c) else 0 # asigna un numero valido
    return sudoku
def generar_tablero_incompleto_valido(dificultad):
    """Genera un tablero incompleto válido a partir
    de un tablero completo válido. Elimina celdas aleatorias
    dependiendo de la dificultad."""
    import random
    # Genera un tablero válido
    tablero_seleccionado = resolver_tablero(generar_tablero_completo())
    # Elimina números
    if dificultad == '1' or dificultad == '':
        for i in range(35):
            a = random.randint(0, 8)
            b = random.randint(0, 8)
            tablero_seleccionado[a][b] = 0
    elif dificultad == '2':
        for i in range(45):
            a = random.randint(0, 8)
            b = random.randint(0, 8)
            tablero_seleccionado[a][b] = 0
    elif dificultad == '3':
        for i in range(55):
            a = random.randint(0, 8)
            b = random.randint(0, 8)
            tablero_seleccionado[a][b] = 0
    elif dificultad == '4': 
        for i in range(64):
            a = random.randint(0, 8)
            b = random.randint(0, 8)
            tablero_seleccionado[a][b] = 0
    elif dificultad == 'prueba':
        tablero_seleccionado = [[2, 1, 0, 3, 5, 6, 7, 8, 9], [5, 7, 8, 1, 2, 9, 3, 6, 4], [6, 3, 9, 4, 7, 8, 5, 1, 2], [4, 2, 5, 6, 9, 1, 8, 3, 7], [1, 9, 6, 7, 8, 3, 2, 4, 5], [3, 8, 7, 2, 4, 5, 6, 9, 1], [7, 4, 1, 8, 6, 2, 9, 5, 3], [8, 5, 3, 9, 1, 7, 4, 2, 6], [9, 6, 2, 5, 3, 4, 1, 7, 8]]
    return tablero_seleccionado

def print_tablero(sudoku):
    """Imprime un tablero."""
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end=' ')
        print()
