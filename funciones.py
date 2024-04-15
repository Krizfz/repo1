import numpy as np

def init_tablero(size = (10, 10), fill = " "):
    tablero = np.full(size, fill)
    return tablero

def colocar_barco(tablero, size = 4):
    coord_x_tab = int(np.random.randint(0, 10))
    coord_y_tab = int(np.random.randint(0, 10))

    orien = np.random.choice(["E", "S"])
    print("Orien:", orien)
    print("Coord_x:", coord_x_tab, "Coord_y:", coord_y_tab)
    if orien == "E":
        tablero[coord_x_tab, coord_y_tab:coord_y_tab + size] = "O"

    elif orien == "S":
        tablero[coord_x_tab:coord_x_tab + size, coord_y_tab] = "O"

def disparar(tablero):
    coord_x = int(input("Coord X:"))
    coord_y = int(input("Coord Y:"))

    if tablero[coord_x, coord_y] == "O":
        tablero[coord_x, coord_y] = "X"
        print("Has acertado!")

    elif tablero[coord_x, coord_y] == " ":
        tablero[coord_x, coord_y] = "-"
        print("Has fallado!")

    else:
        print("Has repetido el disparo.")

    print(tablero)