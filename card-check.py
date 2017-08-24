#!/usr/bin/env python3

import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

print("To check the ID hold the card / tag near to the reader")
print("When done press CTRL + C to exit")

try:
    while True:
        id, text = reader.read()
        print("This card's ID is",id)
except KeyboardInterrupt:
    print("Exit")