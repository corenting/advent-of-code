#!/usr/bin/env dotnet-script

using System;

var fileContent = File.ReadLines("input").Select(x=> (x[0], x[2]));

var scorePart1 = 0;
foreach((var other, var mine) in fileContent)
{
    // Item score (part 1)
    switch (mine)
    {
        case 'X':
            scorePart1 += 1;
            break;
        case 'Y':
            scorePart1 += 2;
            break;
        case 'Z':
            scorePart1 += 3;
            break;
        default:
            throw new InvalidDataException("Invalid input");
    }

    // Winner or draw score (part 1)
    if (
        (other == 'A' && mine == 'Y') ||
        (other == 'B' && mine == 'Z') ||
        (other == 'C' && mine == 'X')
    ) {
        scorePart1 += 6;
    }
    else if (
        (other == 'A' && mine == 'X') ||
        (other == 'B' && mine == 'Y') ||
        (other == 'C' && mine == 'Z')
    ) {
        scorePart1 += 3;
    }
}

System.Console.WriteLine($"Part 1: {scorePart1}");
