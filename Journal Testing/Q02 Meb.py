import random

secretnum= random.randint(1,100)  # generates random number

#print(secretnum)
guessnum=int(input("Enter the number between 1 to 100:"))


while guessnum!=secretnum :

       if(guessnum <secretnum) :
                     
                     print "your guess is too low "
       else:
                      print "your guess is too high "

       guessnum=int(input("Enter the number :"))
       


print("Congrats: You Found the Number")         
