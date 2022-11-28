import random

def hangman():
    word = random.choice(["pugger", "tiger", "thor", "superman", "pokemon", "earth"])
    return print(word)
    
name = input("Enter your name: ")
print("Welcome", name)
print("=====================")
print("Try to guess the word in less than 10 attempts")
hangman()
print()