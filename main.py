class Person:
  height: 5000
  name = "Name"
  is_sad = True
  def __init__(self, name, height):
    self.name = name
    self.height = height
    
class Cat:
  color = "Black"
  age = 4
  height = 65
  name = "name"

  def __init__(self, name, height, age):
    self.name = name
    self.height = height
    self.age = age

  def play_w_homan(self, human):
    human.is_sad = False
    

me = Person("Banana", 5006)
my_pet = Cat("Vova", 60, 4)

print(me.is_sad)



