import random

secret_number = random.randint(1, 100)

print("Guess a number between 1 and 100")
for attempt in range(1, 11):
    print("Guess #{}".format(attempt))
    guess = int(input())

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    elif guess == secret_number:
        print("Correct")
        break
if guess != secret_number:
    print("The secret number was", secret_number)
