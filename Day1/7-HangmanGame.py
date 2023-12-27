import random
from HangmanExtra import word_list
from HangmanExtra import stages
from HangmanExtra import logo

print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

user_progress = []
for i in range(0, word_length):
    user_progress += "_"

while lives>0:
    user_guess = input("Guess a letter")
    #belong
    if user_guess in chosen_word:
        
    #doesnt belong
    else: