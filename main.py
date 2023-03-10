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
  is_sad = True


  def __init__(self, name, height, age):
    self.name = name
    self.height = height
    self.age = age


  def play_w_human(self, human):
    self.is_sad = False
    human.is_sad = False

class dog:
  age = 6
  height = 100
  is_sad = True
  name = "Name"

  def play_w_human2(self, human):
    self.is_sad = False
    human.is_sad = False

  def __init__(self, name, height, age):
    self.name = name
    self.height = height
    self.age = age


    

me = Person("Banana", 5000, 5006)
my_pet = Cat("Vova", 65, 4)
my_friend = Person("Bunana", 5005 , 4999)
my_mom = Person("Banuna", 4500, 5500)
my_dad = Person("Bununa", 5500, 5954)
my_pet2 = dog("vova2", 100, 6)

print("...")

print(me.is_sad)
my_pet.play_w_human(me)
print("сумний(я)(після гри з котом) - ", me.is_sad)
my_pet.play_w_human(my_friend)
print ("Сумний(друг)(після гри з котом) -", my_friend.is_sad)
print("сумний(кіт)(після гри з людьми) -", my_pet.is_sad)

print("...")

my_pet2.play_w_human2(me)
print("сумний(я)(після гри з собакою) - ", me.is_sad)
my_pet2.play_w_human2(my_friend)
print("Сумний(друг)(після гри з собакою) -", my_friend.is_sad)
my_pet2.play_w_human2(my_pet)
print("сумний(кіт)(після гри з собакою) -", my_pet.is_sad)
print("сумний(пес)(після гри з людьми та котом) -", my_pet2.is_sad)

print("...")




