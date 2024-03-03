#!/usr/bin/python3
""" Finds a peak in a list
"""


def find_peak(list_of_numbers):
    """
    Returns: peak of list_of_numbers or None
    """
    size = len(list_of_numbers)
    mid_e = size
    mid = size // 2

    if size == 0:
        return None

    while True:
        mid_e = mid_e // 2
        if (mid < size - 1 and
                list_of_numbers[mid] < list_of_numbers[mid + 1]):
            if mid_e // 2 == 0:
                mid_e = 2
            mid = mid + mid_e // 2
        elif mid_e > 0 and list_of_numbers[mid] < list_of_numbers[mid - 1]:
            if mid_e // 2 == 0:
                mid_e = 2
            mid = mid - mid_e // 2
        else:
            return list_of_numbers[mid]

