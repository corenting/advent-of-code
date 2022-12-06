#!/usr/bin/env dotnet-script

using System;

var fileContent = File.ReadLines("input");

var counts = new List<int>();
var currentCount = 0;
foreach(var item in fileContent) {
    if (string.IsNullOrWhiteSpace(item)) {
        counts.Add(currentCount);
        currentCount = 0;
        continue;
    }
    currentCount += int.Parse(item);
}
counts.Add(currentCount);

var ordered = counts.OrderDescending();

System.Console.WriteLine($"Part 1: {ordered.Take(1).Sum()}");
System.Console.WriteLine($"Part 2: {ordered.Take(3).Sum()}");
