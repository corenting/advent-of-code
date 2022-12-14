#!/usr/bin/env dotnet-script

using System;

var scorePart1 = File.ReadLines("input")
    .Select(line => line.Take(line.Length /2).Intersect(line.Skip(line.Length / 2)).First())
    .Select(item => char.IsLower(item) ?  (int) item - 96 : (int) item - 38)
    .Sum();

Console.WriteLine($"Score part 1: {scorePart1}");

// Part 2
var scorePart2 = File.ReadLines("input")
    .Chunk(3)
    .Select(items => items[0].Intersect(items[1]).Intersect(items[2]).First())
    .Select(item => char.IsLower(item) ?  (int) item - 96 : (int) item - 38)
    .Sum();

Console.WriteLine($"Score part 2: {scorePart2}");
