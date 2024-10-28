# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def validacion(tablero):
    print("w")

def victoria(tablero):


def printTablero(tablero):
    for i in range(8):
        for j in range(8):
            print(tablero[i][j], end = " ")

def sudoku():
    tablero = [[0 for i in range(9)] for j in range(9)]
    for i in range(8):
        for j in range(8):
            tablero[i][j] = 0

    printTablero(tablero)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sudoku()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
