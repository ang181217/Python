def calcular_promedio(notas):
    return sum(notas) / len(notas)

nombres_estudiantes = []
notas_matematicas = []
notas_literatura = []
notas_quimica = []

for _ in range(5):
    nombre = input("Ingresa el nombre del estudiante: ")
    matematicas = float(input("Ingresa la nota de matemáticas: "))
    literatura = float(input("Ingresa la nota de literatura: "))
    quimica = float(input("Ingresa la nota de química: "))

    nombres_estudiantes.append(nombre)
    notas_matematicas.append(matematicas)
    notas_literatura.append(literatura)
    notas_quimica.append(quimica)

promedios = []
for i in range(5):
    promedio_estudiante = calcular_promedio([notas_matematicas[i], notas_literatura[i], notas_quimica[i]])
    promedios.append(promedio_estudiante)

promedios_redondeados = [round(promedio, 2) for promedio in promedios]

promedio_general = calcular_promedio(promedios)
promedio_mas_alto = max(promedios)
promedio_mas_bajo = min(promedios)

promedio_general_redondeado = round(promedio_general, 2)
promedio_mas_alto_redondeado = round(promedio_mas_alto, 2)
promedio_mas_bajo_redondeado = round(promedio_mas_bajo, 2)

for i in range(5):
    print(f"\nEstudiante: {nombres_estudiantes[i]}")
    print(f"Matemáticas: {notas_matematicas[i]}")
    print(f"Literatura: {notas_literatura[i]}")
    print(f"Química: {notas_quimica[i]}")
    print(f"Promedio: {promedios_redondeados[i]}")

print("\nPromedio general: ", promedio_general_redondeado)
print("Promedio más alto: ", promedio_mas_alto_redondeado)
print("Promedio más bajo: ", promedio_mas_bajo_redondeado)
