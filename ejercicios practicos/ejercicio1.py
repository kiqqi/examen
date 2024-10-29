alumnos = ["Juan", "Ana", "Luis", "Maria", "Carlos", "Pedro", "Sofia", "Laura"]
notas = {
    "Juan": [8, 9, 7, 10, 6, 8],
    "Ana": [9, 10, 9, 8, 9, 9],
    "Luis": [7, 6, 5, 8, 7, 6],
    "Maria": [10, 10, 9, 9, 10, 10],
    "Carlos": [6, 7, 5, 5, 6, 6],
    "Pedro": [8, 9, 8, 7, 8, 9],
    "Sofia": [9, 8, 10, 9, 10, 10],
    "Laura": [7, 6, 8, 9, 8, 7]
}

for alumno in alumnos:
    promedio = sum(notas[alumno]) / len(notas[alumno])
    print(f"{alumno}: {promedio}")
