import random

print("Welcome to Number Guessing Game!")

again = "yes"

while again == "yes":

    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5
    win = False

    print("\nI have chosen a number between 1 and 100.")
    print("You have 5 chances to guess it.")

    while attempts < max_attempts:

        print("\n-------------------------")
        print("Attempt", attempts + 1, "of 5")
        print("Lives remaining:", max_attempts - attempts)

        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Invalid input! Please enter a number.")
            continue

        guess = int(guess)

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts = attempts + 1

        if guess == number:
            print("\nCongratulations! You won!")
            win = True

            if attempts == 1:
                print("Your rank: Excellent!")
            elif attempts == 2:
                print("Your rank: Very good!")
            elif attempts == 3:
                print("Your rank: Good!")
            elif attempts == 4:
                print("Your rank: Accepted!")
            elif attempts == 5:
                print("Your rank: Lucky winner!")

            break

        elif guess > number:
            print("Enter a smaller number.")

        else:
            print("Enter a bigger number.")

        difference = abs(guess - number)

        if difference <= 5:
            print("You are very close!")
        elif difference <= 15:
            print("You are close, but still have some distance!")
        else:
            print("You are very far!")

    if win == False:
        print("\nGame Over! You lost.")
        print("The correct number was:", number)

    again = input("\nDo you want to play again? (yes/no): ")
    again = again.lower()

    while again != "yes" and again != "no":
        print("Please enter yes or no.")
        again = input("Do you want to play again? (yes/no): ")
        again = again.lower()

print("\nThank you for playing!")