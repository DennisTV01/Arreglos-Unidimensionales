using System;

class Program
{
    static void Main()
    {
        int[] X = { 3, 3, 4, 5 };
        int[] Y = { 3, 4, 4 };

        Console.Write("Ingrese el dato a buscar: ");
        int dato = int.Parse(Console.ReadLine());

        int contadorX = 0;
        int contadorY = 0;

        // Buscar en X
        for (int i = 0; i < X.Length; i++)
        {
            if (X[i] == dato)
            {
                contadorX++;
            }
        }

        // Buscar en Y
        for (int i = 0; i < Y.Length; i++)
        {
            if (Y[i] == dato)
            {
                contadorY++;
            }
        }

        Console.WriteLine($"\nEn el arreglo X se repite {contadorX} veces.");
        Console.WriteLine($"En el arreglo Y se repite {contadorY} veces.");
        Console.WriteLine($"Total de repeticiones: {contadorX + contadorY}");

        Console.ReadKey();
    }
}
