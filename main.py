class Person:
  height: 5000
  name = "Name"
  is_sad = True
  age = 5006
  def __init__(self, name, height, age):
    self.name = name
    self.height = height
    self.age - age
    
class Cat:
  color = "Black"
  age = 4
  height = 65
  name = "Name"

  def __init__(self, name, height, age):
    self.name = name
    self.height = height
    self.age = age


  def play_w_human(self, human):
    human.is_sad = False
    

me = Person("Banana", 5000, 5006)
my_pet = Cat("Vova", 19, 0.1)
my_friend = Person("Bunana", 5005 , 4999)
my_mom = Person("Banuna", 4500, 5500)
my_dad = Person("Bununa", 5500, 5954)

print(me.is_sad)
my_pet.play_w_human(me)
print("сумний(я) - ", me.is_sad)
my_pet.play_w_human(my_friend)
print ("Сумний(друг) -", my_friend.is_sad)




