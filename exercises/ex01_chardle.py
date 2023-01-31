"""EX01 - Chardle - A cute step toward Wordle."""

_author_ ="730607734"
five_letters_word: str =input("Enter a 5-character word: ")
only_one_character: str =input("Enter a single character: ")
print ("Searching for " + only_one_character + " in " + five_letters_word)
if(only_one_character == five_letters_word[0]) :
    print(only_one_character + " found at index 0")
else:
    if(only_one_character == five_letters_word[1]):
        print(only_one_character + " found at index 1")
    else:
        if(only_one_character==five_letters_word[2]):
            print(only_one_character + " found at index 2")
        else:
            if(only_one_character==five_letters_word[3]):
                print(only_one_character + " found at index 3")
            else:
                if(only_one_character==five_letters_word[4]):
                    print(only_one_character + " found at index 4")
five_letters_word: str =input("Enter a 5-character word: ")
only_one_character: str =input("Enter a single character: ")
print ("Searching for" + only_one_character + " in " + five_letters_word)
if(only_one_character == five_letters_word[0]) :
    number_of_character= number_of_character + 1
    print(only_one_character + " found at index 0")
else:
    if (only_one_character == five_letters_word[1]):
        print(only_one_character+ " found at index 1")
        if (only_one_character== five_letters_word[2]):
            print(only_one_character +" found at index 2" )
        else:
            if(only_one_character== five_letters_word[3]):
                print(only_one_character +" found at index 3")
            else:
                if(only_one_character== five_letters_word[4]):
                    print(only_one_character +" found at index 4")
five_letters_word: str =input("Enter a 5-character word: ")
only_one_character: str =input("Enter a single character: ")
print ("Searching for " + only_one_character + " in " + five_letters_word)
if(only_one_character == five_letters_word[0]):
    print (only_one_character + " found at index 0")
else:
    if (only_one_character == five_letters_word[1]):
        print(only_one_character + " found at index 1")
    else:
        if (only_one_character == five_letters_word[2]):
            print(only_one_character + " found at index 2")
        else:
            if(only_one_character == five_letters_word[3]):
                print(only_one_character + " found at index 3")
            else:
                if(only_one_character ==five_letters_word[4]):
                    print(only_one_character + " found at index 4")

five_letters_word: str =input("Enter a 5-character word: ")
only_one_character: str =input("Enter a single character: ")
if(len(five_letters_word)!= int(5)):
    print("Error:Word must contain 5 characters")

if(len(only_one_character)!=int(1)):
    print("Error:Character must be a single character")