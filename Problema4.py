# Lista para almacenar los datos de los alumnos
alumnos = []

# Pedimos al usuario que ingrese la cantidad de alumnos
n = int(input("Ingrese la cantidad de alumnos: "))

# Iteramos para ingresar los datos de cada alumno
for i in range(1, n + 1):
    # Creamos un diccionario para el alumno
    alumno = {}
    
    # Pedimos el nombre del alumno y mostramos el número de alumno
    alumno['Alumno'] = input(f"Ingrese el nombre del alumno {i}: ")
    
    # Pedimos las tres notas del alumno y las guardamos en una lista
    notas = []
    for j in range(1, 4):
        nota = int(input(f"Ingrese la nota {j} del alumno {i} ({alumno['Alumno']}): "))
        notas.append(nota)
    
    # Guardamos las notas en el diccionario del alumno
    alumno['Notas'] = notas
    
    # Añadimos el diccionario del alumno a la lista de alumnos
    alumnos.append(alumno)

# Mostramos la lista completa de alumnos con sus notas
print("\nListado de Alumnos y sus Notas:")
for idx, alumno in enumerate(alumnos, start=1):
    print(f"Alumno {idx}: {alumno['Alumno']}, Notas: {alumno['Notas']}")

