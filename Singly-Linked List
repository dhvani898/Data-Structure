class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.val = data
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        """
        if list node is empty
        """
        if self.head == None:
            self.head =  ListNode(data)
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next =  ListNode(data)
    
    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        temp = self.head
        while(temp!=None):
            if(temp.val == key):
                return temp.val
            temp = temp.next
        return None
            
    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        """
        temp = self.head
        if(temp.val == key):
            head = temp.next
            return
            
        while (temp.next != None):
            if(temp.next.val == key):
                temp.next = temp.next.next
                return 
            temp = temp.next
        return
    
    def print_list(self):
        temp = self.head
        while(temp != None):
            print (temp.val,end ='')
            temp = temp.next
        return    
    
SLL = SinglyLinkedList()
SLL.append(3)
SLL.append(4)
SLL.append(5)
SLL.append(2)
SLL.print_list()
print(SLL.find(3))
SLL.remove(2)
print(SLL.find(2))
SLL.print_list()
    
    
                
    
        
        
        
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
