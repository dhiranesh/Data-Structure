class Node:
    def __init__(self):
        self.data = None
        self.next = None
class Queue:

    def __init__(self,size):
        self.root = Node()
        self.lenght = size
        self.top = 0
        self.tail = self.root
    def enqueue(self, value):
        if(self.root.data == None):
            self.root.data = value
            self.tail.data = value
        elif(self.top == self.lenght):
            print("The Queue is over loaded!!!")
            return
        else:
            new = Node()
            new.data = value
            self.tail.next = new
            self.tail = new
        self.top +=1

    def dequeue(self,value):
        if(self.root == None ):
            print("The Queue is under flow!!!")
        else:
            temp = self.root.data
            self.root = self.root.next
            return temp
my_queue = Queue(size = 10)
for i in range(1,10):
    my_queue.enqueue(i)
for i in range(1,10):
    print(my_queue.dequeue(i))
