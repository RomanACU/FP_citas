def registrar_citas():
    cantidad = int(input("Ingrese la cantidad de ciudadanos que harán una solicitud: "))
    
# Se utilizaron dos listas vacias para que coincidiera con el pseudocodigo 
    nombres = ["" for _ in range(cantidad)]
    tiempos = [0 for _ in range(cantidad)]

    for i in range(cantidad):
        nombres[i] = input("Ingrese el nombre del ciudadano/a: ")
        
        while True:
            tiempo = int(input("Ingrese el tiempo estimado en minutos (máximo 120): "))
            if tiempo <= 120:
                tiempos[i] = tiempo
                break
            else:
                print("Error: El tiempo máximo permitido es 120. Ingrese un valor menor.")

    # Ordenar usando el método de burbuja
    for i in range(cantidad - 1):
        for j in range(cantidad - i - 1):
            if tiempos[j] > tiempos[j + 1]:
                tiempos[j], tiempos[j + 1] = tiempos[j + 1], tiempos[j]
                nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]

    print("\nLista de solicitudes registradas:")
    for i in range(cantidad):
        print(f"Nombre: {nombres[i]} | Tiempo de atención estimado: {tiempos[i]} minutos")

# Llamar a la función
registrar_citas()
