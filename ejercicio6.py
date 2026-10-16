
while True:
    print("===== MENÚ =====")
    print("1. Ingresar")
    print("2. Salir")
    print("================")

    opcion = input("Elige una opción (1-2): ").strip()

    if opcion == "1":
        print(">>> Has elegido INGRESAR.\n")
        hombres = 0
        mujeres = 0
        n = int(input("Ingrese la cantidad de personas: "))

        for i in range(n):
            sexo = (input("Ingrese el sexo de la persona (H/M): ").strip().upper())
            if sexo == "H":
                hombres += 1
            elif sexo == "M":
                mujeres += 1
        else:
            print("Sexo no valido, por favor ingrese H para hombre o M para mujer.")
            print(f"Cantidad de hombres: {hombres}")
            print(f"Cantidad de mujeres: {mujeres}")    
    elif opcion == "2":
        print(">>> Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print(">>> Opción no válida. Intenta de nuevo.\n")