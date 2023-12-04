<?php

function get_lines(): array
{
    $handle = fopen("input", "r");
    if (!$handle) {
        throw new Exception("File error");
    }

    $lines = array();
    while (($file_line = fgets($handle)) !== false) {
        $lines[] = trim($file_line);
    }
    return $lines;
}

function get_numbers_array_from_string($line): array
{
    $numbers = explode(" ", trim($line)); // split by space
    $numbers = array_filter($numbers, fn($value): int => $value != ""); // we may have double spaces for single-digits numbers
    $numbers = array_map(fn($value): int => (int) $value, $numbers); // cast to int

    return $numbers;
}

$lines = get_lines();
$totalWorth = 0;
foreach ($lines as $line) {
    $cardRegex = "/Card[\s]+([\d]+): /";

    // Get card ID
    preg_match($cardRegex, $line, $matches);
    $cardId = (int) $matches[1];

    // Line without the Card <num>:
    $lineWithoutCardId = trim(preg_replace($cardRegex, "", $line));
    $lineWithoutCardIdExploded = explode("|", $lineWithoutCardId);

    $winningNumbers = get_numbers_array_from_string($lineWithoutCardIdExploded[0]);
    $playedNumbers = get_numbers_array_from_string($lineWithoutCardIdExploded[1]);

    // Get intersection of played and winning numbers
    $intersection = array_intersect($winningNumbers, $playedNumbers);
    $cardValue = 0;
    if (count($intersection) > 0) {
        $cardValue = pow(2, count($intersection) - 1);
    }
    $totalWorth += $cardValue;
}

echo "Part 1: $totalWorth\n";
