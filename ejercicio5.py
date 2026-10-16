total_ninos = 0.0
cantidad_ninos = 0

total_jovenes = 0.0
cantidad_jovenes = 0

total_adultos = 0.0
cantidad_adultos = 0

total_ancianos = 0.0
cantidad_ancianos = 0

for i in range(50):
    edad = int(input(f"Ingrese la edad de la persona {i + 1}: "))
    peso = float(input(f"Ingrese el peso de la persona {i + 1}: "))

    if 0 <= edad <= 12:
        total_ninos += peso
        cantidad_ninos += 1
    elif 13 <= edad <= 29:
        total_jovenes += peso
        cantidad_jovenes += 1
    elif 30 <= edad <= 59:
        total_adultos += peso
        cantidad_adultos += 1
    elif edad >= 60:
        total_ancianos += peso
        cantidad_ancianos += 1
    else:
        print("Edad no válida. La edad debe ser mayor o igual a 0.")
        continue

print("\nPromedio de peso por categoría:")

if cantidad_ninos > 0:
    promedio_ninos = total_ninos / cantidad_ninos
    print(f"Niños: {promedio_ninos:.2f} kg")
else:
    print("Niños: No hay personas registradas")

if cantidad_jovenes > 0:
    promedio_jovenes = total_jovenes / cantidad_jovenes
    print(f"Jóvenes: {promedio_jovenes:.2f} kg")
else:
    print("Jóvenes: No hay personas registradas")

if cantidad_adultos > 0:
    promedio_adultos = total_adultos / cantidad_adultos
    print(f"Adultos: {promedio_adultos:.2f} kg")
else:
    print("Adultos: No hay personas registradas")

if cantidad_ancianos > 0:
    promedio_ancianos = total_ancianos / cantidad_ancianos
    print(f"Ancianos: {promedio_ancianos:.2f} kg")
else:
    print("Ancianos: No hay personas registradas")