print('                                    Shoppers Centre \n   ')
y=int(input('Enter the  number of products to be purchased: '))

sn=0
price=0

for x in range(0, y):

   code=str(input('\nEnter the code: '))
   
   quan=int(input('Enter Quantity: '))

   rate=float(input('Enter Rate: Rs. '))

   x=(quan*rate)
   price=(x+price)
   sn=(sn+1)

   print('\n',sn,'.','Item Code','        ', 'Quantity', '       ','Rate(Rs)','     ','Price(Rs)')
   print('     ',code,'           ', quan, '                ',rate,'                ',x)
 

print('\nTotal= Rs ', price)


if (price>100) & (price<500):
    print('\n Congatulations you have won a Key Ring')
elif (price>500) & (price<1000):
    print('\n Congatulations you have won a Leather Purse')
elif (price>1000):
    print('\n Congatulations you have won a Pocket Calculator')

print ('\n                  Thank You for shopping with us')



