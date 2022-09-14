class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None
        self.prev: Node | None = None


class DoublyStack:
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

    def push(self, data):
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

    def pop(self):
        if self.head is None:
            raise IndexError("pop from empty stack")
        else:
            popped = self.head.data
            self.head = self.head.next
            assert self.head is not None
            self.head.prev = None
            self.size -= 1
            return popped

    def peek(self):
        if self.isempty():
            return None
        else:
            assert isinstance(self.head, Node)
            return self.head.data


if __name__ == "__main__":
    dstack = DoublyStack()
    dstack.push(1)
    dstack.push(2)
    dstack.push(3)
    dstack.push(9)
    #  dstack.push(9)
    #  dstack.push(15)
    print(dstack)
    dstack.pop()
    print(dstack)
    dstack.pop()
    print(dstack)
    #  print(dstack)
    #  print(dstack.peek())
    #  print(len(dstack))
    #  lst = []
    #  lst.pop()
