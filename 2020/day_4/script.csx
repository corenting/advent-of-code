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
var validPassports = new List<Dictionary<string, string>>();
var validPassportsCount = 0;
foreach (var passport in passports) {
    if (requiredFields.Intersect(passport.Keys).Count() == requiredFields.Count()) {
        validPassportsCount += 1;
        validPassports.Add(passport);
    }
}
Console.WriteLine($"Valid passports (part 1): {validPassportsCount}");

// Part 2
var validPassportsCountPart2 = 0;
foreach (var passport in validPassports) {
    var allFieldsValid = true;
    foreach (var (key, value) in passport) {
        bool valid = false;
        switch(key)
        {
            case "byr":
                var byr = int.Parse(value);
                valid = byr >= 1920 && byr <= 2002;
                break;
            case "iyr":
                var iyr = int.Parse(value);
                valid = iyr >= 2010 && iyr <= 2020;
                break;
            case "eyr":
                var eyr = int.Parse(value);
                valid = eyr >= 2020 && eyr <= 2030;
                break;
            case "hgt":
                var min = value.Contains("cm") ? 150 : 59;
                var max = value.Contains("cm") ? 193 : 76;
                var hgt = int.Parse(value.Replace("cm", "").Replace("in", ""));
                valid = hgt >= min && hgt <= max;
                break;
            case "hcl":
                var hclRegex = new Regex(@"#[0-9a-f]{6}");
                valid = hclRegex.IsMatch(value);
                break;
            case "ecl":
                var validEcl = new string[] {
                    "amb",
                    "blu",
                    "brn",
                    "gry",
                    "grn",
                    "hzl",
                    "oth",
                };
                valid = validEcl.Contains(value);
                break;
            case "pid":
                var pidRegex = new Regex(@"^\d{9}$");
                valid = pidRegex.IsMatch(value);
                break;
            case "cid":
                valid = true;
                break;
        }
        if (!valid) {
            allFieldsValid = false;
            break;
        }
    }
    validPassportsCountPart2 += allFieldsValid ? 1 : 0;
}
Console.WriteLine($"Valid passports (part 2): {validPassportsCountPart2}");
