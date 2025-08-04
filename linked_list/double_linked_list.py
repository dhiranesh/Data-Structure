from colorama import Fore, Style
class node:
    data = 0
    next = None
    prev = None
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class method:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0
    def append_list(self,value):
        if(self.head == None):
            self.head = node(value)
            self.tail = self.head
        else:
            newnode = node(value)
            self.tail.next = newnode
            self.head.prev = newnode
            self.tail = newnode
        self.lenght += 1
    def prepend(self, value):
        if(self.head == None):
            self.head = node(value)
            self.tail = self.head
        else:
            newnode = node(value)
            self.head.prev = newnode
            newnode.next = self.head
            
            self.head = newnode
        self.lenght +=1
    def insert_list(self,position,value):
        if(position >= -1 and position <self.lenght):
            print ("Invalid position!!!")
            return
        if position == 0:
            return self.prepend(value)
        if position == self.lenght:
            return self.append_list(value)
        
        newnode = node(value)
        temp = self.head
        for _ in range(position):
            temp = temp.next
        newnode = temp.next
        temp.prev.next = newnode
        self.lenght +=1
    def get_item(self,position):
        if(position >= -1 and position <self.lenght):
            print ("Invalid position!!!")
            return
        else:
            temp = self.head
            count = 0 
            for _ in range(position):
                temp = temp.next
            return temp.data
    def pop_first(self):
        if(self.head == None):
            return "List is under flow"
        else:
            data = self.head.data
            self.head,temp = None,self.head.next
            self.head = temp
        self.lenght -= 1
        return data
    def pop(self):
         if(self.head == self.tail):
            self.head = None
            self.tail = None
         if(self.tail == None):
            return "List is under flow"
         else:
             data = self.tail.data
             self.tail = self.tail.prev
             self.tail = None
             return data
         self.lenght -=1
    def remove(self,index):
        if(self.head == None):
            return "List is under flow"
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            preitem = temp.prev
            preitem.next = temp.next
    def clear_all(self):
        self.head = None
        self.tail = None
    def __str__(self):
        """
        Return a string representation of the doubly linked list,
        with node values separated by '<->'."""
        result = []
        temp = self.head
        while temp:
            result.append(str(temp.data))
            temp = temp.next
        return "<->".join(result)
a = method()
while(True):
    print(Fore.GREEN+"1St method append method\n2nd method prepend method\n3rd insert method insert at desired postion\n4th Search method for search for element in linked list\n5th get method it return the value of that perticular index\n6th set method it search for element in perticualr position an upate the data\n7th method that print all the value in the linked list \n8th pop method to pop the first element from the list \n9th pop the first element\n10th pop the last element in the list\n11th clear all the elements"+Style.RESET_ALL)
    i = int(input(Fore.RED+"Enter the input:"))
    if(i == 1):
        v = int(input("Enter the value:"))
        a.append_list(v)
    elif(i == 2):
        v = int(input("Enter the value:"))
        a.prepend(v)        
    elif(i == 3):
        p = int(input("Enter the position:"))
        v = int(input("Enter the value:"))
        a.insert_list(p,v)
    # elif(i == 4):
    #     v = int(input("Enter the value:"))
    #     print(a.search_list(v))
    elif(i == 5):
        index = int(input("Enter the value:"))
        print(a.get_item(index))
    # elif(i == 6):
    #     p = int(input("Enter the position:"))
    #     v = int(input("Enter the value:"))
    #     a.set_item(v,p)
    elif(i == 7):
        print(a)
    elif(i == 8):
        a.pop_first(index)
    elif(i == 9):
        print(a.pop())
    # elif(i == 10):
    #     print(a.pop_last())
    elif(i == 11):
        a.clear_all()
    elif(i == 111):
        for i in range(0,20,1):
            a.append_list(i)
    else:
        print(Style.RESET_ALL)
        exit(0)
    print(a)