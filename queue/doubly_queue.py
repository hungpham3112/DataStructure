class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None
        self.prev: Node | None = None


class DoublyQueue:
    # Function to initialize head
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def __repr__(self):
        current = self.head
        node = []
        while current:
            node.append(current.data)
            current = current.next
        return "None <- " + " <=> ".join(map(str, node)) + " -> None"

    def isempty(self):
        return self.size == 0

    def enqueue(self, data):
        """
        enqueue is a function to add a new data to the head of linked list
        Time complexity: O(1)
        Space complexity: O(1)
        """
        if self.head is None:
            self.head = self.tail = Node(data)
            self.size += 1
        else:
            new_node = Node(data)
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node
            self.size += 1

    def dequeue(self):
        """
        dequeue is a function to remove a data from the tail of linked list
        Time complexity: O(1)
        Space complexity: O(1)
        """
        if self.head is None:
            return None
        else:
            assert isinstance(self.tail, Node)
            self.tail = self.tail.prev
            assert isinstance(self.tail, Node)
            self.tail.next = None
            self.size -= 1


if __name__ == "__main__":
    dqueue = DoublyQueue()
    dqueue.enqueue(4)
    dqueue.enqueue(12)
    dqueue.enqueue(500)
    dqueue.enqueue(9)
    print(dqueue)
    dqueue.dequeue()
    print(dqueue)
    dqueue.dequeue()
    print(dqueue)
    #  print(len(dqueue))
