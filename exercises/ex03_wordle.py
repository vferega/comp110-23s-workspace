"""Wordle Practice Three!"""
__author__ = "730607734"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(word:str, letter:str) -> bool:
    assert len(letter) == 1
    i:int = 0 
    while i < len(word):
        if word[i] == letter:
            return True
        else:
            i= i+1
    return False


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    result = ""
    i: int = 0
    while i < (len(guess)):
        if guess[i] == secret[i]:
            result +=GREEN_BOX
        elif contains_char(secret, guess[i]):
            result +=YELLOW_BOX
        else:
            result +=WHITE_BOX
        i+= 1
    return result


def input_guess(expected_length: int) ->str:
    while True: 
        guess= input(f"Enter a {expected_length} character word: ")
        if len(guess) == expected_length:
            return guess
        print (f"That wasn't {expected_length} chars! Try again: ")

def main() -> None:
    secret_word:str = "codes"
    turns:int = 1
    if_won:bool = False 
    # guessed_letters = set()

    while turns <= 6 and not if_won:
        print(f"===Turn {turns}/6 ===")
        guess = input_guess(len(secret_word))
        # guessed_letters.add(guess)
        result = emojified(guess, secret_word)
        print(result)
        if guess == secret_word:
            print(f"You won in {turns}/6 turns!")
            if_won = True
        turns += 1
    if turns > 6:
         print(f"X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()

