import random
random_number = random.randint(1,100)
Name = input("What's your name?")
attempts = 0
print("Hello", Name, "Welcome to the number guessing game!")
print("I'm thinking of a number between 1 through 100")

#setting the loop to run until the user guesses the number correctly or decides to quit
while True:
    guess = int((input("Can you guess the number? ")))
    attempts +=1
    if guess < random_number:
        print("Too low!")
    elif guess > random_number:
        print("Too high!")
    elif guess == random_number:
#if the user guesses the number correctly, congratulate them and ask if they want to play again
        print("Congratulations", Name, "You guessed the number in", attempts, "attempts!")
        print("Would you like to play again? (yes/no)")
        if input().lower() == "yes":
            random_number = random.randint(1,100)
            attempt = 0
        elif input().lower() == "no":
            print("Thanks for playing! Goodbye!")
            break 
