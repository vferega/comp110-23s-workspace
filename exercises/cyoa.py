"""Choose your own adventunre experience."""

__author__ = "730607734"


points: int = 0
player: str = ""
pet: str = "Arči"

food = 15
fitness = 15
friends = 15
sleep = 15

heart_emoji = "\U00002764"


def main():
    """Let's take an adventure with our virtual pet Arči - my childhood dog."""
    greet()
    while True:
        print(f" Welcome {player}!{heart_emoji} Here is how {pet} is doing at the moment: Food: {food}, Fitness: {fitness}, Friends: {friends}, Sleep{sleep} ")
        print("What are you and {pet} going to do?  ")
        print(" 1.Give food to {pet}.")
        print(" 2.Take {pet} for a run in a park.")
        print(" 3.Invite {pet}'s friends over.")
        print(" 4. Carry {pet} to his bed.")
        decision = input("Pick a number (1-5) and start your wonderful time with {pet} {heart_emoji}!")
        if decision == "1":
            give_food_to_Arči()
        elif decision == "2":
            go_for_run()
        elif decision == "3":
            call_friends()
        elif decision == "4":
            take_naps()
        elif decision == "5":
            print(f"Ciao {player}, you finished the game with {points}.")
        else:
            print("Please enter a valid input.")


def greet():
    """Greeting to all the lovely players."""
    global player
    print("Hello! Let's take an adventure with your new virtual pet {pet} !")
    player = input("What is your name? ")
    print(f"Pleasure to have you, {player}! Come on let's play!")


def give_food_to_Arči():
    """Earning points every time a player chooses to feed Arči."""
    global food, points
    print(f"Good job {player}! {pet} is fed now.")
    food += 1
    points += 1
    

def go_for_run():
    """Earning points every time a player chooses to take Arči for a run."""
    global fitness, points 
    print(f" Awesome work {player}! You and {pet} are so fit! ")
    fitness += 1
    points += 1
    

def call_friends():
    """Earning points every time a player chooses to call Arči's friends to come play with him."""
    global friends, points
    print(f" Hurray {player}! Your {pet} had a great time! ")
    friends += 1
    points += 1


def take_naps():
    """Earning points every time a player allows Arči to take a nap."""
    global sleep, points
    print(f"Yawn yawn. Sweet dreams {pet}.")
    sleep += 1
    points += 1


    
