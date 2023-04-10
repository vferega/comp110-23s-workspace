"""Wordle Practice Three!"""
__author__ = "730607734"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(word:str, letter:str) -> bool:
    assert len(letter) == 1
    for char in word: 
        if char == letter:
            return True
    return False


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    result = ""
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            result +=GREEN_BOX
        elif contains_char(secret, guess[i]):
            result +=YELLOW_BOX
        else:
            result +=WHITE_BOX
    return result


def input_guess(expected_length):
    while True: 
        guess= input("Enter a {} character word :". format(expected_length))
        if len (guess) == expected_length:
            return guess
        print ("That wasn't {} chars! Try again: ")

def main() -> None:
    secret_word = "codes"
    turns_left = 6
    # guessed_letters = set()

    while turns_left > 0:
        print(f"===Turn{7- turns_left}/6 === ")
        guess = input_guess(len(secret_word))
        # guessed_letters.add(guess)
        result = emojified(guess, secret_word)
        print(result)
        if guess == secret_word:
            print(f"You won in {7- turns_left}/{6} turns! ")
            return
        turns_left -= 1
    print(f"X/6 - Sorry, try again tomorrow! ")

if __name__ == "__main__":
    main()

