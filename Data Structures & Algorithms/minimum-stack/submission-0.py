class MinStack:

    def __init__(self):
        self.stack = []
        self.minInds = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minInds) == 0 or self.stack[self.minInds[-1]] > val:
            self.minInds.append(len(self.stack) - 1)


    def pop(self) -> None:
        self.stack.pop()

        if self.minInds[-1] > len(self.stack) - 1:
            self.minInds.pop()
    

    def top(self) -> int:
        return self.stack[-1]

        
    def getMin(self) -> int:
        return self.stack[self.minInds[-1]]
        
