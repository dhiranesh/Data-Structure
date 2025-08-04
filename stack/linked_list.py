from colorama import Fore, Style

class node:
    def __init__(self, value):
        self.data = value
        self.next = None

class single_linked_list:
    def __init__(self, value=None):
        self.head = node(value)
        self.tail = self.head
        self.length = 0
    # 1st method: append method
    def append_list(self, value):
        if self.head.data is None:
            self.head.data = value
        elif self.head.next is None:
            self.temp = node(value)
            self.head.next = self.temp
            self.tail = self.temp
            self.length += 1
        else:
            temp = node(value)
            self.tail.next = temp
            self.tail = temp
            self.length += 1
    # 2nd method: prepend method
    def prepend(self, value):
        if self.head.data is None:
            self.head.data = value
        else:
            temp = node(value)
            temp.next = self.head
            self.head = temp 
            self.length += 1
    # 3rd method: insert at desired position
    def insert_list(self, position, value):
        if self.head.data is None:
            self.head.data = value
            return
        if position > self.length or position < 0:
            print("invalid position!!!")
        else:
            newnode = node(value)
            index = 0
            temp = self.head
            while index < position - 1:
                temp = temp.next
                index += 1
            prevnode = temp
            newnode.next = temp.next
            prevnode.next = newnode
            self.length += 1
    # 4th method: search for element in linked list
    def search_list(self, value):
        count = 0
        temp = self.head
        while temp.data != value:
            temp = temp.next
            count += 1
        return count
    # 5th method: get value at particular index
    def get_item(self, index):
        if index > self.length or index < 0:
            print("invalid position!!!")
            return
        count = 0
        temp = self.head
        while count != index:
            temp = temp.next
            count += 1
        return temp.data
    # 6th method: set element at particular position and update the data
    def set_item(self, position, item):
        if position > self.length or position < 0:
            print("invalid position!!!")
        else:
            temp = self.head
            for _ in range(position):
                temp = temp.next
            temp.data = item
    # 7th method: print all values in the linked list
    def __str__(self):
        result = []
        temp = self.head
        for i in range(0, self.length + 1):
            result.append(str(temp.data))
            temp = temp.next
        return " -> ".join(result)
    # 8th method: pop element from first or specific position
    def pop_element_first(self, position=None):
        if self.length == 0 or self.head.data is None:
            print(self.head.data)
            self.head.data = None
        if position is None:
            print(self.head.data)
            self.head = self.head.next
            self.length -= 1
        else:
            temp = self.head
            for _ in range(0, position - 1):
                temp = temp.next
            print(temp.next.data)
            temp.next = temp.next.next
            self.length -= 1
    def pop_last(self):
        # If only one element (head contains data, length is 0)
        if self.length == 0:
            if self.head.data is not None:
                result = self.head.data
                self.head.data = None
                return result
            return None
        
        # If only one element in the chain (length is 1, head.next exists)
        if self.length == 1:
            result = self.head.next.data
            self.head.next = None
            self.tail = self.head
            self.length -= 1
            return result
        
        # Multiple elements - traverse to second last
        temp = self.head
        for _ in range(self.length - 1):
            temp = temp.next
        result = temp.next.data
        temp.next = None
        self.tail = temp
        self.length -= 1
        return result
    
    def clear_all(self):
        while self.length > 0:
            self.pop_last()
        self.head.data = None