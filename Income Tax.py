salary=int(input('Enter your monthly salary: '))


if salary>=9000:
    inctax= (salary/100)*40

elif (salary<=8999) & (salary>=7500):
    inctax= (salary/100)*30

elif salary<=7499:
    inctax= (salary/100)*20


print ('The monthly income tax is : Rs', inctax)  
