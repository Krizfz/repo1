from funciones import *
from variables import TABLERO

# tablero_maquina = TABLERO
tablero_jugador = TABLERO

print("Hola bienvenido al juego de hlf!")

colocar_barco(tablero=tablero_jugador)

print("Disfruta!")
counter = 0

print(tablero_jugador)

while "O" in tablero_jugador and counter < 5:
    disparar(tablero=tablero_jugador)
    print(tablero_jugador)
    counter += 1
    if "O" not in tablero_jugador and counter < 5:
        print("Has ganado!")
        break

if "O" in tablero_jugador:
    print("Has perdido!")