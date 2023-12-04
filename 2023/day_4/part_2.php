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

$totalOfCards = 0;

function process_card($card, $cards) {
    $cardRegex = "/Card[\s]+([\d]+): /";
    $copies = [];

    // Get card ID
    preg_match($cardRegex, $card, $matches);
    $cardId = (int) $matches[1];

    // Line without the Card <num>:
    $lineWithoutCardId = trim(preg_replace($cardRegex, "", $card));
    $lineWithoutCardIdExploded = explode("|", $lineWithoutCardId);

    $winningNumbers = get_numbers_array_from_string($lineWithoutCardIdExploded[0]);
    $playedNumbers = get_numbers_array_from_string($lineWithoutCardIdExploded[1]);

    $intersection = array_intersect($winningNumbers, $playedNumbers);
    for ($i = 1; $i <= count($intersection); $i++) {
        array_push($copies, $cards[$cardId + $i - 1]);
    }

    return $copies;
}

$initialCards = get_lines();
$cardsCopiesToProcess = [];

// Process initial cards
foreach ($initialCards as $card) {
    $cardsCopiesToProcess = array_merge($cardsCopiesToProcess , process_card($card, $initialCards));
    $totalOfCards++;
}

// Process copies
while(count($cardsCopiesToProcess) > 0 ) {
    $card = array_pop($cardsCopiesToProcess);
    $cardsCopiesToProcess = array_merge($cardsCopiesToProcess , process_card($card, $initialCards));
    $totalOfCards++;
}

echo "Part 2: $totalOfCards\n";
