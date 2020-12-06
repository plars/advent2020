#!/usr/bin/env python3

with open("day06.txt") as f:
    data = f.read().split("\n\n")

total = 0
for group in data:
    group_answers = set()
    group = group.replace("\n", "")
    for c in group:
        group_answers.add(c)
    total += len(group_answers)

print("Total: {}".format(total))
