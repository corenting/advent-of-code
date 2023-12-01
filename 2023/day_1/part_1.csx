using Internal;

var partOne = File.ReadLines("input")
  .Select(line => line.Where(char.IsDigit).First().ToString() +  line.Where(char.IsDigit).Last().ToString())
  .Select(num => int.Parse(num))
  .Sum();
Console.WriteLine($"Part 1: {partOne}");
