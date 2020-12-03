#!/usr/bin/env python3

with open("day03.txt") as f:
    # This should get us everything without newlines
    map = f.read().splitlines()

width = len(map[0])
trees = 0
x = 0
for y in range(len(map)):
    if map[y][x] == "#":
        trees += 1
    x = (x+3) % width

print("Trees: {}".format(trees))
