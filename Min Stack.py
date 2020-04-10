class MinStack(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.min=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.stack:
            self.min=x
        elif x<self.stack[-1]:
            self.min=x
        self.stack.append(x)
        return self
        
        

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:  
            self.stack.pop()
        return self
        

    def top(self):
        """
        :rtype: int
        """
       
        return  self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
