class Queue:
    def __init__(self):
        self.size = 5
        self.queue = list(range(0, self.size))
        self.front = 0
        self.rear = 0

        self.is_empty = True
        self.is_full = False

    def _inc_circular(self, val):
        if val + 1 == self.size:
            return 0  # cuz last index + 1 will be index error

        return val + 1

    def enqueue(self, value):
        if self.is_full:
            raise IndexError("Queue is full")

        self.queue[self.rear] = value

        self.rear = self._inc_circular(self.rear)

        self.is_empty = False
        if self.rear == self.front:
            self.is_full = True

    def dequeue(self):
        if self.is_empty:
            raise IndexError("Queue is Empty")

        ret = self.queue[self.front]  # we also set the deleted one to None
        self.front = self._inc_circular(self.front)

        self.is_full = False

        if self.front == self.rear:
            self.is_empty = True

        return ret

    def __str__(self):
        ret = str(self.queue[self.front])
        idx = self.front + 1
        while idx != self.rear:
            ret += "," + str(self.queue[idx])
            idx = self._inc_circular(idx)

        return ret


q = Queue()
q.enqueue(12)
q.enqueue(23)
q.enqueue(22)
q.enqueue(15)
q.enqueue(50)
print(q.dequeue())
print(q)
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())

# BTW this is circular queue.
# cuz there is memory loss in linear queue
#  it is possible the array contains only one value but queue is full as the user has dequeue
# from the front all the other value
# in circular queue we utilize the empty elements and does not declare queue full
# until all the elements are present equal to the size of array

# there is simple queue possible btw if you have used count attribute you can check the empty and full queue easily
