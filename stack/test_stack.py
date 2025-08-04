from Stack import Stack

# Test the stack implementation
def test_stack():
    print("Testing Stack Implementation")
    print("=" * 30)
    
    # Create a new stack
    stack = Stack()
    stack.set_max_size(5)  # Set maximum size to 5
    
    print("1. Testing push operations:")
    stack.push_stack(10)
    stack.push_stack(20)
    stack.push_stack(30)
    print(f"Stack contents: {stack}")
    
    print("\n2. Testing peek operation:")
    top_element = stack.peek_stack()
    print(f"Top element: {top_element}")
    
    print("\n3. Testing pop operation:")
    popped = stack.pop_stack()
    print(f"Popped element: {popped}")
    print(f"Stack after pop: {stack}")
    
    print("\n4. Testing empty check:")
    print(f"Is stack empty? {stack.isempty_stack()}")
    
    print("\n5. Testing overflow (adding more than max size):")
    for i in range(10):
        stack.push_stack(i * 10)
    
    print("\n6. Testing underflow (popping from empty stack):")
    stack.clear_stack()
    print(f"Is stack empty after clear? {stack.isempty_stack()}")
    result = stack.pop_stack()
    print(f"Pop from empty stack result: {result}")

if __name__ == "__main__":
    test_stack()
