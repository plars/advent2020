#!/usr/bin/env python3

from math import floor


def find_seat(lowest, highest, lowchar, highchar, sequence):
    """Find the number from highest to lowest referred to by sequence

    :param lowest: lowest number
    :param highest: highest number
    :param lowchar: character denoting to take the low range
    :param highchar: character denoting to take the high range
    :param sequence: list of characters describing the location to find
    """
    if lowest == highest:
        return lowest
    middle = floor((lowest + highest) / 2)
    c = sequence.pop()
    if c == lowchar:
        return find_seat(lowest, middle, lowchar, highchar, sequence)
    else:
        return find_seat(middle+1, highest, lowchar, highchar, sequence)


highest = 0

with open("day05.txt") as f:
    data = f.read().splitlines()

for seat in data:
    row_seq = list(reversed(seat[:7]))
    col_seq = list(reversed(seat[-3:]))
    row = find_seat(0, 127, "F", "B", row_seq)
    col = find_seat(0, 7, "L", "R", col_seq)
    seat_number = row * 8 + col
    highest = max(seat_number, highest)

print("Highest seat number: {}".format(highest))
