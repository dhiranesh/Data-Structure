class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self, size):
        self.root = None
        self.tail = None
        self.max_size = size
        self.current_size = 0

    def enqueue(self, value):
        if self.current_size >= self.max_size:
            print("The Queue is over loaded!!!")
            return
        
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.current_size += 1

    def dequeue(self):
        if self.isEmpty():
            print("The Queue is under flow!!!")
            return None
        
        temp_data = self.root.data
        self.root = self.root.next
        if self.root is None:
            self.tail = None
        self.current_size -= 1
        return temp_data

    def isEmpty(self):
        return self.current_size == 0

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.root.data

my_queue = Queue(size=10)
print(f"Is queue empty? {my_queue.isEmpty()}")

for i in range(1, 6):
    my_queue.enqueue(i)

print(f"Is queue empty? {my_queue.isEmpty()}")
print(f"Peek: {my_queue.peek()}")

for i in range(1, 6):
    print(f"Dequeued: {my_queue.dequeue()}")

print(f"Is queue empty? {my_queue.isEmpty()}")
print(f"Peek after dequeue: {my_queue.peek()}")
