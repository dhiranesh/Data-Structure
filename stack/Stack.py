import linked_list as list

class stack:
    def __init__(self):
        self.linked_stack = list.single_liked_list()
        self.length = None
        self.top = -1
    def Stack(self,length):
        self.length = length
    def push_stack(self,value):
        if(self.top >= self.length -1  ):
            print("Stack is over flow!!!!")
        else:
            self.linked_stack.append_list(value)
            print(self.linked_stack)
            self.top +=1

    def pop_stack (self):
        if(self.top == -1):
            print("Stack is under flow")
        else:
            return self.linked_stack.pop_last()
            top -= 1
    def peek_stack(self):
        if(self.top == -1):
            return None
        else:
            return self.linked_stack.data
    def isempty_stack(self):
        if(self.top == -1):
            return True
        else:
            return False
    def clear_stack(self):
        self.linked_stack.clear_all
    def __str__(self):
        return self.linked_stack
