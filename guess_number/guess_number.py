import random

top_of_range = input("Type a range of number to guess: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time")
        quit()
else:
    print("Please type a number")
    quit()
    
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        
        if user_guess == random_number:
            print("You got it!")
            break
        elif user_guess > random_number:
            print("You were above the number")
            continue
        else:
            print("You were below the number")
            continue
    else:
        print("Please type a number")
        continue
    
           
print("You got it in ", guesses, " guesses")
        