#!/usr/bin/env python
from sys import argv
if len(argv) >= 2:
    with open(argv[1], "r") as file:
        print(file.read())
