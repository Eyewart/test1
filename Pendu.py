""" SUMMARY OF THE PROGRAM FEATURES
the computer chooses a random word in his list
 it becomes the word to look up for the user
 the user has to identify himself
 the user has 8 chances before to lose
 the user enters a letter and so he looses a chance
 if it's correct we fill the screen, if not we show again the screen
 after the game we will save the score
 if the file does not exist, we have to create it
 we save the score in a file, and the scores will be in a dict"""

"""STILL TO DO
-to save properly the score in a file: 100%
-show the current score (saved in the scores file) of the user when he enters his name:100% 
-let the user type the final word before the last round:100%"""

from functions_pendu import *

os.chdir("C:/test")
end=False
found=False
try_again=True

# the user has to identify himself
player_name=input("What's your name?")

# show the current score of the user
player_score=get_score("scores")
for existing_name, existing_score in player_score.items():
    if existing_name == player_name:
        print("Your last score was {}".format(existing_score))

# the computer will draw a random word
rand_word=pick_a_numb()
# generating the stars word
current_string = convert_star_word(rand_word)

# running the loop game
while end is False:
    try_again=True
    print("The current word is: {}".format(current_string))

    # checking if the user knows which word is behind
    x=check_point(rand_word, rounds)
    # we convert the x tuple to list to fetch the "end" and "try_again" values
    if x is not None:
        y=list(x)
        end, try_again=y

    # we have to check that the user has entered a correct letter
    while try_again is True:
        letter_chosen = input("Please pick a letter between A and Z")
        if len(letter_chosen)>1 or len(letter_chosen)==0:
            print("The letter entered is not correct. Please try again")
        elif letter_chosen.isalpha() is False:
            print("The letter entered is not correct. Please try again")
        else:
            try_again=False

    # function to verify if entered letter is in the chosen word
    letter_chosen=letter_chosen.lower()
    current_string=list(current_string)
    # replace the stars by the letter found by the user if any
    for i, x in enumerate(rand_word):
        if x == letter_chosen:
            current_string[i]=letter_chosen

    current_string="".join(current_string)

    # going to the next round if there's still credit
    if current_string==rand_word:
        end=True
    elif rounds>0:
        rounds-=1
        print("The remaining rounds are: {}".format(rounds))
    else:
        print("You have failed and the hidden word was '{}'".format(rand_word))
        end=True

# saving the score of the user
score=rounds
new_entry={player_name: score}

# saving the score in a file
save_score(player_name, new_entry, "scores", found)

# recuperating the last saved score from the file
player_score=get_score("scores")
print("The current scores are: {}".format(player_score))


