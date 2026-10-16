while True:
    print("===== MENÚ =====")
    print("1. Ingresar")
    print("2. Salir")
    print("================")

    opcion = input("Elige una opción (1-2): ").strip()

    if opcion == "1":
        print(">>> Has elegido INGRESAR.\n")
        notasmenos50 = 0
        notas50a70 = 0
        notas70a80 = 0
        notasmas80 = 0
        for i in range(5):
            notas = float(input(f"Ingrese la nota del estudiante {i}:"))
            if notas < 50 > 0:
                notasmenos50 += 1
            elif 50 <= notas <= 70:
                notas50a70 += 1
            elif 70 < notas <= 80:
                notas70a80 += 1
            elif notas >= 80 <= 100:
                notasmas80 += 1
            else:
                print("Nota invalida")
        print("===== RESULTADOS =====")
        print(f"Cantidad de estudiantes con notas menores a 50: {notasmenos50}")
        print(f"Cantidad de estudiantes con notas entre 50 y 70: {notas50a70}")
        print(f"Cantidad de estudiantes con notas entre 70 y 80: {notas70a80}")
        print(f"Cantidad de estudiantes con notas mayores a 80: {notasmas80}")
    elif opcion == "2":
        print(">>> Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print(">>> Opción no válida. Intenta de nuevo.\n")