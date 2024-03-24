# Ordenación de arreglo multidimencional
# Declaración de variables
matriz2d = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

# Solicitar al usuario el índice de la fila a ordenar
indice_ordenar = int(input("Elija la fila que se desee ordenar (0, 1, 2): "))
# Mostrar matriz original
print("\nMatriz original:")
for origin in matriz2d:
    print(origin)

# Verificar si el índice es válido
if 0 <= indice_ordenar < len(matriz2d):
    # Ordenamiento Bubble Sort de la fila específica
    fila_ordenar= matriz2d[indice_ordenar]
    for i in range(len(fila_ordenar)):
        for j in range(0, len(fila_ordenar)-i-1):
            if fila_ordenar[j] > fila_ordenar[j+1]:
                fila_ordenar[j], fila_ordenar[j+1] = fila_ordenar[j+1], fila_ordenar[j]
    matriz2d[indice_ordenar] = fila_ordenar


    # Mostrar matriz con fila ordenada
    print("\nMatriz con la fila ordenada:")
    for fila in matriz2d:
        print(fila)
else:
    print("No existe, debe ser entre 0 y 2", len(matriz2d) - 1)