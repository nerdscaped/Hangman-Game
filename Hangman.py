from ntpath import join
from posixpath import split
from english_words import english_words_set
import random

words = english_words_set

random_word = random.choice(list(words)).lower()
print(random_word)

string=[]
for dash in range(len(random_word)):
    string.append("_")

print("The length of your word is {} characters long.\n".format((len(random_word))))

turns = 1
while turns <= 7:
    print(string)
    choice = input("Go no. {}:\nPick a letter: \n".format(turns))
    if random_word.find(choice) != -1:
        for i, letter in enumerate(random_word):
            if letter == choice:
                string[i] = letter        
            else:
                continue
        if string == list(random_word):
            print("You Won!")
            break 
    else:
        turns += 1
    if turns == 7:
        print("Final go!")


