import random
import os

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
from hangman_art import logo,stages
print(logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('cls')
    if guess in display:
      print(f"You have already guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
      letter = chosen_word[position]
     ###   print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
      if letter == guess:
          display[position] = letter

    #Check if user is wrong.
    
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    if guess not in chosen_word:
      print(f"You guessed {guess}, it is not in the letter, so you lost a life")
      lives -= 1
      
    if lives == 0:
      end_of_game = True
      print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])