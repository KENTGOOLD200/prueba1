# Creación de un diccionario que contenga información ficticia sobre una persona.
# Inicialización de las variables.
print("\nDatos del usuario:\n") # Realizqar un pequeño contexto para darle mas sentido a nuestro diccionario.

person_data = {
    #clave : valor
    "Nombres:":"Juan Alberto",
    "Apellidos:":"Ramírez Ceballos",
    "Edad:": 25,
    "Sexo:":"Masculino",
    "País:":"Ecuador",
    "Ciudad:":"Durán",
    "Provincia:":"Guayas",
    "Título universitario:":"Ingeniero_en_contabilidad",
    "Email:":"alverjua243@gmail.com",
    "Identificacion:":"0703254532",
    "Antecedentes penales:":"NO",
    "Hijos:":"NO"
}

# Proceso para acceder al valor asociado con la clave "ciudad" y modificarlo con una ciudad diferente.
person_data['Ciudad:'] = "Daule"

# Proceso para agregar una nueva clave-valor al diccionario que represente la "profesion" de la persona.
person_data.update({"Profesión:": "Jefe de Tesorería en Canaries S.A."})

# Proceso para verificar si la clave "telefono" existe en el diccionario. Si no existe, agregarla con un número de teléfono ficticio.
person_data.update({"Teléfono:":"8753209842"})

# Proceso para eliminar la clave "edad" del diccionario.
del person_data['Edad:']

# Imprimir el diccionario resultante de todas las operaciones.
for clave, valor in person_data.items(): # Usar el bucle for para darle mas presentación a muestra información
 print(clave, valor)

