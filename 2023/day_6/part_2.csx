using Internal;

private record Race(long Time, long DistanceRecord);

private static long GetNumberFromString(string listAsString) {
    return long.Parse(listAsString.Where(char.IsDigit).ToArray());
}

var input = File
    .ReadLines("input")
    .ToList();

var race = new Race(GetNumberFromString(input[0]), GetNumberFromString(input[1]));
long waysToWin = 0;
long holdTime = 0;
while (holdTime < race.Time + 1)
{
    long remainingRaceTime = race.Time - holdTime;
    long traveledDistance = remainingRaceTime * holdTime;
    if (traveledDistance > race.DistanceRecord) {
        waysToWin++;
    }
    holdTime++;
}

Console.WriteLine($"Part 2: {waysToWin}");
