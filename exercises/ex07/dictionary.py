"""Dictionary Functions."""

__author__ = "730607734"


def invert(DICTIONARY:dict[str, str]) -> dict[str, str]:
    """Function that inverts the keys and the values in the dictionary."""
    result = {}
    for key, value in DICTIONARY.items():
        if value in result:
            raise KeyError(f"Key Error: Whoops! {value} shouldn't be used twice!! ")
        result[value] = key
    return result 


def favorite_color(colors:dict[str, str])->str:
    """Function that returns the color that appears most frequently & in case of a tie for a favorite color it returns the one that appears int eh dictionary first."""
    frequency_of_occuring = {}
    for color in colors.values():
        if color not in frequency_of_occuring:
            frequency_of_occuring[color] = 0 
        frequency_of_occuring[color] += 1
    maximum = max(frequency_of_occuring.values())
    for color in frequency_of_occuring:
        if frequency_of_occuring[color] == maximum:
            return color 
        

def count(items: list [str]) -> dict [str, int]:
    outcome = {}
    for item in items:
        if item in outcome:
            outcome[item] += 1
        else:
            outcome[item] = 1
    return outcome 
    
