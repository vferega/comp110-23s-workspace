"""Utils Practice."""
__author__ = "730607734"


def all(all_numbers: list[int], single_number: int) -> int:
 """A returned bool telling us list if the given list of ints is the same as the provided int."""
 if len(all_numbers) == 0:
        return False
 i = 0
 while i < len(all_numbers):
    if all_numbers[i] != single_number:
        return False
    i = i + 1
 return True 



def max(all_numbers: list[int]) -> int: 
 """Returning the largest number in the list."""
 if len(all_numbers) == 0:
    raise ValueError("max()arg is an empty List ")
 maximum = all_numbers[0]
 i = 1
 while i < len(all_numbers):
        if all_numbers[i] > maximum:
            maximum = all_numbers[i]
        i += 1
 return maximum


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
"""True if every element in both lists at every index is equal in both lists."""
if len(first_list) != len(second_list):
    return False
i = 0
while i < len(first_list):
    if first_list[i] != second_list[i]:
        return False
    i += 1
return True 