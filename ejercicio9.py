while True:
    print("===== MENÚ =====")
    print("1. Ingresar")
    print("2. Salir")
    print("================")

    opcion = input("Elige una opción (1-2): ").strip()

    if opcion == "1":
        hombres = mujeres = edad_hombres = edad_mujeres = 0
        cantidad = int(input("Cantidad de alumnos: "))
        for i in range(cantidad):
            edad = int(input("Ingrese la edad: "))
            sexo = input("Sexo (H/M): ").strip().upper()
            if sexo == "H":
                hombres += 1
                edad_hombres += edad
            else:
                mujeres += 1
                edad_mujeres += edad

        if hombres:
            print(f"Promedio hombres: {edad_hombres / hombres:.2f}")
        if mujeres:
            print(f"Promedio mujeres: {edad_mujeres / mujeres:.2f}")
        print(f"Promedio del grupo: {(edad_hombres + edad_mujeres) / cantidad:.2f}")
    elif opcion == "2":
        print(">>> Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print(">>> Opción no válida. Intenta de nuevo.\n")