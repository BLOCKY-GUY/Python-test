import random

secret = random.randint(1, 50)
remaining_attempts = 5

print("Welcome to the Number Guessing Game!")
print("Guess a secret number between 1 and 50. You have 5 attempts.")

while remaining_attempts > 0:
    guess = int(input("\nEnter your guess: "))

    if guess == secret:
        print(f" You win! The secret number was {secret}.")
        break
    else:
        remaining_attempts -= 1
        diff = abs(guess - secret)

        if diff <= 3:
            print("Hint:  Hot!")
        elif diff <= 10:
            print("Hint:  Warm!")
        elif diff <= 20:
            print("Hint:  Cold!")
        else:
            print("Hint:  Ice cold!")

        hearts = ""
        for _ in range(remaining_attempts):
            hearts += "Hearts: "
        print(f"Remaining lives: {hearts.strip()}")

if remaining_attempts == 0 and guess != secret:
    print(f"\n Game over! You ran out of attempts. The secret number was {secret}.")
