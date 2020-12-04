#!/usr/bin/env python3

valid = 0

with open("day04.txt") as f:
    data = f.read().split("\n\n")

required_fields = ("byr:",
                   "iyr:",
                   "eyr:",
                   "hgt:",
                   "hcl:",
                   "ecl:",
                   "pid:")

for passport in data:
    for field in required_fields:
        if field not in passport:
            break
    else:
        # If we get here, all required fields were present
        valid += 1

print("Valid: {}".format(valid))
