#!/usr/bin/env python3
import re

valid = 0

with open("day04.txt") as f:
    data = f.read().split("\n\n")


def valid_byr(year):
    return 1920 <= int(year) <= 2002


def valid_iyr(year):
    return 2010 <= int(year) <= 2020


def valid_eyr(year):
    return 2020 <= int(year) <= 2030


def valid_hgt(hgt):
    if hgt.endswith("cm"):
        return 150 <= int(hgt[:-2]) <= 193
    elif hgt.endswith("in"):
        return 59 <= int(hgt[:-2]) <= 76


def valid_hcl(hcl):
    return True


def valid_ecl(ecl):
    return ecl in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def valid_pid(pid):
    return len(pid) == 9


required_fields = {re.compile("byr:(\d{4})"): valid_byr,
                   re.compile("iyr:(\d{4})"): valid_iyr,
                   re.compile("eyr:(\d{4})"): valid_eyr,
                   re.compile("hgt:(\d+((cm)|(in)))"): valid_hgt,
                   re.compile("hcl:(#\w{6})"): valid_hcl,
                   re.compile("ecl:(\w{3})"): valid_ecl,
                   re.compile("pid:(\d+)"): valid_pid
                   }


for passport in data:
    for field, validator in required_fields.items():
        m = field.search(passport)
        if not m:
            break
        if not validator(m.group(1)):
            break
    else:
        # If we get here, all required fields were present
        valid += 1

print("Valid: {}".format(valid))
