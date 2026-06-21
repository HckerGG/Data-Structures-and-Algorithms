class Stack:
    def __init__(self):
        self.stack = []

    def push(self, elmt):
        self.stack.append(elmt)
        print(f"Pushed into stack > {elmt}")
    
    def pop(self):
        if self.stack != []:
            elmt = self.stack.pop()
            print(f"Removed from stack > {elmt}")
        else:
            print("Underflow!")
    
    def display(self):
        if self.stack != []:            
            for i in self.stack:
                print(i, end="\n")
            print(f"For nerds: {self.stack}")
        else:
            print(f"Underflow!")
    def peek(self):
        print(f"Top value > {self.stack[-1]}")
    
    def isEmpty(self):
        if self.stack == []:
            return True
        else:
            return False

stack = Stack()

stack.push(25)
stack.push(50)
stack.push(75)
stack.push(100)
stack.pop()
stack.peek()