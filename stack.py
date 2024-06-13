class OddNumberStack:
    def __init__(self):
        self.stack = []

    def push(self, num):
        if num % 2 != 0:  
            self.stack.append(num)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")
odd_stack = OddNumberStack()
odd_stack.push(3)
odd_stack.push(6)
odd_stack.push(7)
odd_stack.push(10)

print("Stack contents:")
while not odd_stack.is_empty():
    print(odd_stack.pop())
