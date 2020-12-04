#!/usr/bin/env dotnet-script


using System;
using System.Text.RegularExpressions;


var passports = new List<Dictionary<string, string>>();
var currentPassport = new Dictionary<string, string>();
foreach (string line in File.ReadLines("input"))
{
    if (line == "") {
        passports.Add(currentPassport);
        currentPassport = new Dictionary<string, string>();
    }

    string pattern = @"([a-z]+):([^\s]+)";
    foreach (Match match in Regex.Matches(line, pattern)) {
        foreach(var capture in match.Captures) {
            var split = capture.ToString().Split(":");
            currentPassport.Add(split[0], split[1]);
        }
    }
}
passports.Add(currentPassport);

var requiredFields = new string[] {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
};
var validPassports = 0;
foreach (var passport in passports) {
    if (requiredFields.Intersect(passport.Keys).Count() == requiredFields.Count()) {
        validPassports += 1;
    }
}

Console.WriteLine($"Valid passports (part 1): {validPassports}");
