try:
  x=int(raw_input("Enter Number: "))
  result=3.0/x

except ZeroDivisionError:
  print " Infinty"
except ValueError:
  print "Invalid Input"
else:
  print result
finally:
  print 'Executing the Final Class'

print 'Tested'
