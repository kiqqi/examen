calificaciones = []
while True:
    calificacion = input("Ingresa una calificación (o 'fin' para terminar): ")
    if calificacion.lower() == 'fin':
        break
    calificaciones.append(float(calificacion))

if calificaciones:
    calificacion_mas_alta = max(calificaciones)
    calificacion_mas_baja = min(calificaciones)
    promedio = sum(calificaciones) / len(calificaciones)

    print(f"Calificación más alta: {calificacion_mas_alta}")
    print(f"Calificación más baja: {calificacion_mas_baja}")
    print(f"Promedio de calificaciones: {promedio}")
else:
    print("No se ingresaron calificaciones.")
