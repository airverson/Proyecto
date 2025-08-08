mascota = {} 
mascota["Nombre"] = input("Ingresa el nombre de tu mascota: ")
mascota["Tipo"] = input("Ingresa el tipo de mascota: ")
while True:
    edad = int(input("Ingresa la edad (1-10): "))
    if 1 <= edad <= 10:
        mascota["edad"] = edad
        break
    print("¡Edad no válida!")
    
vacunas = []
print("\nIngresa sus vacunas (escribe 'fin' para terminar): ")
while True:
    vacuna = input("Ingrese vacuna: ")
    if vacuna.lower() == "fin":
        break
    if vacuna.lower() in [a.lower() for a in vacunas]:
        print(f"¡La vacuna '{vacuna}' yá está registrada!")
    else:
        vacunas.append(vacuna)

mascota["vacuna"] = vacunas
  
print("\nDatos de la mascota: ")
print(mascota)
