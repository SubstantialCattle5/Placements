---
tags:
  - LinkedList
---

## Description
A **Linked List** is a linear, dynamic, and ordered data structure. It consists of a sequence of elements, where each element (commonly called a node) contains a reference (or link) to the next node in the sequence. Linked Lists are typically used in situations where the size of the data structure is unknown ahead of time or may change dynamically, as they allow for efficient insertions and deletions.

## Characteristics
- **Type:** #Linear
- **Dynamic/Static:** #Dynamic
- **Ordered/Unordered:** #Ordered

## Operations
### Basic Operations
- **Insert**: The insert operation in a linked list can occur at the beginning (head), at the end (tail), or at any given position. When inserting, a new node is created, and its reference (link) is adjusted to point to the appropriate node, ensuring the list remains intact.
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
```
- **Delete:** The delete operation removes a node from the linked list. The reference in the previous node is updated to bypass the deleted node, linking it directly to the next node.
```python
    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
```
- **Search:** The search operation traverses the linked list from the head to the end, comparing each node's data with the target value. The search can be linear, making it an O(n) operation.
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
- **Reverse:** Reversing a linked list involves changing the direction of the links so that the last node becomes the first, and the first becomes the last.
```python
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
```
- **Detect Cycle:** This operation checks whether a linked list contains a cycle (a loop where a node's next reference points to a previous node) using techniques like Floyd's Tortoise and Hare algorithm.
```python
    def detect_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```

## Example
- **Input:** A linked list with elements `[1, 2, 3, 4]`.
- **Output:** After inserting `5` at the end, the linked list becomes `[1, 2, 3, 4, 5]`.

## Implementation
### Language: Python
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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

    def delete(self, key):
        current = self.head

        # If the node to be deleted is the head
        if current and current.data == key:
            self.head = current.next
            return

        # Search for the node to be deleted
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not present in the list
        if not current:
            return

        # Unlink the node from the linked list
        prev.next = current.next

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


    def detect_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    print("Original List:")
    current = ll.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    ll.reverse()
    print("Reversed List:")
    current = ll.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    print("Cycle Detected?" , ll.detect_cycle())
    
    # Creating a cycle for testing
    ll.head.next.next.next = ll.head.next
    print("Cycle Detected?" , ll.detect_cycle())

```

## Complexity Analysis
### Time Complexity
- **Insert:** O(1) for insertion at the head; O(n) for insertion at the end or at a specific position.
- **Delete:** O(1) for deleting the head node; O(n) for deleting any other node.
- **Search:** O(n) as it requires traversing the list.
- **Update:** O(n) due to the need to search for the node.

### Space Complexity
- **Space Complexity:** O(n), where n is the number of nodes in the linked list.

## Use Cases
- **Implementation of Stacks and Queues**
- **Handling of real-time data streams**
- **Dynamic memory allocation**
- **Graph adjacency list representation**

## Related Questions
- [Reverse a Linked List](#)
- [Detect Cycle in a Linked List](#)
- [Merge Two Sorted Linked Lists](#)

## References
- [Linked List Wikipedia](https://en.wikipedia.org/wiki/Linked_list)
- [Data Structures: Linked List (GeeksforGeeks)](https://www.geeksforgeeks.org/linked-list-data-structure/)
  
---

## Metadata
```dataview
table
    DataStructureName as "Data Structure Name",
    Complexity as "Time Complexity"
where contains(file.name, "Data Structure")
sort file.ctime desc
```

**Tags:** #LinkedList #DataStructure #TechPlacements #DSA

---
