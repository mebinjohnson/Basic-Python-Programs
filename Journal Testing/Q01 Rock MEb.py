import random
def number_to_name(number):
  
    if number == 0:
        name = "Rock"
    elif number == 1:
        name = "paper"
    elif number == 2:
        name = "Scissors"
          
    return name

def name_to_number(name):

    if name == "Rock":
        number = 0
    elif name == "Paper":
        number = 1
    elif name == "Scissors":
        number = 2
    else:
         number=-1
    return number    
    

def rpsls(name): 

    comp_number = random.randrange(0,3)
     
    player_number = name_to_number(name)

    comp_move = number_to_name(comp_number)

    print "The Computer chose:",comp_move

    print "Player chose:", name
    


    if (comp_number - player_number) % 3 == 0:
       print "Computer and Player tie!"
    
    elif ( comp_number-player_number ) % 3 == 1: 
        print "Computer wins!"
        print
    
    else:
        print "Player Wins"
        print
        
    
# function calling

rpsls("Rock") 

rpsls("Paper")

rpsls("Scissors")
