class Node:
    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None


class Doubly:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next is not None:
            last = last.next

        last.next = new_node
        new_node.prev = last

    def pop(self):
        if self.head is None:
            raise Exception("can't pop from empty list")

        last = self.head
        # case 1 Exactly one Node
        if self.head.next is None:
            self.head = None
            return last.val

        # case 2 More than one Node
        prev = None
        while last.next is not None:
            prev = last
            last = last.next

        # there is prev attribute in last node since we are deleting it through garbage
        # collector so prev will be deleted as node is deleted
        prev.next = None
        # last is a local variable it will automatically popped from the stack
        return last.val

    def insert(self, val, index):
        new_node = Node(val)

        if index == 0:
            new_node.next = self.head
            # so there are two cases in case 1 if head is None or if head is not None
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
            return

        counter = 0
        temp = self.head
        prev = None
        while counter < index and temp is not None:
            prev = temp
            temp = temp.next
            counter += 1

        # so when we are out of either temp is None or temp contain node of required index
        # we have  handle index 0 in above but if list is empty and some one insert at index greater than 0
        # then insertion will be one on zeroth index and btw prev will be None
        # as loop will never executed index == counter
        if prev is not None:
            prev.next = new_node  # meaning we are not inserted in 0 th index
        else:
            self.head = new_node  # if we are inserting in index 0 then head must be set

        new_node.prev = prev
        new_node.next = temp
        if temp is not None:
            temp.prev = new_node

    def __str__(self):
        temp = self.head
        rep_str = "["

        while temp is not None:
            rep_str += str(temp.val) + ", "
            temp = temp.next

        rep_str = rep_str.rstrip(", ") + "]"
        return rep_str

    def __len__(self):
        temp = self.head
        counter = 0
        while temp is not None:
            counter += 1
            temp = temp.next
        return counter


d = Doubly()
# d.push(1)
# d.push(2)
# d.push(3)
# d.push(4)
# d.push(5)
# d.push(6)
# print(d.pop())
# print(d.pop())
# print(d.pop())
# print(d.pop())
# print(d.pop())
# print(d.pop())
d.insert(23, 122)
print(d)
print(len(d))
