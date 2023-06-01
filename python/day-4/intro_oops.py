class Greeting:
    
    name = "Mark"
    
    def __init__(self,section):
        print("Constructor is called")
        self.section = section
    
    def say_hello_world(self):
        return "Hello World"
    
    def say_hello(self,name):
        return f"Hello, {name}"
    
    def say_hello_mem_var(self):
        return f"Hello, memnber variable {self.name}"
    
    def __str__(self):
        return "This is a Greet Class"
    
greeting  = Greeting('C')
print(greeting.say_hello_world())
print(greeting.say_hello("Sambit"))
print(greeting.name)
print(greeting.say_hello_mem_var())