<?php
$payload = $_GET['xss'] ?? '';

if (!empty($payload)) {
    // Store the payload in a file
    $file = fopen('confirmed.txt', 'a'); // Opens the file in append mode
    fwrite($file, $payload . PHP_EOL); // Write the payload to the file with a new line
    fclose($file);

    // Optional: Notify the user that the payload was received
    echo 'Received and stored XSS Payload: ' . $payload;
} else {
    // No payload received
    echo 'No XSS Payload received';
}
?>
