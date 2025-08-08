Marca = {} 
Marca["Nombre"] = input("Ingresa el nombre de tu Marca: ")
Marca["Tipo"] = input("Ingresa los que vende tu marca: ")
while True:
    edad = int(input("Ingresa la edad de tu marca (1-10): "))
    if 1 <= edad <= 10:
        Marca["edad"] = edad
        break
    print("¡Edad no válida!")

Productos = []
print("\nIngresa sus vacunas (escribe 'fin' para terminar): ")
while True:
    Productos = input("Ingrese vacuna: ")
    if Productos.lower() == "fin":
        break
    if Productos.lower() in [a.lower() for a in Productos]:
        print(f"¡La vacuna '{Productos}' yá está registrada!")
    else:
        Productos.append(Productos)

Marca["Productos"] = Productos 
  
print("\nDatos de la mascota: ")
print(Marca)