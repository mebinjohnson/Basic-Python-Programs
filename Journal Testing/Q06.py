#	Calculating total, percentage and grade 

def Cal_Grade(Per): 
              Grd = "" 

              if Per > 91 :
                  Grd = "A1" 

              elif Per > 81 and Per <= 90:
                  Grd = "A2" 

              elif Per > 71 and Per <= 80:
                  Grd = "B1" 

              elif Per > 61 and Per <= 70:
                  Grd = "B2"

              elif Per > 51 and Per <= 60:
                  Grd = "C1" 

              elif Per > 41 and Per <= 50:
                  Grd = "C2" 

              elif Per > 33 and Per <= 40:
                  Grd = "D"
                #return Grd
              
print

print ("StudentList....")
print


ctr ,Total,Per,Grade=1,0,0,""

#	Entering 10 best students information
while ctr <2 : 

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
              Cal_Grade(Per)
              ctr += 1 

print ("-" * 110)

print ("{0:<13} {1:>12} {2:>12} {3:>12} {4:>12} {5:>12} {6:>8} {7:>12} {8:^10}".format("Name", "Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5","Total", "Percentage", "Grade"))

print ("-" * 110)

print ("{0:<13} {1:>12} {2:>12} {3:>12} {4:>12} {5:>12} {6:>8} {7:>12.2f} {8:^10}".format(Name, Sub1, Sub2, Sub3, Sub4, Sub5, Total, Per, Grade))

print ("-" * 110)
