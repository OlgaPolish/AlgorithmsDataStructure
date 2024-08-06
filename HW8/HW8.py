class Stack:
    def __init__(self):
        self.stack = []

    def empty(self):
        if len(self.stack) == 0:
            return "Stack is empty"
        return self.stack

    def push(self, item):
        self.stack.append(item)

    def pop(self):
         if len(self.stack) == 0:
            return None
         return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[len(self.stack) - 1]

    def search(self, element):
        if element in self.stack:
            num = len(self.stack) - self.stack.index(element) - 1
            return num
        return -1


mystack = Stack()
mystack.push(1)
mystack.push("Two")
mystack.push(3)
mystack.push("Four")
print(mystack.empty())
print(mystack.peek())
print(mystack.search("Two"))
mystack.pop()
mystack.pop()
print(mystack.search(3))