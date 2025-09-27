class Stack:
    def __init__(self):
        self.list = []

    def push(self, val):
        self.list.append(val)

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[-1]

    def __len__(self):
        return len(self.list)


# using the concept of stack and utilizing stack operation for bracket matching
def is_bracket_matched(string):
    opening = "{[("
    closing = "}])"
    mapping = dict(zip(opening, closing))
    stack = Stack()

    for char in string:
        # case 1 neither opening nor closing bracket
        if char not in mapping and char not in mapping.values():
            continue

        # case 2
        if char in mapping.keys():
            stack.push(mapping[char])

        # case 3
        elif len(stack) == 0 or char != stack.pop():
            return False

    return len(stack) == 0


print(is_bracket_matched("[{9)}]"))
