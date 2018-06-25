class stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        item=self.items.pop()
        return item
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def isEmpty(self):
        if len(self.items)==0:
            return True
        else:
            return False
    def __str__(self):
        return str(self.items)

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)
    
s=stack()
s.push((45,8,5,9,9,88,9,9,9,946,4654,54,4,654,54))


q=Queue()
q.push((45,8,5,9,9,88,9,9,9,946,4654,54,4,654,54))

print s
print q
