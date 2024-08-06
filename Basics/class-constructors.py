class Person:
  def __init__(self,name):
      self.name=name
  def talk(self):
    print(f"hi {self.name}")
    
name = input(">")    
john = Person(name)

john.talk()