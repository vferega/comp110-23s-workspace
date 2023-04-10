"""One shot Wordle Exercise."""

__author__ = "730607734"


secret_word = "python"
length_of_secret_word = len(secret_word)

guess = input(f"What is your {length_of_secret_word} -letter guess? ")
while len(guess) != 6:
    guess = input(f"That was not {length_of_secret_word} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

result = " "
i = 0

while i < len(secret_word) and i < len(guess):
    if guess[i] == secret_word[i]:
        result += GREEN_BOX
    else:
        matched = False
        the_index = 0
        while not matched and the_index < len(secret_word):
            if the_index != i and guess[i] == secret_word[the_index]:
                matched = True
            else:
                the_index += 1
        if matched:
            result += YELLOW_BOX
        else: 
            result += WHITE_BOX
    i += 1
# print(result)

if guess == secret_word:
    print(result)
    print("Woo! You got it!")
else:
    print(result)
    print("Not quite. Play again soon!")
