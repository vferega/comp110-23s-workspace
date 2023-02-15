"""One shot Wordle Exercise"""

_author_= "730607734"

import random

word_list = ["python", "hi" , "okk", "whyy", "nooooooo" , "tootle", "snakes"]

Max_Attempts = 5
secret_word = "python"

for i in range(Max_Attempts):
    attempts_remaining = Max_Attempts - i
    guess = input (f"What is your 6-letter guess?")
    if len(guess)!= 6:
        print ("That was not 6 letters! Try again: ")
        continue
    if guess == secret_word:
        print("Woo! You got it!")
        break
    else:
        print("Not quite. Play again soon!")


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

result = " "
i= 0

while i <len(secret_word) and i < len(guess):
    if guess[i] == secret_word[i]:
        result += GREEN_BOX
    else:
        result += WHITE_BOX
    i += 1
while i<6:
    result += WHITE_BOX
    i += 1

if guess == secret_word:
    print (result)
    print ("Woo! You got it!")
else:
    print(result)
    print("Not quite. Play again soon!")
    
