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

    $is_not_first_column = $j >= 1;
    $is_not_last_column = $j < count($array[0]) - 1;
    $is_not_first_line = $i >= 1;
    $is_not_last_line = $i < count($array) - 1;

    // Same line, on the left
    if($is_not_first_column) {
        $ret[] = $array[$i][$j - 1];
    }
    // Same line, on the right
    if($is_not_last_column) {
        $ret[] = $array[$i][$j + 1];
    }
    // Below
    if($is_not_last_line) {
        $ret[] = $array[$i + 1][$j];
    }
    // Up
    if($is_not_first_line) {
        $ret[] = $array[$i - 1][$j];
    }
    // Diagonal up-left
    if ($is_not_first_line && $is_not_first_column) {
        $ret[] = $array[$i - 1][$j - 1];
    }
    // Diagonal up-right
    if ($is_not_first_line && $is_not_last_column) {
        $ret[] = $array[$i - 1][$j + 1];
    }
    // Diagonal down-left
    if ($is_not_last_line && $is_not_first_column) {
        $ret[] = $array[$i + 1][$j - 1];
    }
    // Diagonal down-right
    if ($is_not_last_line && $is_not_last_column) {
        $ret[] = $array[$i + 1][$j + 1];
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

function has_four_occupied_neighbours($neighbours) : bool {
    $count = 0;
    foreach($neighbours as $neighbour) {
        if ($neighbour == '#') {
            $count++;
        }
    }
    return $count >= 4;
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

function part_1(): void {
    $state = get_lines();
    $previous_state = null;

    while(1) {
        if ($state == $previous_state) {
            echo('Part 1: ' . count_occupied($state) . "\n");
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
                    if (has_four_occupied_neighbours($neighbours)) {
                        $state[$i][$j] = 'L';
                    };
                }

            }
        }
    }


}

part_1();
?>
