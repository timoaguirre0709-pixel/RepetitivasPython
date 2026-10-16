while True:
    print("===== MENÚ =====")
    print("1. Ingresar alumnos")
    print("2. Salir")
    opcion = input("Elige una opción (1-2): ").strip()

    if opcion == "1":
        hombres = mujeres = altos = bajos = cantidad = 0
        suma_alturas = 0

        while True:
            edad = int(input("Edad (0 para terminar): "))
            if edad == 0:
                break

            sexo = input("Sexo (H/M): ").strip().upper()
            while sexo not in ("H", "M"):
                sexo = input("Ingrese H o M: ").strip().upper()
            altura = float(input("Altura en metros: "))

            if sexo == "H":
                hombres += 1
            else:
                mujeres += 1

            suma_alturas += altura
            cantidad += 1
            altos += altura > 1.70
            bajos += altura <= 1.50

        print(f"Hombres: {hombres}")
        print(f"Mujeres: {mujeres}")
        if cantidad:
            print(f"Altura promedio: {suma_alturas / cantidad:.2f} m")
        else:
            print("No se ingresaron alumnos.")
        print(f"Alumnos con altura mayor a 1.70 m: {altos}")
        print(f"Alumnos con altura menor o igual a 1.50 m: {bajos}")
    elif opcion == "2":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida.\n")