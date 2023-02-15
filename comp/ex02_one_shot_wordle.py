"""One shot Wordle Exercise"""

_author_= "730607734"

Max_Attempts= 4
Word_Length= 6

def __init__(self, secret: str):
    self.secret: str = secret
    self.attempts= []
    pass

def attempt(self, word:str):
    self.attempts.append(word)

@property
def is_solved(self):
    return len(self.attempts) > 0 and self.attempts[-1] == self.secret

@property
def remaining_attempts(self)-> int:
    return self .Max_Attempts - len(self.attempts)

@property 
def can_attempt(self):
    return self .remaining_attempts == 0 and not self.is_solved
    


def main():
    print("Hello Wordle!")
    wordle =("python")
    while wordle.can_attempt:
        x = input ("What is your 6-letter guess?")
        wordle.attempt(x)

    if wordle.is_solved:
        print("Woo! You got it!")
    else:
        print("That was not 6 letters! Try again: ")
       


