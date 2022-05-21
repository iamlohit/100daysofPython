import random
from hangman_words import word_list
from hangman_art import stages, logo
from replit import clear
chosen_word = random.choice(word_list)

display = []
word_length = len(chosen_word)

print(f"Chosen word is: {chosen_word}")

display += "_" * word_length
print(logo)
print(display)
end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print(f"You have already guessed {guess}")
        
    for char in range(word_length):
        letter = chosen_word[char]
        if letter == guess:
            display[char] = letter
    print(display)

    if guess not in chosen_word:
            lives -= 1
            print(stages[lives])
            print(f"That was an incorrect guess. You have {lives} left.")
            if lives == 0:
                print(f"You have lost the game.")
                end_of_game = True

    if "_" not in display:
        print("Congratulations, you guessed it right. You have Won.")
        end_of_game = True

