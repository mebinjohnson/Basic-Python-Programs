ctr ,Total,Per,Grd=1,0,0,""
Grade=""
lst=[]
t=()
def Cal_Grade(Per):
              Grd=""
              if Per > 91 : Grd = "A1" 

              elif Per > 81 and Per <= 90: Grd = "A2" 

              elif Per > 71 and Per <= 80: Grd = "B1" 

              elif Per > 61 and Per <= 70: Grd = "B2" 

              elif Per > 51 and Per <= 60: Grd = "C1" 

              elif Per > 41 and Per <= 50: Grd = "C2" 

              elif Per > 33 and Per <= 40:
                            Grd = "D"

              return Grd

              

print ("Student  List....")
print
print ("-" * 110)

print "Name                 ", "Subject 1", " Subject 2", " Subject 3", " Subject 4 ", "  Subject 5 ","  Total ", "Percentage ", " Grade"

print ("-" * 110)
#	Entering 10 best students information
while ctr <= 2 : 
              print
              Name = raw_input("Enter Name: ")
              Name = Name.upper() 
              Sub1 = float(input("Enter first subject marks: "))
              Sub2 = float(input("Enter second subject marks: "))
              Sub3 = float(input("Enter third subject marks: "))
              Sub4 = float(input("Enter fourth subject marks: "))
              Sub5 = float(input("Enter fifth subject marks: ")) 
              Total=Sub1+Sub2+Sub3+Sub4+Sub5
              Per=Total/5
              Grade=Cal_Grade(Per)
              ctr += 1
              t=(Name,Sub1,Sub2,Sub3,Sub4,Sub5,Total,Per,Grade)               
              lst.append(t)
              


print "Name                 ", "Subject 1", " Subject 2", " Subject 3", " Subject 4 ", "  Subject 5 ","  Total ", "Percentage ", " Grade"

for i in lst:
              Name,Sub1,Sub2,Sub3,Sub4,Sub5,Total,Per,Grade=i

              print Name+"         ", str(Sub1)  +"     " , str(Sub2)+"    ",  str(Sub3)  +"  ", str(Sub4 )+"   ",  str(Sub5 )+ "  " , str(Total )  +"   ", str(Per )+"  " + str(Grade)

              

print ("-" * 110)
