class Error(Exception):
    pass
class ValueTooSmallError(Error):
    pass
class ValueTooLargeError(Error):
    pass

number=int(input("Enter Number to Set: "))
while True:
    try:
        i_num=int(input("Enter a Number: "))
        if i_num<number:
            raise ValueTooSmallError
        elif i_num>number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print "This Value Too Small, try again !"
    except ValueTooLargeError:
        print "This Value Is Too Large, try again!"
