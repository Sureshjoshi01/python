# Word Guessing Game

# The Word Guessing Game is a fun and interactive project where players try to
# guess a secret word, one letter at a time. The word is selected randomly from a list
# of words stored in a text file. The player has six attempts to guess the word, with
# each incorrect guess reducing the remaining attempts. Correctly guessed letters
# are revealed in their respective positions, while incorrect guesses prompt the
# player to try again.


import random
def word_select():
    with open("words.txt", "r") as file:
        words = [line.strip().lower() for line in file if line.strip()]
    if not words:
        raise ValueError("words.txt has no usable words.")
    return random.choice(words)
def guess_word():
    count = 0
    guessed_letters = set()
    word = word_select()
    display = "_" * len(word)
    print(display)
    while count < 6:
        letter = input("Enter a letter: ").strip().lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Enter one alphabetic letter.")
            continue
        if letter in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.add(letter)
        if letter in word:
            print("Good guess!")
            display_list = list(display)
            for i, character in enumerate(word):
                if character == letter:
                    display_list[i] = letter
            display = "".join(display_list)
        else:
            count += 1
            print(f"Wrong guess. Attempts left: {6 - count}.")
        print(display)
        if display == word:
            return True, word
    return False, word
def main():
    while True:
        won, word = guess_word()
        if won:
            print("Congratulations!")
        else:
            print(f"You exhausted all attempts. The correct word was: {word}")
        while True:
            answer = input("Do you want to guess again (Y/N)? ").strip().upper()
            if answer in ("Y", "N"):
                break
            print("Please enter Y or N.")
        if answer == "N":
            break
main()