class Stack:
    """A class representing a stack (LIFO) data structure."""
    def __init__(self):
        self._items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the top item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self._items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self._items)

    def __str__(self):
        return f"Stack(top->bottom): {list(reversed(self._items))}"
