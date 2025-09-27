class Queue:
    def __init__(self, size=5):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.count = 0  # number of elements

    def _inc_circular(self, val):
        return (val + 1) % self.size

    def enqueue(self, value):
        if self.count == self.size:
            raise IndexError("Queue is full")

        self.queue[self.rear] = value
        self.rear = self._inc_circular(self.rear)
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise IndexError("Queue is empty")

        ret = self.queue[self.front]
        self.queue[self.front] = None  # optional
        self.front = self._inc_circular(self.front)
        self.count -= 1
        return ret

    def __str__(self):
        if self.count == 0:
            return "[]"

        ret = []
        idx = self.front
        for _ in range(self.count):
            ret.append(str(self.queue[idx]))
            idx = self._inc_circular(idx)
        return "[" + ",".join(ret) + "]"
