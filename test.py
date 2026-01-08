class Stack:
    def __init__(self):
        self.items = []
        
    def push (self, item):
        self.items.append(item)
        
    def pop (self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack kosong"
            
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack kosong"
            
    def is_empty(self):
        return len(self.items) == 0
            
    def display(self):
        print("Isi Stack (Top -> Bottom):", list (reversed(self.items)))
        
stack = Stack ()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()
print("Elemen atas:", stack.peek())

print("pop:", stack.pop())
stack.display()
