using System;

class Program
{
    static double squareCircle(int r, int n)
    {
        return Math.Round(Math.PI * Math.Pow(r, 2), n);
    }

    static void Main()
    {
        Console.Write("Введите радиус круга - ");
        int radius = int.Parse(Console.ReadLine());
        Console.Write("Введите количество знаков после запятой - ");
        int count = int.Parse(Console.ReadLine());

        Console.WriteLine($"Площадь круга = {squareCircle(radius, count)}");
        Console.ReadLine();
    }
}