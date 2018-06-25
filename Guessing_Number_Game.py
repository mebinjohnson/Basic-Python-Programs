import random

x=int(input("Enter no. of chance's to Guess: "))
compno=random .randint(1,20)
score=x*10

for a in range (x):
    guess=int(input("Enter no. b/w 1-20 to play:"))

    if guess==compno:
        print "\tCorrect Guess"
        break
    else:
        print "\nSorry. Wrong Choice"
        score-=10

else:
    print "Sorry Chance Over." ,'The Number is', compno,"Better Luck NextTime."
    
print score

raw_input()
