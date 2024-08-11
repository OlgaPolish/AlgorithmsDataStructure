class MyLinkedList:
    class New_Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0

    def push_to_tail(self, data):
        new_node = self.New_Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def remove_last(self):
        if not self.head:
            return

        if not self.head.next:
           self.head = None
        else:
            current = self.head
            while current.next and current.next.next:
                current = current.next
            current.next = None
        self.size -= 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0


List = [4, 6, 7, 9, 12, 15, 20]
list = MyLinkedList()
for i in List:
    list.push_to_tail(i)

print(list.__len__())
print(list.get(1))
print(list.get(5))
#print(list.get(6))
list.remove_last()
print(list.__len__())