class ContadorPares:
    def __init__(self):
        self.arreglo = []

    def cargar_datos(self):
        n = int(input("Ingrese la cantidad de elementos: "))

        for i in range(n):
            valor = int(input(f"Ingrese el elemento {i + 1}: "))
            self.arreglo.append(valor)

    def contar_pares(self):
        contador = 0

        for numero in self.arreglo:
            if numero % 2 == 0:
                contador += 1

        return contador

    def mostrar_resultado(self):
        print("\nArreglo:", self.arreglo)
        print("Cantidad de números pares:", self.contar_pares())


# Programa principal
objeto = ContadorPares()
objeto.cargar_datos()
objeto.mostrar_resultado()
