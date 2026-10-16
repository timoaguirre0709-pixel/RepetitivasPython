while True:
    print("===== MENÚ =====")
    print("1. Ingresar")
    print("2. Salir")
    print("================")

    opcion = input("Elige una opción (1-2): ").strip()

    if opcion == "1":
        print(">>> Has elegido INGRESAR.\n")
        contadorAmarillo = 0
        contadorRosa = 0
        contadorRojo = 0
        contadorVerde = 0
        contadorAzul = 0
        n = int(input("Ingrese la cantidad de automoviles: "))
        for i in range(n):
            ultimo_digito = int(input("Ingrese el último dígito de la placa: "))
            match ultimo_digito:
                case 1 | 2:
                    contadorAmarillo += 1
                case 3 | 4:
                    contadorRosa += 1
                case 5 | 6:
                    contadorRojo += 1
                case 7 | 8:
                    contadorVerde += 1
                case 9 | 0:
                    contadorAzul += 1
                case _:
                    print("El digito no es valido, por favor ingrese un digito del 0 al 9.")
                    continue
        print("===== RESULTADOS =====")
        print(f"Cantidad de automóviles amarillos: {contadorAmarillo}")
        print(f"Cantidad de automoviles rosas: {contadorRosa}")
        print(f"Cantidad de automoviles rojos: {contadorRojo}")
        print(f"Cantidad de automoviles verdes: {contadorVerde}")
        print(f"Cantidad de automoviles azules: {contadorAzul}")
    elif opcion == "2":
        print(">>> Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print(">>> Opción no válida. Intenta de nuevo.\n")