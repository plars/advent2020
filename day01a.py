#!/usr/bin/env python3

entries = set()
with open("day01.txt") as f:
    for entry in f.readlines():
        entries.add(int(entry))

for _ in range(len(entries)):
    cur = entries.pop()
    diff = 2020-cur
    if diff in entries:
        print(cur*diff)
        raise SystemExit
