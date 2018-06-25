name=input ('Enter Name of Employee: ')
b=int(input('Enter the Basic of the Employee: '))


if b>=10000:
    da= (b/100)*40
    hr= (b/100)*30

elif b>=5000:
    da= (b/100)*40
    hr= (b/100)*25

elif b>=2000:
    da= (b/100)*40
    hr= (b/100)*30

else:
    da= (b/100)*30
    hr= (b/100)*15

salary= (b+da+hr)

inc= salary*12


if inc>50000:
    x= ((inc/100)*30)/12
else:
    x=0


print ('\nPay Slip \n')
print ( 'The salary of', name,'per month is :' ,'Rs', salary-x , '\nDeduction:',x ,'\nGross:',inc/12)
