# implement a queue by using an array. 

# ## Functionality
# 
# Once implemented, our queue will need to have the following functionality:
# 1. `enqueue`  - adds data to the back of the queue
# 2. `dequeue`  - removes data from the front of the queue
# 3. `front`    - returns the element at the front of the queue
# 4. `size`     - returns the number of elements present in the queue
# 5. `is_empty` - returns `True` if there are no elements in the queue, and `False` otherwise
# 6. `_handle_full_capacity` - increases the capacity of the array, for cases in which the queue would otherwise overflow
# 
# Also, if the queue is empty, `dequeue` and `front` operations should return `None`.

class Queue:

    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0

    def enqueue(self, value):
        # TODO: Check if the queue is full; if it is, call the _handle_queue_capacity_full method
        if(self.next_index==len(self.arr)):
            self._handle_queue_capacity_full

        # enqueue new element
        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index = (self.next_index + 1)
        if self.front_index == -1:
            self.front_index = 0

    def dequeue(self):
        # check if queue is empty
        if self.is_empty():
            self.front_index = -1   # resetting pointers
            self.next_index = 0
            return None

        # dequeue front element
        value = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) 
        self.queue_size -= 1
        return value 

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.size() == 0
    
    def front(self):
        # check if queue is empty
        if self.is_empty():
            return None
        return self.arr[self.front_index]

    # TODO: Add the _handle_queue_capacity_full method
    def _handle_queue_capacity_full(self):
        old_arr=[self.arr[i] for i in range(self.front_index,self.next_index)]
        self.arr=[0 for _ in range(len(self.arr)+10)]
        self.next_index=len(old_arr)
        for i in range(len(old_arr)):
            self.arr[i]=old_arr[i]
            
        self.front_index=0


# ### Test your queue


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

