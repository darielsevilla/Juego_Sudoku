
import numpy
import random

def validacion(tablero, elemento, fil, col):

    for i in range(9):
        if(tablero[i][col] == elemento):
            return False

    for j in range(9):
        if(tablero[fil][j] == elemento):
            return False

    for regX in range(3):
        for regY in range(3):
            existe = False
            for i in range(3):
                for j in range(3):
                    if(fil >= (regX*3) and fil <= (regX*3) +2 and col >= (regY*3) and col <= (regY*3)+2):
                        if (tablero[i+(regX*3)][j+(regY*3)] == elemento):
                            return False

    return True

def distribucion2(tablero):
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:  
                
                numeros = [0,0,0,0,0,0,0,0,0]
                for num in range(9):
                    numero = random.randint(1,9)
                    while numero in numeros:
                        numero = random.randint(1, 9)
                    numeros[num] = numero

                for num in numeros:
                    if validacion(tablero, num, i, j):
                        tablero[i][j] = num  

                        if distribucion2(tablero):
                            return True

                        tablero[i][j] = 0

                return False

    return True

def victoria(tablero2):
    for i in range(9):
        for j in range(9):
            if tablero2[i][j]==0:
                return False
    return True

def printTablero(tablero):
    for i in range(9):
        if(i % 3 == 0):
            for p in range(10):
                print(" - ", end=" ")

            print("")
        for j in range(9):
            if(j % 3 == 0 and j != 0):
                print("|", end = " ")
            if(tablero[i][j] == 0):
                print("[ ]", end=" ")
            else:
                print("[" + str(tablero[i][j]) + "]", end=" ")
        print("")

def ocultar(tablero, tablero2):
    contador=0
    while contador < 20:
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        while(tablero2[i][j] != 0):
            i = random.randint(0, 8)
            j = random.randint(0, 8)
        tablero2[i][j]=tablero[i][j]
        contador+=1


def sudoku():
    tablero = [[0 for i in range(9)] for j in range(9)]
    tablero2 = [[0 for i in range(9)] for j in range(9)]

    print()
    distribucion2(tablero)

    ocultar(tablero, tablero2)
    print()

    victory = False
    while(victory == False):
        printTablero(tablero2)
        print("1) ingresar numero")
        print("2) salir")
        op = int(input("Ingrese opcion: "))

        if op == 1:
            numero = int(input("Ingrese un numero: "))
            fila = int(input("Fila: "))
            columna = int(input("Columna: "))
            if(fila >= 0 and fila <= 8 and columna >= 0 or columna <= 8):
                if validacion(tablero2, numero, fila, columna):
                    print("Numero Valido")
                    tablero2[fila][columna]=numero
                    victory = victoria(tablero2)
                else:
                    print("*Numero incorrecto*")
            else:
                print("*Coordenadas Invalidas*")
        elif op == 2:
            break
        else:
            print("*Opcion invalida*")

    if(victory == True):
        print("Ha Ganado!!!")
    else:
        print("Ha perdido")

if __name__ == '__main__':
    sudoku()