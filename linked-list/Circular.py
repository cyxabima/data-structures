class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Circular:
    def __init__(self):
        self.head = None

    def insert(self, val, index):
        new_node = Node(val)
        last = self._get_last()

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            if last is None:  # new node is being inserted list was empty
                self.head.next = self.head
            else:
                last.next = self.head

            return

        if self.head is None and index > 0:
            raise Exception("Can't insert other than zero index in empty list")

        temp = self.head
        prev = None
        counter = 0
        while temp is not None and counter < index:  # btw temp will never be none
            prev = temp
            temp = temp.next
            counter += 1

        prev.next = new_node
        new_node.next = temp

    def remove(self, val):
        if self.head is None:
            return

        last = self._get_last()
        temp = self.head
        # Case 1: at index zero
        if temp.val == val:

            # meaning there is only one Node and we are removing it
            if last == self.head:
                self.head = None
            else:
                self.head = temp.next
                last.next = self.head
            return

        # Case 2 at any index other than zero
        # no need to circular loop
        prev = temp  # as we are breaking before making a temp
        temp = temp.next  # as if we use only self.head the loop will never execute
        while temp != self.head:
            if temp.val == val:
                break
                # we can also do prev.next = temp.next here and then return instead of break

            prev = temp
            temp = temp.next

        if temp == self.head:
            return  # meaning val not found

        # prev and temp both will be node at this point as loop will always executed
        prev.next = temp.next

    def _get_last(self):
        # case 1: No element in the list
        if self.head is None:
            return

        # case 2 and case 3
        # if at least one node then it must have a next
        # case 2 is that if head.next is pointing to it self meaning list has only one node
        # case 3 is that if head.next is not pointing to it self
        # then we have to traverse the list till the last node points to head
        last = self.head
        # there was error in while condition i am checking the last of next otherwise last contain 1st node
        while last.next != self.head:
            last = last.next
        return last

    def __str__(self):
        repr_str = "["
        temp = self.head
        while temp is not None:
            repr_str += str(temp.val) + ","
            temp = temp.next
            if temp == self.head:
                break

        repr_str = repr_str.rstrip(",") + "]"
        return repr_str

    def __len__(self):
        if self.head is None:
            return 0

        temp = self.head.next  # as we are sure that al least one Node is there
        if temp == self.head:
            return 1

        counter = 1
        while temp != self.head:
            temp = temp.next
            counter += 1

        return counter

    # def __str__(self):
    #     if self.head is None:
    #         return "[]"

    #     result = [str(self.head.val)]
    #     temp = self.head.next
    #     while temp != self.head:
    #         result.append(str(temp.val))
    #         temp = temp.next

    #     return "[" + ", ".join(result) + "]"


r = Circular()
r.insert(0, 0)
r.insert(0, 1)
r.insert(1, 2)
r.insert(3, 3)
r.insert(2, 4)
r.insert(8, 5)
r.insert(0, 0)
r.remove(0)
r.remove(0)
r.remove(8)
print(r)
print(len(r))
print(r._get_last().val)
