notabaja = 999
notaalta = 0
promedio = 0
while True:
    print("===== MENÚ =====")
    print("1. Ingresar")
    print("2. Salir")
    print("================")

    opcion = input("Elige una opción (1-2): ").strip()

    if opcion == "1":
        print(">>> Has elegido INGRESAR.\n")
        for i in range(20):
            nota = float(input(f"Ingrese la nota {i + 1}: "))
            promedio += nota

            if nota < notabaja:
                notabaja = nota
            if nota > notaalta:
                notaalta = nota
        promedio /= 20
        print(f"La nota más baja es: {notabaja}")
        print(f"La nota más alta es: {notaalta}")
        print(f"El promedio de las notas es: {promedio}")
    elif opcion == "2":
        print(">>> Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print(">>> Opción no válida. Intenta de nuevo.\n")