print('Indian Electricity Cooperation\n')

unit=int(input('Enter the Units consumed: '))

if (unit<=100):
    rate= (unit*0.40)

elif (unit<=300):
    rate= 40+((unit-100)*0.50)

elif unit>=300:
    rate= 140+((unit-300)*0.60)


if unit>0:
    print('\n             Your Electricity bill plus meter charge (50 Rs) is : Rs',rate+50)
else:
    print('\nSorry. Their is some Error in your Transaction.')
