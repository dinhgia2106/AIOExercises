class StackOverflowError(Exception):
    pass


class StackUnderflowError(Exception):
    pass


class QueueOverFlow(Exception):
    pass


class QueueUnderFlow(Exception):
    pass


class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def push(self, value):
        if self.is_full():
            raise StackOverflowError('Stack Overflow')
        self.__stack.append(value)

    def pop(self):
        if self.is_empty():
            raise StackUnderflowError('Stack Underflow')
        return self.__stack.pop()

    def top(self):
        if self.is_empty():
            return 'Stack is empty'
        return self.__stack[-1]


class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def enqueue(self, value):
        if self.is_fulll():
            raise QueueOverFlow('Queue Overflow')
        self.__queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise StackUnderflowError('Queue Underflow')
        self.__queue.pop()

    def font(self):
        if self.is_empty():
            print('Queue is empty')
            return
        return self.__queue[0]
