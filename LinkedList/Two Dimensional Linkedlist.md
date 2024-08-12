---
tags:
  - LinkedList
solved: false
date: 2024-08-11T01:46
---
## Description
A **Doubly Linked List (DLL)** is a linear, dynamic, and ordered data structure. It consists of a sequence of elements, where each element (commonly called a node) contains a reference (or link) to both the next node and the previous node in the sequence. This bi-directional linking allows for more flexible navigation, making operations such as insertions and deletions more efficient, especially when the position of the node to be modified is known.

## Characteristics
- **Type:** #Linear
- **Dynamic/Static:** #Dynamic
- **Ordered/Unordered:** #Ordered

## Operations
### Basic Operations
- **Insert:** The insert operation in a doubly linked list can occur at the beginning (head), at the end (tail), or at any given position. When inserting, a new node is created, and its `next` and `prev` references are adjusted to maintain the bidirectional links in the list.
```python 
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
```
- **Delete:** The delete operation removes a node from the doubly linked list. The references in both the previous and next nodes are updated to bypass the deleted node, maintaining the list's integrity.
```python
    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            if self.head:
                self.head.prev = None
            return
        while current and current.data != key:
            current = current.next
        if current is None:
            return
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next
```
- **Search:** The search operation traverses the doubly linked list from the head to the end, comparing each node's data with the target value. The search is linear, with a time complexity of O(n).
```python
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
```
- **Update:** The update operation involves first searching for the node containing the target value, then modifying the data within that node.
```python
    def update(self, old_key, new_data):
        current = self.head
        while current:
            if current.data == old_key:
                current.data = new_data
                return True
            current = current.next
        return False
```

### Advanced Operations
- **Reverse:** Reversing a doubly linked list involves changing the direction of the `next` and `prev` links so that the last node becomes the first, and the first becomes the last.
```python
    def reverse(self):
        current = self.head
        temp = None
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev
```
- **Traverse Backwards:** Unlike a singly linked list, a doubly linked list can be traversed in both directions, forward and backward.
```python
    def traverse_backward(self):
        current = self.head
        while current and current.next:
            current = current.next
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")
```

## Example
- **Input:** A doubly linked list with elements `[1, 2, 3, 4]`.
- **Output:** After inserting `5` at the end, the doubly linked list becomes `[1, 2, 3, 4, 5]`.

## Implementation
### Language: Python
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete(self, key):
        current = self.head

        # If the node to be deleted is the head
        if current and current.data == key:
            self.head = current.next
            if self.head:
                self.head.prev = None
            return

        # Search for the node to be deleted
        while current and current.data != key:
            current = current.next

        # If the key was not present in the list
        if not current:
            return

        # Unlink the node from the doubly linked list
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def update(self, old_key, new_data):
        current = self.head
        while current:
            if current.data == old_key:
                current.data = new_data
                return True
            current = current.next
        return False

    def reverse(self):
        current = self.head
        temp = None
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev

    def traverse_backward(self):
        current = self.head
        while current and current.next:
            current = current.next
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")

# Example usage:
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert(1)
    dll.insert(2)
    dll.insert(3)
    dll.insert(4)
    print("Original List:")
    current = dll.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    dll.reverse()
    print("Reversed List:")
    current = dll.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    dll.traverse_backward()
```

## Complexity Analysis
### Time Complexity
- **Insert:** O(1) for insertion at the head; O(n) for insertion at the end or at a specific position.
- **Delete:** O(1) for deleting the head node; O(n) for deleting any other node.
- **Search:** O(n) as it requires traversing the list.
- **Update:** O(n) due to the need to search for the node.
- **Traverse Backwards:** O(n) as it requires traversing the list.

### Space Complexity
- **Space Complexity:** O(n), where n is the number of nodes in the doubly linked list.

## Use Cases
- **Navigating browser history (backward and forward navigation)**
- **Implementing undo and redo functionalities**
- **Managing playlist songs in music players**
- **Storing and manipulating large datasets with frequent insertions and deletions**

## Related Questions
- [Reverse a Doubly Linked List](#)
- [Delete a Node in a Doubly Linked List](#)
- [Merge Two Doubly Linked Lists](#)

## References
- [Doubly Linked List Wikipedia](https://en.wikipedia.org/wiki/Doubly_linked_list)
- [Data Structures: Doubly Linked List (GeeksforGeeks)](https://www.geeksforgeeks.org/doubly-linked-list/)

---

## Metadata
```dataview
table
    DataStructureName as "Data Structure Name",
    Complexity as "Time Complexity"
where contains(file.name, "Data Structure")
sort file.ctime desc
```

**Tags:** #DoublyLinkedList #DataStructure #TechPlacements #DSA

