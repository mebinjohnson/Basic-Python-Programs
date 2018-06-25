import sys
 
username= raw_input('Username for this program : ')
 
if username == '23':
    print "Welcome user #23"
else:
    print 'I am sorry you are not the user of this program.'
    exit()
 
password = raw_input('Password : ')
 
if password == 'rosebud':
    print "User authenticated"
else:
    print 'Incorrect password'
    exit()
