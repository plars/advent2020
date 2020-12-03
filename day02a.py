#!/usr/bin/env python3
import re

with open("day02.txt") as f:
    data = f.readlines()

valid = invalid = 0

p = re.compile('(\d+)-(\d+) (\w): (\w+)')
for line in data:
    m = p.match(line)
    (low, high, letter, password) = m.groups()
    if int(low) <= password.count(letter) <= int(high):
        valid += 1
    else:
        invalid += 1
print("valid passwords: {}".format(valid))
print("invalid passwords: {}".format(invalid))
