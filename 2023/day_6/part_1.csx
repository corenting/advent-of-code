using Internal;

private record Race(int Time, int DistanceRecord);

private static IEnumerable<int> GetNumbersFromString(string listAsString) {
    return listAsString.Split().Where(x => x.All(char.IsDigit) && !string.IsNullOrEmpty(x)).Select(x => int.Parse(x));
}

var input = File
    .ReadLines("input")
    .ToList();
var races = GetNumbersFromString(input[0]).Zip(GetNumbersFromString(input[1]), (time, distance) => new Race(time, distance));

int total = 1;
foreach(var race in races) {
    // Get all possibilities
    int waysToWin = 0;
    foreach (int holdTime in Enumerable.Range(0, race.Time + 1))
    {
        int remainingRaceTime = race.Time - holdTime;
        int traveledDistance = remainingRaceTime * holdTime;
        if (traveledDistance > race.DistanceRecord) {
            waysToWin++;
        }
    }
    total *= waysToWin;
}

Console.WriteLine($"Part 1: {total}");
