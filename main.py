import words_fetcher
import random


def congratulate_user():
    print(f"Congratulations, you won! your words: {set(guesses)}")


def is_game_over():
    return guessed == WORDS_TO_WIN or errors == ERRORS_TO_LOSE


guessed = 0
errors = 0

guesses = []

WORDS_TO_WIN = 5
ERRORS_TO_LOSE = 3

words = words_fetcher.fetch_words(min_letters=9, max_letters=9)
full_list = words_fetcher.fetch_words(min_letters=3, max_letters=9)
word = words[random.randrange(0, len(words))]

print(f"Can you make up {WORDS_TO_WIN} words from letters in word provided by me?")
print(f"Your word is '{word}'")


while not is_game_over():
    guess = input("Your next take: ")
    if guess in full_list:
        guesses.append(guess)
        if guesses.count(guess) > 1:
            print("You've entered these word, DRY!")
        else:
            guessed += 1
            print(f"That's right! {WORDS_TO_WIN - guessed} to go")
        if guessed == WORDS_TO_WIN:
            congratulate_user()
            exit()
    else:
        errors += 1
        print(f"Oops :( No such word, you have {ERRORS_TO_LOSE - errors} lives more")
