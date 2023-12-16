# Manually transcribing the text from the image and then implementing the singly linked list in Python.

class Node:
    """A Node class for a singly linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    """A Singly Linked List class with basic operations."""
    def __init__(self):
        self.head = None

    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None

    def append(self, value):
        """Append a node with the given value to the end of the list."""
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def length(self):
        """Return the length of the list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def insert(self, value, position):
        """Insert a node with the given value at the given position."""
        if position == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            count = 0
            while count < position - 1 and current.next:
                current = current.next
                count += 1
            new_node = Node(value)
            new_node.next = current.next
            current.next = new_node

    def delete(self, position):
        """Delete a node at the given position."""
        if position == 0:
            self.head = self.head.next
        else:
            current = self.head
            count = 0
            while count < position - 1 and current.next:
                current = current.next
                count += 1
            if current.next:
                current.next = current.next.next

    def get_value(self, position):
        """Get the value of the node at the given position."""
        current = self.head
        count = 0
        while count < position and current:
            current = current.next
            count += 1
        if current:
            return current.value
        else:
            return None

    def traverse(self):
        """Traverse the list and print the value of each node."""
        current = self.head
        while current:
            print(current.value, end=' ')
            current = current.next
        print()

# Create and test the singly linked list based on the tasks in the image
sll = SinglyLinkedList()
print(sll.is_empty())  # Task 2, should return True

# Task 3, insert multiple nodes
for value in [33, 24, 231, 3, 11]:
    sll.append(value)

print(sll.length())  # Task 4, should return the length of the list

sll.insert(11, 3)  # Task 5, insert 11 at position 3
sll.insert(25, 0)  # Task 6, insert 25 at the start

sll.delete(4)  # Task 7, delete node at position 4
print(sll.get_value(3))  # Task 8, get value at position 3

sll.traverse()  # Task 9, traverse all nodes
