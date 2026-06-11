class Vector:

    def __init__(self, datos):
        self.v = datos

    def contar_pares(self):
        cp = 0
        i = 0

        while i < len(self.v):
            if self.v[i] % 2 == 0:
                cp += 1

            i += 1

        return cp


# Programa principal
datos = [3, 8, 4, 7, 10]

obj = Vector(datos)

print("Cantidad de pares:", obj.contar_pares())