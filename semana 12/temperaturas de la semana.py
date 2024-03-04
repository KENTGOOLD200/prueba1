# Inicialización del proceso para crear una matríz 3D que represente las temperaturas en diferentes ciudades y en diferentes dias de la semana:
# Declaración de variables
temperaturas = [ # Variable 3D de las temperaturas mensuales de Portoviejo, Huaquillas y Manta
                 [# PORTOVIEJO
                     [# SEMANA 1
                         {"Día": "Lunes", "Temperatura °C": 30},
                         {"Día": "Martes", "Temperatura °C": 31},
                         {"Día": "Miercoles", "Temperatura °C": 29},
                         {"Día": "Jueves", "Temperatura °C": 30},
                         {"Día": "viernes", "Temperatura °C": 25},
                         {"Día": "Sabado", "Temperatura °C": 28},
                         {"Día": "Domingo", "Temperatura °C": 30}
                     ],
                     [# SEMANA 2
                         {"Día": "Lunes", "Temperatura °C": 32},
                         {"Día": "Martes", "Temperatura °C": 30},
                         {"Día": "Miercoles", "Temperatura °C": 31},
                         {"Día": "Jueves", "Temperatura °C": 30},
                         {"Día": "viernes", "Temperatura °C": 29},
                         {"Día": "Sabado", "Temperatura °C": 30},
                         {"Día": "Domingo", "Temperatura °C": 29}
                     ],
                     [# SEMANA 3
                         {"Día": "Lunes", "Temperatura °C": 30},
                         {"Día": "Martes", "Temperatura °C": 32},
                         {"Día": "Miercoles", "Temperatura °C": 31},
                         {"Día": "Jueves", "Temperatura °C": 29},
                         {"Día": "viernes", "Temperatura °C": 30},
                         {"Día": "Sabado", "Temperatura °C": 31},
                         {"Día": "Domingo", "Temperatura °C": 29}
                     ],
                     [ #SEMANA 4
                         {"Día": "Lunes", "Temperatura °C": 29},
                         {"Día": "Martes", "Temperatura °C": 30},
                         {"Día": "Miercoles", "Temperatura °C": 28},
                         {"Día": "Jueves", "Temperatura °C": 30},
                         {"Día": "viernes", "Temperatura °C": 31},
                         {"Día": "Sabado", "Temperatura °C": 31},
                         {"Día": "Domingo", "Temperatura °C": 30}
                     ]
                 ],
                 [# HUAQUILLAS
                     [  # SEMANA 1
                         {"Día": "Lunes", "Temperatura °C": 30},
                         {"Día": "Martes", "Temperatura °C": 31},
                         {"Día": "Miercoles", "Temperatura °C": 30},
                         {"Día": "Jueves", "Temperatura °C": 30},
                         {"Día": "viernes", "Temperatura °C": 29},
                         {"Día": "Sabado", "Temperatura °C": 28},
                         {"Día": "Domingo", "Temperatura °C": 29}
                     ],
                     [  # SEMANA 2
                         {"Día": "Lunes", "Temperatura °C": 32},
                         {"Día": "Martes", "Temperatura °C": 32},
                         {"Día": "Miercoles", "Temperatura °C": 30},
                         {"Día": "Jueves", "Temperatura °C": 29},
                         {"Día": "viernes", "Temperatura °C": 31},
                         {"Día": "Sabado", "Temperatura °C": 31},
                         {"Día": "Domingo", "Temperatura °C": 30}
                     ],
                     [  # SEMANA 3
                         {"Día": "Lunes", "Temperatura °C": 28},
                         {"Día": "Martes", "Temperatura °C": 27},
                         {"Día": "Miercoles", "Temperatura °C": 28},
                         {"Día": "Jueves", "Temperatura °C": 29},
                         {"Día": "viernes", "Temperatura °C": 30},
                         {"Día": "Sabado", "Temperatura °C": 31},
                         {"Día": "Domingo", "Temperatura °C": 30}
                     ],
                     [  # SEMANA 4
                         {"Día": "Lunes", "Temperatura °C": 32},
                         {"Día": "Martes", "Temperatura °C": 31},
                         {"Día": "Miercoles", "Temperatura °C": 30},
                         {"Día": "Jueves", "Temperatura °C": 29},
                         {"Día": "viernes", "Temperatura °C": 29},
                         {"Día": "Sabado", "Temperatura °C": 31},
                         {"Día": "Domingo", "Temperatura °C": 30}
                     ]
                 ],
                 [ #MANTA
                     [  # SEMANA 1
                         {"Día": "Lunes", "Temperatura °C": 27},
                         {"Día": "Martes", "Temperatura °C": 29},
                         {"Día": "Miercoles", "Temperatura °C": 28},
                         {"Día": "Jueves", "Temperatura °C": 27},
                         {"Día": "viernes", "Temperatura °C": 30},
                         {"Día": "Sabado", "Temperatura °C": 28},
                         {"Día": "Domingo", "Temperatura °C": 29}
                     ],
                     [  # SEMANA 2
                         {"Día": "Lunes", "Temperatura °C": 31},
                         {"Día": "Martes", "Temperatura °C": 30},
                         {"Día": "Miercoles", "Temperatura °C": 29},
                         {"Día": "Jueves", "Temperatura °C": 29},
                         {"Día": "viernes", "Temperatura °C": 28},
                         {"Día": "Sabado", "Temperatura °C": 30},
                         {"Día": "Domingo", "Temperatura °C": 31}
                     ],
                     [  # SEMANA 3
                         {"Día": "Lunes", "Temperatura °C": 30},
                         {"Día": "Martes", "Temperatura °C": 30},
                         {"Día": "Miercoles", "Temperatura °C": 30},
                         {"Día": "Jueves", "Temperatura °C":28},
                         {"Día": "viernes", "Temperatura °C": 28},
                         {"Día": "Sabado", "Temperatura °C": 27},
                         {"Día": "Domingo", "Temperatura °C": 29}
                     ],
                     [  # SEMANA 4
                         {"Día": "Lunes", "Temperatura °C": 29},
                         {"Día": "Martes", "Temperatura °C": 28},
                         {"Día": "Miercoles", "Temperatura °C": 27},
                         {"Día": "Jueves", "Temperatura °C": 30},
                         {"Día": "viernes", "Temperatura °C": 29},
                         {"Día": "Sabado", "Temperatura °C": 28},
                         {"Día": "Domingo", "Temperatura °C": 28}
                     ]
                 ]
]
# Almacenar las temperaturas diarias para una ciudad en un día específico de una semana determinada
# Hacer uso de un bucle anidado para recorrer la matiz buscando seleccionar las ciudades
for ciudad in range(len(temperaturas)):
    if ciudad == 0: # Por decisión propia usé la condicional if-else para mayor órden
        city = "Portoviejo"
    elif ciudad == 1:
        city = "Huaquillas"
    elif ciudad == 2:
        city = "Manta"

    # Hacer uso de un bucle anidado para recorrer la matiz buscando seleccionar las semanas
    for semana in range(len(temperaturas[ciudad])):
        if semana == 0: # Aquí tambien hice uso de la condicional if-else
            sem = "Semana 1"
        elif semana == 1:
            sem = "Semana 2"
        elif semana == 2:
            sem = "Semana 3"
        elif semana == 3:
            sem = "Semana 4"

        # Hacer uso de un bucle anidado para recorrer la matiz buscando seleccionar los días
        for dia in range(len(temperaturas[ciudad][semana])):
            if dia == 0: # Hacer uso de un bucle anidado para recorrer la matiz buscando seleccionar las ciudades
                day = "Lunes"
            elif dia == 1:
                day = "Martes"
            elif dia == 2:
                day = "Miercoles"
            elif dia == 3:
                day = "Jueves"
            elif dia == 4:
                day = "Viernes"
            elif dia == 5:
                day = "Sábado"
            elif dia == 6:
                day = "Domingo"

            # Imprimir los resultados de la matriz, asegurandose de no cometer errores en la sintáxis
            print("Ciudad:", city, sem, "  Día:", day, "  temperatura:", temperaturas[ciudad] [semana] [dia] ["Temperatura °C"])

# Calcular los promedios de las temperaturas semanales de cada ciudad
promedios = []

# Usar un bucle anidado para recorrer el arreglo
for ciudad in temperaturas: # Para cada ciudad
    # Crear una lista vacía para guardar los promedios semanales de la ciudad
    promedios_ciudad = []
    for semana in ciudad: # Para cada semana
        # Inicializar la suma y el contador de temperaturas de la semana
        suma = 0
        contador = 0
        for dia in semana: # Para cada día
            # Sumar la temperatura del día a la suma
            suma += dia["Temperatura °C"]
            # Incrementar el contador en uno
            contador += 1
        # Calcular el promedio de la semana dividiendo la suma por el contador
        promedio = suma / contador
        # Agregar el promedio a la lista de promedios de la ciudad
        promedios_ciudad.append(promedio)
    # Agregar la lista de promedios de la ciudad a la lista de promedios
    promedios.append(promedios_ciudad)

# Imprimir los resultados
print("\n\nLos promedios de las 4 semanas del mes de cada ciudad son:\n")
print(f"Portoviejo: {promedios[0]}")
print(f"Huaquillas: {promedios[1]}")
print(f"Manta: {promedios[2]}")