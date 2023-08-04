# 1918번

class Stack:
    def __init__(self):
        self.s = []
        self.pointer = -1

    def pop(self):
        if self.pointer < 0:
            raise AttributeError
        self.pointer -= 1
        return self.s.pop()
    
    def push(self, value):
        self.s.append(value)
        self.pointer += 1

    def peek(self):
        if self.pointer >= 0:
            return self.s[self.pointer]
        else:
            return ""
        
    def __str__(self) -> str:
        return "".join(self.s)


input = input()
stack = Stack()
result = ""
operator = "+-*/()"

for s in input:
    if s in operator:
        if s == ")":
            while stack.peek() != "(":
                result += stack.pop()
            stack.pop()
        elif s == "+" or s == "-":
            while stack.peek() != "" and stack.peek() != "(":
                result += stack.pop()
            stack.push(s)
        elif s == "*" or s == "/":
            while stack.peek() == "*" or stack.peek() == "/":
                result += stack.pop()
            stack.push(s)
        else:
            stack.push(s)
    else:
        result += s

while stack.pointer >= 0:
    result += stack.pop()

print(result)