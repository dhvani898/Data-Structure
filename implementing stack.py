class myStack:
 
     def __init__(self):
        self.s = []
         
     def isEmpty(self):
        if len(self.s)==0:
            return True
        else:
            return False
        
     def push(self, item):
        self.s.append(item)
         
     def pop(self):
        return self.s.pop()
        
     def peek(self):
        return self.s[-1]
        
     def size(self):
        return len(self.s)
         
     def show(self):
            print(self.s)

s = myStack()
print(s.isEmpty())
s.push('1')
s.push('2')
s.push('3')
s.push('4')
s.push('5')
print(s.isEmpty())
print(s.peek())
print(s.pop())
s.show()
