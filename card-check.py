#!/usr/bin/env python3

import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

print("Hold a tag near the reader")

while True:
    id = reader.read()
    print("This card's ID is",id)
    #print(text)