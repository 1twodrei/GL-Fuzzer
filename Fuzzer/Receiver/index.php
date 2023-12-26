<?php
$payload = $_GET['xss'] ?? '';

if (!empty($payload)) {
    $file = fopen('confirmed.txt', 'a'); 
    fwrite($file, $payload . PHP_EOL);
    fclose($file);

    echo 'Received and stored XSS Payload: ' . $payload;
} else {
    echo 'No XSS Payload received';
}
?>
