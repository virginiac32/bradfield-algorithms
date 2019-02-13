class PythonListQueue(object):
    """
    A queue based on the built in Python list type.
    """

    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop(0)

    def size(self):
        return len(self._items)

    def is_empty(self):
        return len(self._items) == 0


class LinkedListNode(object):
    """
    A doubly linked list node, support for the LinkedListQueue. You should not need
    to change this code, but you will want to use it in the LinkedListQueue
    """

    def __init__(self, value, prevNode, nextNode):
        self.value = value
        self.prev = prevNode
        self.next = nextNode


class LinkedListQueue(object):
    """
    Finish the functions below to create a queue based on a linked list. Because
    a queue must either:

        *** enqueue to the head and dequeue from the tail; or
        * enqueue to the tail and dequeue from the head.

    You should use a doubly linked list to ensure O(1) time enqueue and dequeue.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.total = 0

    def enqueue(self, item):
        temp = LinkedListNode(item, None, self.head)
        if self.is_empty():
            self.head = temp
            self.tail = temp
        else:
            self.head.prev = temp
            self.head = temp
        self.total += 1

    def dequeue(self):
        last_node = self.tail
        if self.size() == 1:
            self.head = None
            self.tail = None
        else:
            previous_node = self.tail.prev
            previous_node.next = None
            self.tail = previous_node
        self.total -= 1
        return last_node.value

    def size(self):
        return self.total

    def is_empty(self):
        return self.head is None


class RingBufferQueue(object):
    """
    Finish the functions below such that this queue is backed by a Ring Buffer.
    Recall that a ring buffer uses an array and two pointers to keep track of
    where to read, and where to write.

    Be careful! If the read pointer were to overtake the write pointer, it
    would return incorrect data! If the write pointer were to overtake the read
    pointer, it would overwrite data that hasn't been read yet!

    In many contexts, you would avoid this issue by stalling when one pointer
    would overwrite the other. Since doing so only makes sense in a multithreaded
    environment, you may prefer to just resize the underlying ring buffer at
    these times, instead.
    """

    def __init__(self):
        self.array = [None] * 100
        # store the read position and the write position
        self.read = 0
        self.write = 0

    def enqueue(self, item):
        self.array[self.write] = item
        if self.write == len(self.array) - 1:
            self.write = 0
        else:
            self.write = self.write + 1
        if self.read == self.write:
            self.expand()

    def dequeue(self):
        value = self.array[self.read]
        if self.read == len(self.array) - 1:
            self.read = 0
        else:
            self.read += 1
        return value

    def size(self):
        if self.is_empty():
            return 0
        elif self.read < self.write:
            return self.write - self.read
        else:
            return len(self.array) - self.read + self.write

    def is_empty(self):
        return self.read == self.write

    def expand(self):
        # double the size of the array
        old_size = len(self.array)
        new_array = [None] * (old_size * 2)
        read_pos = self.read
        for x in range(old_size):
            new_array[x] = self.array[read_pos]
            if read_pos == old_size - 1:
                read_pos = 0
            else:
                read_pos += 1
        self.read = 0
        self.write = old_size
        self.array = new_array

QUEUE_CLASSES = (
    PythonListQueue,
    LinkedListQueue,
    RingBufferQueue,
)
