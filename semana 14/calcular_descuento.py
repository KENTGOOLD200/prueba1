# Definir la función
def calcular_descuento(valor_total, descuento_aplicado=25): # Declaración de parámetros
    descuento = (valor_total * descuento_aplicado) / 100
    return descuento # Retornamos el resultado de nuestra función

# Declaración de variables
productos = ["camiseta", "zapatos", "pantalón"]
busqueda = input("¡Bienvenidos a nuestra tienda de ropa online!\n\nSeleccione el producto que desea comprar (camiseta, zapatos, pantalón): ")  # Realizamos un contexto para darle mas Sentido a nuestro proceso
cantidad = int(input("Seleccione la cantidad que desea comprar: "))
valor_producto= 0
total_cantidad = 0

for producto in productos: # Con el bucle for podemos hacer la búsqueda de nuestro producto en la matríz y le asignamos un precio
    if producto == busqueda:
        if producto == "camiseta":
            valor_producto = 300
        elif producto == "zapatos":
            valor_producto = 200
        elif producto == "pantalón":
            valor_producto = 450

        total_cantidad = valor_producto * cantidad # Hacemis una operación para obtener el prcio a pagar de lo que se compra.
        print("\nEl producto (", producto,") tiene un valor de: $", valor_producto)
        print("El valor total de la compra es: $", total_cantidad)

#Convertimos las variables e imprimimos resultados
valor_final = calcular_descuento(100, )
print("\nDescuento de:", int(valor_final), "%")

descuento_adquirido = calcular_descuento(total_cantidad, )
print("\nValor total de la compra: $", total_cantidad, "\nPorcentaje de descuento:", int(valor_final), "%\nValor de descuento: $", descuento_adquirido, "\n\nPRECIO FINAL : $", total_cantidad - descuento_adquirido)