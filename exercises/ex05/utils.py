"""More Practice with list Utility Functions."""

__author__ = "730607734"


def only_evens(all_numbers: list[int]) -> list[int]:
    """Returning only the elemenats of the input that are even."""
    result: list[int] = []
    for i in range(len(all_numbers)):
        if all_numbers[i] % 2 == 0:
            result = result + [all_numbers[i]]
    return result


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Generating all the elements from the two lists into a new list."""
    result: list[int] = []
    for i in range(len(first_list)):
        result.append(first_list[i])
    for i in range(len(second_list)):
        result.append(second_list[i])
    return result


def sub(a_list: list[int], begin: int, stop: int) -> list[int]:
    """Generating a list which is a subset of a given list between the specified start and end index."""
    if len(a_list) == 0 or begin >= len(a_list) or stop <= 0:
        return []
    if begin < 0:
        begin = 0
    if stop > len(a_list):
        stop = len(a_list)
    result: list[int] = []
    i = begin
    while i < stop:
        result = result + [a_list[i]]
        i += 1
    return result
