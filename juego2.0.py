import numpy as np
import random

def inicio():
    # ESCOGE QUIEN JUEGA PRIMERO Y CREA LA MATRIZ DEL TRICKI
    global jugador, maquina, juego_posiciones

    jugador = random.randint(1, 2)
    maquina = 1 if jugador == 2 else 2
    juego_posiciones = np.zeros((3, 3))

def rectificar_posiciones(x, y):
    return juego_posiciones[x, y] == 0

def verificar_victoria():
    for i in range(3):
        # Verifica filas y columnas
        if all(juego_posiciones[i, :] == jugador) or all(juego_posiciones[:, i] == jugador):
            return jugador
        if all(juego_posiciones[i, :] == maquina) or all(juego_posiciones[:, i] == maquina):
            return maquina
    # Verifica diagonales
    if all(np.diag(juego_posiciones) == jugador) or all(np.diag(np.fliplr(juego_posiciones)) == jugador):
        return jugador
    if all(np.diag(juego_posiciones) == maquina) or all(np.diag(np.fliplr(juego_posiciones)) == maquina):
        return maquina
    # Verifica empate
    if not np.any(juego_posiciones == 0):
        return 0
    return None

def movimientos():
    print(f"Eres el jugador {jugador}")
    while True:
        # Turno del jugador
        while True:
            try:
                print("Escoje una posicion, primero di la fila y luego la columna (1-3)")
                x = int(input("Fila: ")) - 1
                y = int(input("Columna: ")) - 1
                if x not in range(3) or y not in range(3) or not rectificar_posiciones(x, y):
                    raise ValueError("Posición inválida")
                break
            except ValueError as e:
                print(e)
        juego_posiciones[x, y] = jugador
        print("\n" * 3, juego_posiciones)
        ganador = verificar_victoria()
        if ganador is not None:
            break
        
        # Turno de la máquina
        while True:
            jugada_maquinax = random.randint(0, 2)
            jugada_maquinay = random.randint(0, 2)
            if rectificar_posiciones(jugada_maquinax, jugada_maquinay):
                break
        juego_posiciones[jugada_maquinax, jugada_maquinay] = maquina
        print("\n" * 3, juego_posiciones)
        ganador = verificar_victoria()
        if ganador is not None:
            break

    if ganador == 0:
        print("¡Es un empate!")
    else:
        print(f"¡El jugador {ganador} ha ganado!")

inicio()
movimientos()
