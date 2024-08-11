class MyDoublyLinkedList:
    class New_Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_to_tail(self, data):
        new_node = self.New_Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove_last(self):
        if not self.head:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        if index < self.size // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.size - 1, index, -1):
                current = current.prev
        return current.data

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

List = [4, 6, 7, 9, 12, 15, 20]
list = MyDoublyLinkedList()
for i in List:
    list.push_to_tail(i)

print(list.__len__())
print(list.get(1))
print(list.get(5))
#print(list.get(6))
list.remove_last()
print(list.__len__())