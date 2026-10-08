alumnos = [
    {"nombre": "Ana", "nota": 8.5},
    {"nombre": "Luis", "nota": 4.0},
    {"nombre": "Marta", "nota": 7.0},
    {"nombre": "Pablo", "nota": 3.5},
    {"nombre": "Sara", "nota": 9.0},
]
contador_aprobados=0
contador_suspensos=0
for alumno in alumnos:
    if alumno["nota"] > 5:
        print(f"{alumno['nombre'].upper()} ha aprobado con una nota de {alumno['nota']}.")
        contador_aprobados+=1
    else:
        print(f"{alumno['nombre'].upper()} ha suspendido con una nota de {alumno['nota']}.")
        contador_suspensos+=1
        
print(f"Total de alumnos aprobados: {contador_aprobados}")
print(f"Total de alumnos suspensos: {contador_suspensos}")

total=contador_aprobados + contador_suspensos
nota_total=0
for alumno in alumnos:
    nota = alumno["nota"]
    nota_total += nota
media = nota_total / total
print(media)
def calcular_media(alumnos):
    try:
        nota_total = 0
        for alumno in alumnos:
            nota = alumno["nota"]
            nota_total += nota
        media = nota_total / len(alumnos)
    except ZeroDivisionError:
        print("0 alumnos en la lsita. No se puede calcular la media.")
    return media
print(f"Numero de alumnos aprobados: {contador_aprobados}")
print(f"Numero de alumnos suspensos: {contador_suspensos}")
print(f"total de alumnos: {total}")
print(f"Media de notas: {calcular_media(alumnos)}")
        
