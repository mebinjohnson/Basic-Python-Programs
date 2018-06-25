def create(dict_list,rollno=None):
    name=raw_input('enter the name ').upper()
    #rollno=int(raw_input('enter the rollno '))
    age=int(raw_input('enter the age '))
    Class=raw_input('enter the class ').upper()
    dict_list[rollno]={'Name':name,'Class':Class,"Age":age}
    print "\n\tData Entered"

def remove(dict_list):
    roll=int(input("Enter  Roll Number to Delete: "))
    try:
        del dict_list[roll]
        "\n\tDeleted Succesfully"
    except KeyError:
        print "\n\tRoll Number Does Not Exist"

def modify(dict_list):
    roll=int(input("Enter Roll Number To Modify: "))
    try:
        dict_list[roll]
        create(dict_list,roll)
    except KeyError:
        print "\n\tRoll Number Does Not Exist"

def viewall(dict_list):
    for x in dict_list:
        print x,
        for y in dict_list[x]:
            print y,':',dict_list[x][y],'\t',
        print

def menu(dict_list):
    menu="""
                ******Student menu******
                    1.Add                
                    2.Remove
                    3.Modify
                    4.Display All
                    5.Quit
                
                ***********************
                """
    print(menu)
    choice=int(raw_input('enter the choice(1-5): '))
    if choice==1:
         rollno=int(raw_input('enter the rollno '))
         create(dict_list,rollno)
    elif choice==2:
        remove(dict_list)
    elif choice==3:
        modify(dict_list)
    elif choice==4:
        viewall(dict_list)
    elif choice==5:
        exit()
    else:
        print('\n\tinvalid choice')
    raw_input()

student_data={}

while True:
              menu(student_data)
              
