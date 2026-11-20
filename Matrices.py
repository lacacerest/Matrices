filas = int(input("Ingresa el número de filas: "))
columnas = int(input("Ingresa el número de columnas: "))

while filas <= 0 or columnas <= 0:
    print("Las filas y columnas deben ser mayores a cero.")
    filas = int(input("Ingresa el número de filas: "))
    columnas = int(input("Ingresa el número de columnas: "))


# Crear matriz con todos los asientos libres

asientos = []

for i in range(filas):

    fila = []

    for j in range(columnas):
        fila.append("L")

    asientos.append(fila)

def mostrar_sala():

    print("\n========== SALA DE CINE ==========")

    print("    ", end="")

    for j in range(columnas):
        print(f"{j + 1:^5}", end="")

    print()

    for i in range(filas):

        print(f"{i + 1:<4}", end="")

        for j in range(columnas):
            print(f"{asientos[i][j]:^5}", end="")

        print()


def reservar_asiento():

    fila = int(input("Ingresa la fila: "))
    columna = int(input("Ingresa la columna: "))

    # Verificar que el asiento exista

    if fila < 1 or fila > filas or columna < 1 or columna > columnas:

        print("Error: el asiento no existe.")

    else:

        # Convertir a índices de Python

        fila = fila - 1
        columna = columna - 1

        if asientos[fila][columna] == "L":

            asientos[fila][columna] = "X"

            print("¡Asiento reservado correctamente!")

        else:

            print("El asiento ya está ocupado.")

def liberar_asiento():

    fila = int(input("Ingresa la fila: "))
    columna = int(input("Ingresa la columna: "))

    # Verificar que el asiento exista

    if fila < 1 or fila > filas or columna < 1 or columna > columnas:

        print("Error: el asiento no existe.")

    else:

        fila = fila - 1
        columna = columna - 1

        if asientos[fila][columna] == "X":

            asientos[fila][columna] = "L"

            print("¡Asiento liberado correctamente!")

        else:

            print("El asiento ya se encuentra libre.")

def contar_asientos():

    libres = 0
    ocupados = 0

    for i in range(filas):

        for j in range(columnas):

            if asientos[i][j] == "L":

                libres += 1

            else:

                ocupados += 1

    print("Asientos libres:", libres)
    print("Asientos ocupados:", ocupados)
    print("Total de asientos:", libres + ocupados)



while True:

    print("1. Mostrar sala")
    print("2. Reservar asiento")
    print("3. Liberar asiento")
    print("4. Contar asientos ocupados y libres")
    print("5. Salir")

    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":

        mostrar_sala()

    elif opcion == "2":

        reservar_asiento()

    elif opcion == "3":

        liberar_asiento()

    elif opcion == "4":

        contar_asientos()

    elif opcion == "5":

        print("Gracias por utilizar el sistema del cine.")
        break

    else:

        print("Opción no válida. Intenta nuevamente.")



