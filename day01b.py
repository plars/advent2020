#!/usr/bin/env python3

entries = list()
with open("day01.txt") as f:
    for entry in f.readlines():
        entries.append(int(entry))

for x in range(len(entries)):
    cur = entries.pop()
    diff = 2020-cur
    for y in range(len(entries)):
        e1 = entries[y]
        diff2 = diff - e1
        if diff2 < 0:
            continue
        if diff2 in entries[y+1:]:
            print(cur*e1*diff2)
            raise SystemExit
