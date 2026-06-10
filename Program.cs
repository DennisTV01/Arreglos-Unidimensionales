using System;

class Program
{
    static void Main()
    {
        Console.Write("Ingrese la cantidad de elementos del arreglo: ");
        int n = int.Parse(Console.ReadLine());

        int[] arreglo = new int[n];

        for (int i = 0; i < n; i++)
        {
            Console.Write($"Ingrese el elemento {i + 1}: ");
            arreglo[i] = int.Parse(Console.ReadLine());
        }

        Console.Write("\nIngrese el dato que desea buscar: ");
        int dato = int.Parse(Console.ReadLine());

        bool encontrado = false;

        for (int i = 0; i < arreglo.Length; i++)
        {
            if (arreglo[i] == dato)
            {
                Console.WriteLine($"\nDato encontrado en la posición {i}");
                encontrado = true;
                break;
            }
        }

        if (!encontrado)
        {
            Console.WriteLine("\nDato no encontrado en el arreglo");
        }

        Console.ReadKey();
    }
}