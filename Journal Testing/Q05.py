import random
WORDS = ("TRANSMISSION","NETWORK","TOPOLOGY","ETHERNET")
word=random.choice(WORDS)
correct  =word
correct = correct.lower()
jumble = " "
while word:
    position=random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]
print \
""" 
Welcome to Word Jumble Game!!!
-------Guess Computer WORDS ---------
Unscramble the letters to make a word
"""
print "The jumble word is:",jumble
Guess = raw_input("Guess the word:")
while(Guess!=correct) and (Guess != ""):
    print ("Sorry, %s is not exactly jumble " %jumble)
    Guess = raw_input("Please guess again:")
    Guess = Guess.lower()
if Guess == correct:
    print "Thats it! You Guessed it! \n"
