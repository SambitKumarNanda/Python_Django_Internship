# class MathFunction:
    
#     a = None
#     b = None
    
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
    
#     def sum(self):
#         return self.a + self.b
    
#     def sub(self):
#         return self.a - self.b
    
#     def mul(self):
#         return self.a * self.b 
    
#     def div(self):
#         return self.a / self.b
    
# obj = MathFunction(5, 2)
# print(obj.sum())       
# print(obj.sub())       
# print(obj.mul())       
# print(obj.div())    

class MathFunction:
     
    def sum(self,a,b):
        return a + b
    
    def sub(self,a,b):
        return a - b
    
    def mul(self,a,b):
        return a * b 
    
    def div(self,a,b):
        return a / b
    
    
class MathFormulas(MathFunction):
    
    def method1(self,a,b):
        return self.mul(self.sum(a, b),self.sum(a, b))
    
    
# obj = MathFormulas()
# print(obj.method1(5, 2))