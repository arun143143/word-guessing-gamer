import random
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
def get_random_word():
    return random.choice(word_list)

def initialize_game():
    word_to_guess = get_random_word()
    guessed_letters = set()
    max_attempts = 6
    incorrect_attempts = 0
    return word_to_guess, guessed_letters, max_attempts, incorrect_attempts


def display_word(word, guessed_letters):
    masked_word = ""
    for letter in word:
        if letter in guessed_letters:
            masked_word += letter
        else:
            masked_word += "_"
    return masked_word

def word_guessing_game():
    print("Welcome to the Word Guessing Game!")
    word_to_guess, guessed_letters, max_attempts, incorrect_attempts = initialize_game()

    while incorrect_attempts < max_attempts:
        masked_word = display_word(word_to_guess, guessed_letters)
        print("\nCurrent word:", masked_word)
        if "_" not in masked_word:
            print("Congratulations! You guessed the word correctly!")
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word_to_guess:
            incorrect_attempts += 1
            print(f"Oops! '{guess}' is not in the word. Attempts left: {max_attempts - incorrect_attempts}")

    else:
        print(f"\nGame over! The word was '{word_to_guess}'. Better luck next time!")

if __name__ == "__main__":
    word_guessing_game()
