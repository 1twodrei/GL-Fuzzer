#!/bin/bash -S

# run receiver.php in the background:
php -S localhost:8123 -t Receiver &
receiver_pid=$!

python3 fuzzer.py

kill $receiver_pid