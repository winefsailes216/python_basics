class Mammal:
  def walk(self): #this is method
    print("walk")
    
    
class Dog(Mammal):
  def bark(self): #this is method
    print("bark bark")
  
    
cooper = Dog() #cooper is object
print(cooper.walk())