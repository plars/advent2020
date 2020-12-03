#!/usr/bin/env python3
import re
from operator import xor

with open("day02.txt") as f:
    data = f.readlines()

valid = invalid = 0

p = re.compile('(\d+)-(\d+) (\w): (\w+)')
for line in data:
    m = p.match(line)
    (low, high, letter, password) = m.groups()
    if xor(password[int(low)-1] == letter, password[int(high)-1] == letter):
        valid += 1
        print(line)
    else:
        invalid += 1
print("valid passwords: {}".format(valid))
print("invalid passwords: {}".format(invalid))
