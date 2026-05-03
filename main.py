import random


def generate_secret_number():
    """Generate 4-digit number with unique digits, not starting with 0."""
    digits = list(range(10))
    first = random.choice(range(1, 10))
    digits.remove(first)

    remaining = random.sample(digits, 3)
    return str(first) + ''.join(str(d) for d in remaining)


def validate_input(guess):
    """Check input and return error message or None."""
    errors = []

    if len(guess) != 4:
        errors.append("Number must have 4 digits")

    if not guess.isdigit():
        errors.append("Only digits allowed")

    if guess.startswith("0"):
        errors.append("Number cannot start with 0")

    if len(set(guess)) != 4:
        errors.append("Digits must be unique")

    if errors:
        return ", ".join(errors)

    return None


def calculate_bulls_and_cows(secret, guess):
    """Return number of bulls and cows."""
    bulls = 0
    cows = 0

    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1

    return bulls, cows


def format_result(bulls, cows):
    """Format output text."""
    bull_word = "bull" if bulls == 1 else "bulls"
    cow_word = "cow" if cows == 1 else "cows"

    return f"{bulls} {bull_word}, {cows} {cow_word}"


def play_game():
    """Main game loop."""
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")

    secret = generate_secret_number()
    guesses = 0

    while True:
        guess = input("Enter a number:\n>>> ").strip()

        error = validate_input(guess)
        if error:
            print(error)
            print("-----------------------------------------------")
            continue

        guesses += 1
        bulls, cows = calculate_bulls_and_cows(secret, guess)

        if bulls == 4:
            print(f"Correct, you've guessed the right number in {guesses} guesses!")
            print("-----------------------------------------------")
            print("That's amazing!")
            break
        else:
            print(format_result(bulls, cows))
            print("-----------------------------------------------")


if __name__ == "__main__":
    play_game()