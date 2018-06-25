string=raw_input('Enter string to reverse:')
new_string=''


for x in range(len(string)):
    
    print string[-(x+1)],'\t',string[x]


