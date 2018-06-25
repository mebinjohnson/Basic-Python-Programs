matrix1=[]

while True:
    line=raw_input()
    if not line:
        break
    value=line.split()
    values=[[int(value)] for values in value]
    matix1.append(value)

print matrix1
