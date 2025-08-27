class Stack:
    def __init__(self):
        self.list = []

    def push(self, val):
        self.list.append(val)

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[-1]


my_stack = Stack()
my_stack.push(12)
my_stack.push(22)
my_stack.push(32)
my_stack.push(42)

print(my_stack.peek())
print(my_stack.pop())
print(my_stack.peek())
print(my_stack.pop())
print(my_stack.peek())
