class MathClass(object):
    def __init__(self):
        self.num = 0
    
    def factorial(self,n): 
        if n < 0: 
            return 0
        elif n == 0 or n == 1: 
            return 1
        else: 
            fact = 1
        while(n > 1): 
            fact *= n 
            n -= 1
        return fact 
    
    def square(self, n):
        return n * n
  
