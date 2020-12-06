<?php
$handle = fopen("input", "r");
if (!$handle) {
    throw new Exception("File error");
}

$groups = array();
$current_group = array();
while (($file_line = fgets($handle)) !== false) {
    $line = trim($file_line);
    if ($line == "") {
        $groups[] = $current_group;
        $current_group = array();
    }
    else {
        $chars = str_split($line);
        foreach ($chars as $char) {
            if (!in_array($char, $current_group)) {
                $current_group[] = $char;
            }
        }
    }
}
$groups[] = $current_group;

$counts = 0;
foreach ($groups as $group) {
    $counts += count(array_unique($group));
}

echo("Sum of counts: " . $counts . "\n");
fclose($handle);
?>
