<?php
$handle = fopen("input", "r");
if (!$handle) {
    throw new Exception("File error");
}

$groups = array();
$groups_size = array();
$current_group = array();
$current_group_size = 0;
while (($file_line = fgets($handle)) !== false) {
    $line = trim($file_line);
    if ($line == "") {
        $groups[] = $current_group;
        $groups_size[] = $current_group_size;
        $current_group = array();
        $current_group_size = 0;
    }
    else {
        $current_group_size += 1;
        $chars = str_split($line);
        foreach ($chars as $char) {
            $current_group[] = $char;
        }
    }
}
$groups[] = $current_group;
$groups_size[] = $current_group_size;

$counts = 0;
foreach ($groups as $idx=>$group) {
    $group_size = $groups_size[$idx];
    $frequences = array_count_values($group);

    foreach ($frequences as $item_freq) {
        if ($item_freq == $group_size) {
            $counts += 1;
        }
    }
}

echo("Sum of counts: " . $counts . "\n");
fclose($handle);
?>
