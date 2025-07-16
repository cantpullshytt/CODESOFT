#Password Generator by Sankalp Mishra!!

import random
import string

print("Hey there! Let's make you a secret password nobody can guess.")

def make_secret(howlong, big_letters, small_letters, numbers, funky_stuff):
    stuff = ""
    if big_letters:
        stuff += string.ascii_uppercase
    if small_letters:
        stuff += string.ascii_lowercase
    if numbers:
        stuff += string.digits
    if funky_stuff:
        stuff += string.punctuation

    if not stuff:
        print("Oops! You gotta pick at least one type of character.")
        return None

    result = ""
    for wow in range(howlong):
        result += random.choice(stuff)
    return result

try:
    size = int(input("How many letters do you want? (be brave, pick a big number): "))
    if size < 4:
        print("Come on, at least 4 characters! Try again next time.")
    else:
        print("Do you want UPPERCASE letters? (yes/no)")
        want_big = input().lower().startswith("y")
        print("How about lowercase? (yes/no)")
        want_small = input().lower().startswith("y")
        print("Wanna throw in some numbers? (yes/no)")
        want_numbers = input().lower().startswith("y")
        print("Feeling wild? Add some symbols? (yes/no)")
        want_symbols = input().lower().startswith("y")

        password = make_secret(size, want_big, want_small, want_numbers, want_symbols)
        if password:
            print("\nHere's your secret pass:")
            print(password)
            print("Don't tell anyone!")
except Exception as e:
    print("Hmmm, something went wrong. Try picking a number next time!")