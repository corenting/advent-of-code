#!/usr/bin/env dotnet-script

using System;

var fileContent = File.ReadLines("input").Select(x=> (x[0], x[2]));

var scorePart1 = 0;
var scorePart2 = 0;
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

    // Part 2
    switch(other) {
        case 'A':
            switch(mine) {
                case 'X':
                    scorePart2 += 3;
                    break;
                case 'Y':
                    scorePart2 += 4;
                    break;
                case 'Z':
                    scorePart2 += 8;
                    break;
            }
            break;
        case 'B':
            switch(mine) {
                case 'X':
                    scorePart2 += 1;
                    break;
                case 'Y':
                    scorePart2 += 5;
                    break;
                case 'Z':
                    scorePart2 += 9;
                    break;
            }
            break;
        case 'C':
            switch(mine) {
                case 'X':
                    scorePart2 += 2;
                    break;
                case 'Y':
                    scorePart2 += 6;
                    break;
                case 'Z':
                    scorePart2 += 7;
                    break;
            }
            break;
    }
}

System.Console.WriteLine($"Part 1: {scorePart1}");
System.Console.WriteLine($"Part 2: {scorePart2}");
