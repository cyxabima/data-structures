# singly-linked-list


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f"{self.val}"


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)

        # Case 1 no node
        if self.head is None:
            self.head = new_node
            return

        # Case 2 at least one node
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        # now temp is pointing to the last node of the list
        temp.next = new_node

    def pop(self):

        if self.head is None:
            raise Exception("Can't pop from empty List")

        temp = self.head
        prev = None
        # case 1 exactly one node
        if self.head.next is None:
            self.head = None
            return temp.val

        # case 2 more than one node
        while temp.next is not None:
            prev = temp
            temp = temp.next

        prev.next = None
        return temp.val

    def insert(self, val, index=0):

        new_node = Node(val)

        # case 1 insertion at index zero
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # case 2
        temp = self.head
        prev = None
        counter = 0
        while counter < index and temp is not None:
            prev = temp
            temp = temp.next
            counter += 1

        prev.next = new_node
        new_node.next = temp

    def remove(self, val):

        if self.head is None:
            raise Exception("can't remove from empty list")

        # case 1 val is at head
        if self.head.val == val:
            self.head = self.head.next
            return

        # case 2
        temp = self.head
        prev = None
        while temp is not None:
            if temp.val == val:
                break
            prev = temp
            temp = temp.next
        else:
            return  # this return is used if no val found then loop with exit with break and you know it

        prev.next = temp.next

    def __str__(self):
        temp = self.head
        rep_str = "["

        while temp is not None:
            rep_str += str(temp.val) + ", "
            temp = temp.next

        rep_str = rep_str.rstrip(", ") + "]"
        return rep_str


l = LinkedList()
l.push(1)
l.push(2)
l.push(3)
l.remove(3)
print(l)
