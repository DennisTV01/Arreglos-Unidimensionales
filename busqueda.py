# Ingreso de datos
n = int(input("Ingrese la cantidad de elementos del arreglo: "))

arreglo = []

for i in range(n):      # 1
    valor = int(input(f"Ingrese el elemento {i + 1}: "))   # 2
    arreglo.append(valor)  # 3

# Dato a buscar
dato = int(input("\nIngrese el dato que desea buscar: "))    # 4

# Búsqueda secuencial
encontrado = False  # 5

for i in range(len(arreglo)):   # 6
    if arreglo[i] == dato:  # 7
        print(f"\nDato encontrado en la posición {i}")  # 8
        encontrado = True # 9
        break  

# Si no se encontró
if not encontrado: # 1 
    print("\nDato no encontrado en el arreglo")  # 10