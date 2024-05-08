class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.Q = [0] * max_size
        self.num = 0
        self.first = 0

    def enqueue(self, item):
        if self.num >= self.max_size:
            raise Exception("Queue overflow")
        self.Q[(self.num + self.first) % self.max_size] = item
        self.num += 1

    def dequeue(self):
        if self.num == 0:
            raise Exception("Queue empty")
        item = self.Q[self.first]
        self.first = (self.first + 1) % self.max_size
        self.num -= 1
        return item

    def front(self):
        if self.num == 0:
            raise Exception("Queue empty")
        return self.Q[self.first]

    def is_empty(self):
        return self.num == 0

    def size(self):
        return self.num

    def is_full(self):
        return self.num >= self.max_size

    def get_element_at(self, index):
        if index < 0 or index >= self.num:
            raise Exception("Index out of bounds")
        return self.Q[(self.first + index) % self.max_size]

# Example usage
q = Queue(10)
q.enqueue("ra'na")
q.enqueue("vez")
q.enqueue("Arya")
print("queue size is: ", q.size())

print(q.dequeue(), "left the queue")
print("front of queue is:", q.front())

q.enqueue("milda")
print("Element at index 1:", q.get_element_at(1))  # Assuming "Arya" is at index 1 after one dequeue

q.dequeue()  # Dequeue "vez"
q.dequeue()  # Dequeue "Arya"
q.dequeue()  # Dequeue "milda"
print("It was a queue")
