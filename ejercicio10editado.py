numero = 1
multiplicacion = 1

while numero <= 20:
    if numero == 10:
        numero += 1
        continue

    if numero > 15:
        break

    multiplicacion *= numero
    numero += 1

print("El resultado de la multiplicación es:", multiplicacion)
