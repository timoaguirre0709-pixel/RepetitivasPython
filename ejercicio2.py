for i in range(10):
    numero = int(input("Ingrese sus números negativos: "))
    if numero < 0:
        positivos = numero*(-1)
        print(f"El número convertido a positivo es: {positivos}")
    else:
        print("El número ingresado no es negativo, por favor ingrese un número negativo.")