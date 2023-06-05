
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Stack:
    def __init__(self):
        self.head = None
        
    def push(self, data):
        n = Node(data)
        if self.head == None :
            self.head = n
        else:
            n.next = self.head.next
            self.head.next = n
            
    def pop(self):
        if self.head == None :
            return None
        else:
            temp = self.head
            self.head = self.head.next
            return temp
            
    def print_stack(self):
        temp = self.head
        while(temp != None):
            print (temp.data)
            temp = temp.next
        return    
        
a_stack = Stack()
while True:
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    operation = do[0].strip().lower()
    if operation == 'push':
        a_stack.push(int(do[1]))
    elif operation == 'pop':
        popped = a_stack.pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
            
    elif operation == 'quit':  
        break
    a_stack.print_stack()






















