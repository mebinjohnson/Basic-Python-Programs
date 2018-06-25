ans=int(raw_input ("do you want to play? y=1 nad n=0: "))
n=11
if ans==1:
        while n > 0:
                for x in range(20):
                        #import subprocess as sp
                        #sp.call('cls',shell=True)
                        prit='              '*25+str(n)+"\n"
                        print prit
                n-=1
        print('Blastoff')
        from PIL import Image
        myimage = Image.open("disclaimer.png")
        myimage.load()
      

else:
    print('You should have played :( ')
input()
