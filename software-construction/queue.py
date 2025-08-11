from collections import deque

class Queue:
    """A class representing a queue (FIFO) data structure."""
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self._items.append(item)

    def dequeue(self):
        """Remove and return the front item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._items.popleft()

    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self._items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self._items)

    def __str__(self):
        return f"Queue(front->rear): {list(self._items)}"
