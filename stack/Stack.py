import linked_list as list

class Stack:
    def __init__(self):
        self.linked_stack = list.single_linked_list()
        self.length = None
        self.top = -1
    
    def set_max_size(self, length):
        self.length = length
    def push_stack(self, value):
        if self.length is not None and self.top >= self.length - 1:
            print("Stack is overflow!!!!")
        else:
            self.linked_stack.append_list(value)
            self.top += 1

    def pop_stack(self):
        if self.top == -1:
            print("Stack is underflow")
            return None
        else:
            result = self.linked_stack.pop_last()
            self.top -= 1
            return result
    def peek_stack(self):
        if self.top == -1:
            return None
        else:
            return self.linked_stack.get_item(self.top)
    def isempty_stack(self):
        return self.top == -1
    def clear_stack(self):
        self.linked_stack.clear_all()
        self.top = -1
    
    def __str__(self):
        return str(self.linked_stack)
