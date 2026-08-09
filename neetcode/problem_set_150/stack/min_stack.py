'''
Design a stack class that supports the push, pop, top, and getMin operations.

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

Each function should run in O(1)O(1) time.
'''

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        elif val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])
        

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.min_stack.pop()
            return self.stack.pop()
        else:
            raise IndexError('Empty Stack')

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            raise IndexError('Empty Stack')
        

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return self.min_stack[-1]
        else:
            raise IndexError('Empty Stack')



minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
print(minStack.getMin())
minStack.pop()
print(minStack.top())  
print(minStack.getMin())