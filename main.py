import random

randomNumber = random.randint(0, 100)

print("Welcome to the Numebr Guessing Game!")
print("A simple CLI game built in Python. Let's start!")
print("Hint: it's a number between 0-100")

while True:
    userGuess = input("\nWhich number am I thinking of? ")

    # Convert input to integer
    try:
        userGuess = int(userGuess)
    except ValueError:
        print("Please enter a valid number!")
        continue
    
    # Game logic
    if userGuess == randomNumber:
        print(f"🎉 You are correct! The number is {randomNumber}.")
        break  # exit the loop
    elif userGuess > randomNumber:
        print("Too high! Try again.")
    else:
        print("To low! Try again.")