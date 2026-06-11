import random

class Contador:

    def __init__(self, n, m):
        self.X = [random.randint(1, 9) for _ in range(n)]
        self.Y = [random.randint(1, 9) for _ in range(m)]

    def mostrar_arreglos(self):
        print("Arreglo X:", self.X)
        print("Arreglo Y:", self.Y)

    def contar_repeticiones(self, dato):
        contador_x = 0
        contador_y = 0

        for elemento in self.X:
            if elemento == dato:
                contador_x += 1

        for elemento in self.Y:
            if elemento == dato:
                contador_y += 1

        return contador_x, contador_y


# Programa principal
obj = Contador(5, 4)

obj.mostrar_arreglos()

dato = int(input("\nIngrese el dato a buscar: "))

cx, cy = obj.contar_repeticiones(dato)

print(f"\nEn el arreglo X se repite {cx} veces")
print(f"En el arreglo Y se repite {cy} veces")
print(f"Total de repeticiones: {cx + cy}")





