import random

play_again = "yes"

while play_again.lower() == "yes":
    number = random.randint(1, 20)
    guess = None
    attempts = 0

    print("\nI'm thinking of a number between 1 and 20.")

    while guess != number:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")

    print(f"🎉 You got it in {attempts} tries!")

    # Ask if they want to play again
    play_again = input("Do you want to play again? (yes/no): ")

print("Thanks for playing! 👋")
