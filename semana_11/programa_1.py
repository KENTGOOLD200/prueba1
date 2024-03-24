# Proceso de búsqueda dentro de una matriz 2d
# Declaración de variables
matriz2d = [ #matríz 2d
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
# Valor para buscar dentro de la variable
valor_buscar = int(input("\nInforme o valor que desea buscar (del 10 al 90 y avanzar de 10 en 10): "))
valor_final = False

# Buscar en la matrríz
for i in range(len(matriz2d)):
    for j in range(len(matriz2d[i])):
        if matriz2d[i][j] == valor_buscar: # Si se encuentra dentro de la matriz
            # Imprimir resultados
            print(f"\nValor ({valor_buscar}) se encuentra en la posición({i},{j})")
            valor_final = True
            break
    if valor_final:
        break
if not valor_final: # Si no se encuentra en la matriz
    # Imprimir resultados
    print("\nEl valor no se encuentra en la matriz")
