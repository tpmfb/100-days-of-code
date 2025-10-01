import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)
# Word list
word_list = word_list

# Pick a random word
chosen_word = random.choice(word_list)
print(chosen_word)  # <-- remove this later so players can't see the answer

# Lives start at 6
lives = 6

# Build display as a list of underscores
display = []
for i in range(len(chosen_word)):
    display.append("_")

print(display)

# Game loop
while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You've already guessed that letter.")
        continue
    # Check each position
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess

    # If wrong guess, lose a life
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess. You have {lives} lives left.")

    # Show progress + ASCII art
    print(stages[lives])

# End game
if "_" not in display:
    print("You win!")
else:
    print("You lose! The word was:", chosen_word)
