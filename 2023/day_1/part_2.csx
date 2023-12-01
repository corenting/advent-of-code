using Internal;
using System.Text.RegularExpressions;

var mapping = new Dictionary<string, int>()
{
    { "one", 1 },
    { "two", 2 },
    { "three", 3 },
    { "four", 4 },
    { "five", 5 },
    { "six", 6 },
    { "seven", 7 },
    { "eight", 8 },
    { "nine", 9 },
    { "1", 1 },
    { "2", 2 },
    { "3", 3 },
    { "4", 4 },
    { "5", 5 },
    { "6", 6 },
    { "7", 7 },
    { "8", 8 },
    { "9", 9 },
};

var regexText = String.Join("|", mapping.Keys);
var regexFirst = new Regex(regexText);
var regexLast = new Regex(regexText, RegexOptions.RightToLeft);

var sum = File.ReadLines("input")
    .Select(line => {
        var matchesFirst = regexFirst.Matches(line);
        var matchesLast = regexLast.Matches(line);
        return mapping[matchesFirst.First().Value] * 10 + mapping[matchesLast.First().Value];
    })
    .Sum();
Console.WriteLine($"Part 2: {sum}");
