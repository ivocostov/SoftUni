# Класът е създаден за да се демонстрира, че стека има само 4 операции, защото в Python няма начин да се декларира че листа е реално стек.
# В практиката е добре да се декларира стека като class за да се избегне употребата на останалите операции за лист като: remove, sort и всички останали.

class Stack:
    def __init__(self):
        self.values = []


    def push(self, value):
        self.values.append(value)

    def pop(self):
        return self.values.pop()


    def peek(self):
        return self.values[-1]


    def count(self):
        return len(self.values)


s = Stack()

for v in range(5, 10):
    s.push(v)

s.push(1)
print(s.values)
print(s.pop())
print(s.peek())
print(s.count())