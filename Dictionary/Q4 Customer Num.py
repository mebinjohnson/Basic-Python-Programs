#Customers List

customer_dict={}

n=int(input("Enter the No. of the Customers: "))

for x in range(n):

    num=raw_input("Enter Customer No. : ")
    customer=raw_input("Enter Name of Customer : ")
    customer_dict[num]=customer

print customer_dict


no_del=raw_input("Enter Cutomer No. To delete: ")

del customer_dict[no_del]


print customer_dict
