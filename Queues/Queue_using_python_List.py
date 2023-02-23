# queue using a python 'List object'

class Queue:
    def __init__(self):
         # Initialize the Queue
        self.items=[]
    
    def size(self):
         # Check the size of the Queue
            return len(self.items)
    
    def enqueue(self, item):
         # Enter item into Queue
            self.items.append(item)

    def dequeue(self):
         # Remove item from the Queue
            if(len(self.items)==0):
                return
            return self.items.pop(0)

# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")