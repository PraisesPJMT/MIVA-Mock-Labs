class Node:
    """A node class for singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """A class representing a singly linked list."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Append a new node with data to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def prepend(self, data):
        """Add a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self, data):
        """Delete the first node with the specified data."""
        if self.head is None:
            return False
        if self.head.data == data:
            self.head = self.head.next
            return True
        curr = self.head
        while curr.next and curr.next.data != data:
            curr = curr.next
        if curr.next is None:
            return False
        curr.next = curr.next.next
        return True

    def find(self, data):
        """Return True if data is found in the list, False otherwise."""
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    def to_list(self):
        """Return the list elements as a Python list."""
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.data)
            curr = curr.next
        return elements

    def __str__(self):
        return " -> ".join(str(data) for data in self.to_list()) or "Empty List"
