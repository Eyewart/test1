import os
import random
import pickle
from data_pendu import *

# function that verifies if
def pick_a_numb():
    return random.choice(words_list)

def get_score(file_name):
    if os.path.exists(file_name):
        with open(file_name, "rb") as score_file:
            # fetching the dict stored in our file
            my_pickler1 = pickle.Unpickler(score_file)
            player_score = my_pickler1.load()
    return player_score

def check_point(word, rounds):
    if rounds<8 and rounds>0:
        attempt_word=input("What's the hidden word?")
        if attempt_word==word:
            end=True
            try_again=False
            return end, try_again
        else:
            print("Wrong one!")

def convert_star_word(word):
    rand_word_star = ""
    rand_word_star = list(rand_word_star)
    for x in word:
        rand_word_star.append("*")
    rand_word_star = ''.join(rand_word_star)
    return rand_word_star

def save_score(player_name, new_entry, file_name, found):
    if os.path.exists(file_name):
        with open(file_name,"rb") as score_file:
            # fetching the dict stored in our file
            my_pickler1=pickle.Unpickler(score_file)
            player_score=my_pickler1.load()
        # checking if the name exists and adapt the new score
        for existing_name, existing_score in player_score.items():
            if existing_name==player_name:
                player_score[existing_name]=new_entry[player_name]
                found = True
                with open(file_name, "wb") as score_file:
                    my_pickler2 = pickle.Pickler(score_file)
                    my_pickler2.dump(player_score)
        if found is False:
            player_score.update(new_entry)
            with open(file_name, "wb") as score_file:
                my_pickler2 = pickle.Pickler(score_file)
                my_pickler2.dump(player_score)
        found is False
    else:
        # creating file scores and adding a new entry
        with open(file_name, "wb") as score_file:
            my_pickler2=pickle.Pickler(score_file)
            my_pickler2.dump(new_entry)
