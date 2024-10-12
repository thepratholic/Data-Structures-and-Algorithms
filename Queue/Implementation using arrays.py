class Queue:
    def __init__(self, c):
        self.queue = []
        self.front = 0
        self.rear = 0
        self.capacity = c

    # Function to insert an element at the rear of the queue
    def queueEnqueue(self, data):
        # Check queue is full or not
        if self.rear == self.capacity:
            print("\nQueue is full")
        else:
            self.queue.append(data)
            self.rear += 1

    # Function to delete an element from the front of the queue
    def queueDequeue(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            self.front += 1

    # Function to print queue elements
    def queueDisplay(self):
        if self.front == self.rear:
            print("\nQueue is Empty")
        else:
            # Traverse from front to rear to print elements
            for i in range(self.front, self.rear):
                print(self.queue[i], end=' ')

    # Print front of queue
    def queueFront(self):
        if self.front == self.rear:
            print("\nQueue is Empty")
        else:
            print("\nFront Element is:", self.queue[self.front])

    def queueRear(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            print(self.queue[self.rear-1])

q = Queue(4)

# Print queue elements
q.queueDisplay()
q.queueEnqueue(20)
q.queueEnqueue(30)
q.queueEnqueue(40)
q.queueEnqueue(50)

# Print queue elements
q.queueDisplay()


q.queueDequeue()
q.queueDequeue()

# Print front of queue
q.queueFront()
q.queueRear()