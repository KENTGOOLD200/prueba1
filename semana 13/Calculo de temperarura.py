#Proceso de cálculo de temperaturas de diferentes ciudades por medio del uso de las funciones en diferentes intervalos de tiempo.
#Definir la función
def promedio_calculo(base_datos, ciudad, semana_inicio, semana_final): #Definir los parámetros
    var = 0 #Variables para guardar los resultados que obtengo de la funnción
    sm = 0
    for i in range(len(base_datos[ciudad])):
        if i>=semana_inicio and i<=semana_final:
             for j in range(len(base_datos[ciudad] [i])):
                 sm = sm + base_datos[ciudad][i][j]['Temperatura °C']
                 var = var+1
                 print(base_datos[ciudad][i][j])
    promedio = sm/var # variable final resultante de el proceso
    return promedio # Retornar las variables
# Fin de los procesos de la función

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

# Imprimir mensaje para aclarar qué proceso se está realizando
print("\nInicializando  aplicación para calcular las temperaturas de una ciudad en determinados lapsos de tiempo:")

# Declaramos variables para obtener Datos del usuario
ciudad = input("\nIngrese ciudad (Portoviejo, Huaquillas, Manta): ")
city = 0
semana_in = input("\nIngrese semana inicial (Semana 1, Semana 2, Semana 3, Semana 4): ")
sem = 0
semana_fn = input("\nIngrese semana final (Semana 1, Semana 2, Semana 3, Semana 4): ")
sm = 0

if semana_fn == "Semana 1":  # Hago uso de la condicional if-else para asignar valores a las Variables de datos.
    sm = 0
elif semana_fn == "Semana 2":
    sm = 1
elif semana_fn == "Semana 3":
    sm = 2
elif semana_fn == "Semana 4":
    sm = 3
else:
    print("Error, entrada no válida.")

if semana_in == "Semana 1":  # Aquí tambien hice uso de la condicional if-else
    sem = 0
elif semana_in == "Semana 2":
    sem = 1
elif semana_in == "Semana 3":
    sem = 2
elif semana_in == "Semana 4":
    sem = 3
else:
    print("Error, entrada no válida.")

if ciudad == "Portoviejo":  # Aplico la condicional if-else Para aclarar que ciudad busco
    city = 0
elif ciudad == "Huaquillas":
    city = 1
elif ciudad == "Manta":
    city = 2
else:
    print("Error, entrada no válida.")

# Asignamos la variable que se desea convertir
promt= (promedio_calculo(temperaturas, city, sem, sm))

# Imprimimos resultados
print("\nCiudad consultada:", ciudad, "\nSemana inicial:", semana_in, "\nsemana final:", semana_fn, "\nPromedio de temperatura entre las semanas:", promt)


