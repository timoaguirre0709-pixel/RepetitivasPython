numero = int(input("Ingrese un número: "))

for i in range(11):
    if numero > 0:
        tabla = i*numero
        print(f"{numero} x {i} = {tabla}")
    else:
        print("El número ingresado no es positivo, por favor ingrese un número positivo.")