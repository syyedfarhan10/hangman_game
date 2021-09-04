import random

# creating and printing the hangman logo

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)
print("\n\n")

# creating a list of words
wordlist = ["chelsea", "liverpool", "manchester", "madrid", "barcelona", "paris", "turin"]

# choosing a random word from the wordlist:
final_word = random.choice(wordlist)

# creating an empty list
display = []

# creating and printing blanks(= number of letters in the chosen word"
for x in final_word:
    display += "_"
print(f"{''.join(display)}")

endgame = True
life = 6

# while the condition is true execute the game
while endgame:
    guess = input("Enter any letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for pos in range(0, len(final_word)):
        letter = final_word[pos]
        if guess == letter:         # barcelona r
            display[pos] = guess
    print(f"{''.join(display)}")

    # if guess is not in the word, decrease the life by one and check if you've run out of lives
    if guess not in final_word:
        print(f"You've guessed {guess}, but that's not int the word")
        life -= 1
        if life == 0:
            endgame = False
            print("You've no more guesses left!")
            print("You have lost :(")

    # if there are no more blanks left in the word, you win
    if "_" not in display:
        endgame = False
        print("You win!")
