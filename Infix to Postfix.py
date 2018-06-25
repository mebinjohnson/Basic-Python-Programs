#()^/*+-
class stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        item=self.items.pop()
        return item

#Input=raw_input("Input Expression:\t").upper()
Input='a+b^*d-+e/f+a*d'.upper()
Input='A+B*C'.upper()
Output=[]
tem_input=[]
for chra in Input:
    tem_input+=chra
Input=tem_input
print Input

s=stack()

for x in Input:
    print x,'\t\t\tOutput : ',Output
    print '\t\t\t\t\t       Stack : ',s.items
    if x.isalpha():
        Output.append(x)
    else:
        s.push(x)
        if len(s.items)>=2:
            print 'Cond',s.items[:len(s.items)-2]
            if s.items[len(s.items)-2] in ['+','*','/','-'] and x=='^':
                print '1'
                for m in range(len(s.items)):
                    Output+=s.pop()
            elif s.items[len(s.items)-2] in ['+','*','-'] and x=='/':
                print '2'
                for m in range(len(s.items)):
                    Output+=s.pop()
            elif s.items[len(s.items)-2] in ['+','-'] and x=='*':
                for m in range(len(s.items)):
                    Output+=s.pop()
            elif s.items[len(s.items)-2]in ['-'] and x=='+':
                for m in range(len(s.items)):
                    Output+=s.pop()
            else:
                for m in range(len(s.items)):
                    Output+=s.pop()
if len(s.items)!=0:
    for m in range(len(s.items)):
                    Output+=s.pop() 
            
print
print s.items
print 'Ans;        a b ^ d * + - e f / + a d * +'
for x in Output:
    print x,
        


