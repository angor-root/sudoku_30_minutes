"""developed by: CaleIsaCh and another person"""
import random
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


