#Definir una función para convertir grados centígrados a Fahrenheit y a Kelvin.
#Definimos la función
def conversion (cent):
    farng = (9/5) * cent + 32 #convertir a grados Fahrenheit
    kelv = 273.15 + cent # convertir a grados Kelvin
    return farng, kelv
centigrados = float(input("Ingrese grados centígrados:")) #Variable grados centígrados
# Asignamos la variable que se desea convertir
farng, kelv = conversion(centigrados)
# Imprimir resultados
print(centigrados, "grados Centígrados  es igula a:", farng, "grados Fahrenheit")
print(centigrados, "grados Centígrados  es igula a:", kelv, "grados Kelvin")