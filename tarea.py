# Solicitar el número de estudiantes
num_estudiantes = int(input("Ingrese el número total de estudiantes: "))

# Inicialización de variables
calificaciones = []
aprobados = 0
reprobados = 0

# Validar y registrar las calificaciones de cada estudiante
for i in range(num_estudiantes):
    while True:
        calificacion = float(input(f"Ingrese la calificación del estudiante {i + 1}: "))
        if 10 <= calificacion <= 70:
            calificaciones.append(calificacion)
            break
        else:
            print("La calificación debe estar entre 10 y 70. Intente de nuevo.")

# Calcular el número de aprobados y reprobados
for calificacion in calificaciones:
    if calificacion >= 40:
        aprobados += 1
    else:
        reprobados += 1

# Calcular la calificación más alta, más baja y el promedio
if calificaciones:  # Verificación para evitar división por cero
    calificacion_mas_alta = max(calificaciones)
    calificacion_mas_baja = min(calificaciones)
    promedio = sum(calificaciones) / len(calificaciones)
else:
    calificacion_mas_alta = calificacion_mas_baja = promedio = 0

# Imprimir los resultados
print("\nResultados:")
print(f"Calificación más alta: {calificacion_mas_alta}")
print(f"Calificación más baja: {calificacion_mas_baja}")
print(f"Promedio de calificaciones: {promedio:.2f}")
print(f"Número de estudiantes aprobados: {aprobados}")
print(f"Número de estudiantes reprobados: {reprobados}")
