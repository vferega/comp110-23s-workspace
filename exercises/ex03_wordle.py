"""Wordle Practice Three!"""
__author__ = "730607734"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
letter:"p"
word:"python"
secret=word


def contains_char(word:str, letter:str) -> bool:

"""Two strings one being a word of chosen length and second being a letter found or not found in the previous string."""
assert len(letter) == 1
for char in word: 
        if char == letter:
            return True
return False

def emojified (guess: str, secret: str) -> str: 
    
"""Two strings of same length attempting to produce colored boxes."""
assert len(guess) == len(secret)
result = ""
for i, char in enumerate(guess):
        if char == secret [i]:
            result += GREEN_BOX
        elif contains_char(secret, char):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
return result


