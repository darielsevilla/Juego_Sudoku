# This is a sample Python script.
from numpy import random


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def distribucion(tablero):
    fil = random.randint(9)
    col = random.randint(9)
    elemento = random.randint(9)+1

    tableroDistribuido = tablero





def inputUsuario(tablero):
    print("")
def validacion(tablero, elemento, fil, col):
    #revisando columnas
    analisis = tablero
    for i in range(9):
        if(tablero[i][col] == elemento):
            for j in range(9):
                if(analisis[i][j] != 0):
                    analisis[i][j] = -1
    #revisando filas
    for j in range(9):
        if(tablero[fil][j] == elemento):
            for i in range(9):
                if (analisis[i][j] != 0):
                    analisis[i][j] = -1


    for regX in range(3):
        for regY in range(3):
            #revisando casillas del cuadrante
            existe = False
            for i in range(3):
                for j in range(3):
                    if (analisis[i+(regX*3)][j+(regY*3)] == elemento):
                        existe = True

            if(existe):
                for i in range(3):
                    for j in range(3):
                        if (analisis[i + (regX*3)][j + (regY*3)] != 0):
                            analisis[i+(regX*3)][j+(regY*3)] = -1


    if(analisis[fil][col] != -1):
        return True
    else:
        return False

def victoria(tablero):
    print("")


def printTablero(tablero):
    for i in range(9):
        for j in range(9):
            print("[" + str(tablero[i][j]) + "]", end=" ")
        print("")

def sudoku():
    tablero = [[0 for i in range(9)] for j in range(9)]
    printTablero(tablero)
    while(victoria(tablero) != False):
        numero = int(input())
        fila = int(input())
        columna = int(input())
        if validacion(tablero, numero, fila, columna):
            print("Numero correcto")
            # poner el numero en la matriz
        else:
            print("Numero incorrecto")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sudoku()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
