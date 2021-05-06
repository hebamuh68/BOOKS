7.1

class stack_ADT():
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def Length(self):
        return len(self.stack)

    def POP(self):
        assert stack_ADT.isEmpty(self) == False, "List is empty."
        self.stack.pop()
        return self.stack[-1]

    def Peek(self, item):
        assert stack_ADT.isEmpty(self) == False, "List is empty."
        return id(self.stack[item])

    def push(self,item):
        self.stack.append(item)
        return self.stack


prompt = " enter an int value (<0 to end): "
mystack = stack_ADT()
value = int(input(prompt))
while value >= 0:
    mystack.push(value)
    value = int(input(prompt))

print(mystack.POP())

