import math

while (True):
    print

    print ("M A I N M E N U")

    print ("- - - - - - - - - - -") 

    print ("1. Palindrome Number") 

    print ("2. Armstrong number") 

    print ("3. Prime number")

    print ("4. Quit")

    print ("- - - - - - - - - - -")

    Opt = int(input( "Enter your option: "))
    print
    

    if (Opt == 1) :
        N = int(input("Enter a number to check special number: "))
        N1 = N

        Rem = Rev = 0 

        while (N1 > 0):
            Rem = N1 % 10

            Rev=Rev*10+Rem;

            N1 = N1 // 10 #Floor division 

        if (N == Rev):

            print ("It is a Palindrome Number.")
        else:

            print ("It is not Palindrome Number.")
        raw_input()

    elif (Opt == 2) :
        N = int(input("Enter a number to check armstrong number: "))
        N1 = N
        Rem = Sum = 0
        while (N1 > 0):
            Rem = N1 % 10

            N1 = N1 // 10 #Floor division 

            Sum = Sum + math.pow(Rem, 3)

        if (N == Sum):

                print ("It is an armstrong number.")
        else:

                print ("It is not an armstrong number.")
        raw_input()

    elif (Opt == 3) :
        Opt = 0

        N = int(input("Enter a number to check prime number: "))
        for i in range(2, N):
            if (N % i == 0):
                Opt = 1
                break

        if (Opt == 1):
            print ("It is not a Prime number")
        else:
            print ("It is a prime number.")
        raw_input()
    elif (Opt==4):
        exit()
