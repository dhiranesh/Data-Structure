from colorama import Fore, Style
class node:
    def __init__(self,value):
        self.data = value
        self.next = None
class single_liked_list:
    def __init__(self, value = None):
        self.head = node(value)
        self.tail = self.head
        self.lenght = 0
    # 1St method append method
    def append_list(self, value):
        if(self.head.data == None ):
            self.head.data = value
        elif(self.head.next == None):
            self.temp = node(value)
            self.head.next = self.temp
            self.tail = self.temp
            self.lenght+=1
        else:
            temp = node(value)
            self.tail.next = temp
            self.tail = temp
            self.lenght+=1
    # 2nd method prepend method
    def prepend (self,value):
    
        if(self.head.data == None):
            self.head.data = value
        else:
            temp = node(value)
            temp.next = self.head
            self.head = temp 
            self.lenght+=1
    # 3rd insert method insert at desired postion
    def insert_list(self, position,value):
        if(self.head.data == None):
            self.head.data = value
            return
        if(position > self.lenght or  position >-1):
            print("invalid position!!!")
        
        else:
            newnode = node(value)
            index = 0
            temp = self.head
            while(index < position-1):
                temp = temp.next
                index+=1
            prevnode = temp
            newnode.next = temp.next
            prevnode.next = newnode
            self.lenght+=1
    # 4 Search method for search for element in linked list
    def search_list(self, value):
        count = 0
        temp = self.head
        while(temp.data != value):
            temp = temp.next
            count +=1
        return count
    # 5th get method it return the value of that perticular index
    def get_item(self,index):
        if(index > self.lenght or  index <=-1):
            print("invalid position!!!")
            return
        count = 0
        temp = self.head
        while(count != index):
            temp = temp.next
            count +=1
        return temp.data
    # 6th set method it search for element in perticualr position an upate the data
    def set_item(self,position,item):
        if(position > self.lenght or  position <=-1):
            print("invalid position!!!")
        else:
            temp = self.head
            count = 0 
            for _ in range(position):
                temp = temp.next
            temp.data = item
    # 7th method that print all the value in the linked list
    def __str__(self):
        result = list([])
        temp = self.head
        for i in range(0 , self.lenght+1):
            result.append(str(temp.data))
            temp= temp.next
        return " -> ".join(result)
    # 8th pop method to pop the first element from the list
    def pop_element_first(self,position = None):
        if(self.lenght == 0 or self.head.data == None):
            print(self.head.data)
            self.head.data = None
        if(position == None):
            print(self.head.data)
            self.head = self.head.next
            self.lenght -=1
        else:
            temp = self.head
            for _ in range(0,position-1):
                temp = temp.next
            print(temp.next.data)
            temp.next = temp.next.next
            self.lenght-=1
    def pop_last(self):
        temp = self.head
        if(self.lenght == 0):
            if(self.head.data != None):
                result = self.head.data
                self.head.data = None
                return result
            return None
            return
        for _ in range(self.lenght-1):
            temp = temp.next
        result = temp.next.data
        temp.next = None
        self.lenght-=1
        return result
    def clear_all(self):
        while(self.head.data != None):
            self.pop_last()
         
