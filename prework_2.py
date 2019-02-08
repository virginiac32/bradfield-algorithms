class PythonStack(object):

    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def size(self):
        return len(self._items)

# Reverse a list using a stack
def reverse_list(l):
    stack = PythonStack()
    for x in l:
        stack.push(x)
    reversed_list = []
    while stack.size() > 0:
        reversed_list.append(stack.pop())
    return reversed_list

#test
print(reverse_list([1,2,3,4,5]))


# Implement a queue using stacks
class StackQueue(object):
    def __init__(self):
        self._items = PythonStack()
        self._temp = PythonStack()

    def is_empty(self):
        return self._items.is_empty()

    def enqueue(self, item):
        # adds to the beginning of the queue
        while self._items.size() > 0:
            self._temp.push(self._items.pop())
        self._items.push(item)
        while self._temp.size() > 0:
            self._items.push(self._temp.pop())

    def dequeue(self):
        # remove from end of queue
        return self._items.pop()

    def size(self):
        return self._items.size()

# test
queue = StackQueue()
queue.enqueue("a")
queue.enqueue("b")
queue.enqueue("c")
queue.dequeue()
while queue.size() > 0:
    print(queue.dequeue())
