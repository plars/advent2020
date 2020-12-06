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


all_seats = []

with open("day05.txt") as f:
    data = f.read().splitlines()

for seat in data:
    row_seq = list(reversed(seat[:7]))
    col_seq = list(reversed(seat[-3:]))
    row = find_seat(0, 127, "F", "B", row_seq)
    col = find_seat(0, 7, "L", "R", col_seq)
    seat_number = row * 8 + col
    # Ideally we should keep this sorted
    # but it's a small data set so let's be lazy
    all_seats.append(seat_number)

all_seats.sort()
"""
We're looking for a pattern here like ...25,26,28,29...
Where 27 is the missing number, but the surrounding numbers are present
"""
for x in range(len(all_seats)-2):
    if (all_seats[x+1] == all_seats[x] + 2 and
       all_seats[x+2] == all_seats[x] + 3):
        print("Seat #: {}".format(all_seats[x] + 1))
