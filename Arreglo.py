import random

# Tamaños de los arreglos
n = 5
m = 4

# Generar arreglos aleatorios entre 1 y 9
X = [random.randint(1, 9) for _ in range(n)]
Y = [random.randint(1, 9) for _ in range(m)]

print("Arreglo X:", X)
print("Arreglo Y:", Y)

# Dato a buscar
dato = int(input("\nIngrese el dato a buscar: "))

contador_x = 0
contador_y = 0

# Buscar en X
for elemento in X:
    if elemento == dato:
        contador_x += 1

# Buscar en Y
for elemento in Y:
    if elemento == dato:
        contador_y += 1

print(f"\nEn el arreglo X se repite {contador_x} veces")
print(f"En el arreglo Y se repite {contador_y} veces")
print(f"Total de repeticiones: {contador_x + contador_y}")





