import random

words = ["python", "apple", "chair", "table", "mouse"]

word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("Welcome to Hangman Game!")

while incorrect_guesses < max_guesses:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        incorrect_guesses += 1
        print("Wrong guess!")
        print("Remaining guesses:", max_guesses - incorrect_guesses)

else:
    print("\nGame Over!")
    print("The word was:", word)
