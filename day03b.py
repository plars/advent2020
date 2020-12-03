#!/usr/bin/env python3

with open("day03.txt") as f:
    # This should get us everything without newlines
    map = f.read().splitlines()

width = len(map[0])


def find_trees(dx, dy):
    trees = 0
    x = 0
    for y in range(0, len(map), dy):
        if map[y][x] == "#":
            trees += 1
        x = (x+dx) % width
    return trees


paths = [(1, 1),
         (3, 1),
         (5, 1),
         (7, 1),
         (1, 2)]
answer = 1
for path in paths:
    answer *= find_trees(*path)
print("Answer: {}".format(answer))
