#!/usr/bin/env python3

with open("day06.txt") as f:
    data = f.read().split("\n\n")

total = 0
for group in data:
    group_answers = dict()
    individual_answers = group.split()
    for answers in individual_answers:
        for answer in answers:
            if answer in group_answers:
                group_answers[answer] += 1
            else:
                group_answers[answer] = 1
    total += len([x for x in group_answers.keys()
                  if group_answers[x] == len(individual_answers)])

print("Total: {}".format(total))
