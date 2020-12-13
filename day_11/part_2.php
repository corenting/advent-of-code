<?php

function get_lines(): array {
    $handle = fopen("input", "r");
    if (!$handle) {
        throw new Exception("File error");
    }

    $lines = array();
    while (($file_line = fgets($handle)) !== false) {
        $lines[] = str_split(trim($file_line)); ;
    }
    return $lines;
}

function get_neighbours_seats($array, $i, $j): array {
    $ret = array();

    // Seat on the left
    for ($y = $j - 1; $y >= 0; $y--) {
        if ($array[$i][$y] != '.') {
            $ret[] = $array[$i][$y];
            break;
        }
    }

    // Seat on the right
    for ($y = $j + 1; $y < count($array[$i]); $y++) {
        if ($array[$i][$y] != '.') {
            $ret[] = $array[$i][$y];
            break;
        }
    }

    // Seat up
    for ($x = $i - 1; $x >= 0; $x--) {
        if ($array[$x][$j] != '.') {
            $ret[] = $array[$x][$j];
            break;
        }
    }

    // Seat down
    for ($x = $i + 1; $x < count($array); $x++) {
        if ($array[$x][$j] != '.') {
            $ret[] = $array[$x][$j];
            break;
        }
    }

    $y = $j + 1;
    for ($x = $i + 1; $x < count($array); $x++) {
        if ($y == count($array[$i])) {
            break;
        }
        if ($array[$x][$y] != '.') {
            $ret[] = $array[$x][$y];
            break ;
        }
        $y++;
    }

    $y = $j - 1;
    for ($x = $i + 1; $x < count($array); $x++) {
        if ($y < 0) {
            break;
        }
        if ($array[$x][$y] != '.') {
            $ret[] = $array[$x][$y];
            break ;
        }
        $y--;
    }


    $y = $j + 1;
    for ($x = $i - 1; $x >= 0; $x--) {
        if ($y == count($array[$i])) {
            break;
        }
        if ($array[$x][$y] != '.') {
            $ret[] = $array[$x][$y];
            break ;
        }
        $y++;
    }

    $y = $j - 1;
    for ($x = $i - 1; $x >= 0; $x--) {
        if ($y < 0) {
            break;
        }
        if ($array[$x][$y] != '.') {
            $ret[] = $array[$x][$y];
            break ;
        }
        $y--;
    }

    return $ret;
}

function has_adjacent_occupied_seats($neighbours) : bool {
    foreach($neighbours as $neighbour) {
        if ($neighbour == '#') {
            return true;
        }
    }
    return false;
}

function has_five_occupied_neighbours($neighbours) : bool {
    $count = 0;
    foreach($neighbours as $neighbour) {
        if ($neighbour == '#') {
            $count++;
        }
    }
    return $count >= 5;
}

function count_occupied($state): int {
    $occupied = 0;
    for ($i = 0; $i < count($state); $i++) {
        for ($j = 0; $j < count($state[$i]); $j++) {
            if ($state[$i][$j] == "#") {
                $occupied++;
            }
        }

    }
    return $occupied;
}

function print_state($state) {
    for ($i = 0; $i < count($state); $i++) {
        for ($j = 0; $j < count($state[$i]); $j++) {
            echo($state[$i][$j]);
        }
        echo("\n");
    }
    echo("\n\n");
}

function part_2(): void {
    $state = get_lines();
    $previous_state = null;

    while(1) {
        if ($state == $previous_state) {
            echo('Part 2: ' . count_occupied($state) . "\n");
            exit(0);
        }

        $previous_state = $state;
        //print_state($state);

        for ($i = 0; $i < count($state); $i++) {
            for ($j = 0; $j < count($state[$i]); $j++) {
                $neighbours = get_neighbours_seats($previous_state, $i, $j);
                if ($previous_state[$i][$j] == '.') {
                    continue;
                }
                else if ($previous_state[$i][$j] == 'L') {
                    if (!has_adjacent_occupied_seats($neighbours)) {
                        $state[$i][$j] = '#';
                    }
                }
                else {
                    if (has_five_occupied_neighbours($neighbours)) {
                        $state[$i][$j] = 'L';
                    };
                }

            }
        }
    }


}

part_2();
?>
