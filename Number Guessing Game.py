import random
def ngg():
    number = random.randint(1,10)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 10. Can you guess it?")
    while True:
      try:
        guess = int(input("enter the nubrer: "))
        attempts += 1
        if guess > number:
            print("Too high! Try again.")
        elif guess < number:
            print("Too low! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
            break
      except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")
ngg()
         