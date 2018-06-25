def main():
    import math
    r = float(raw_input('enter any radius : '))
    a = math.pi * math.pow(r,2)
    print ' Area = ' , a
main()


x = 3
x+= x-x
print x

class person:
    
        def __init__(self,id):
            self.id = id
arjun = person(150)
arjun.__dict__['age'] = 50
print arjun.age + len(arjun.__dict__) 


def main():
    import random
    p = 'MY PROGRAM'
    i = 0
    while p[i] != 'R':
          l = random.randint(0,3) + 5
          print p[l],'-',
          i += 1
while True:
    main()
    print
