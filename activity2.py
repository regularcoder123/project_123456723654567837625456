class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #info/display function
    def info(self):
        print(f"Hi I am a {self.name} and I am {self.age} years old! ")

    #make sound
    def makesound(self):
        print("Woof Woof")
class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Hi I am a {self.name} and I am {self.age} years old! ")
    def makesound(self):
        print("Meow")
odog = Dog("Jerry",23456789)
ocat = Cat("wuevhwfhodofewiofowfiohewfeufhwfuuosuliuwqfhbof;qfuharehyg,kyeqgrffetytgyheytghersrfk,j,hytgrthgrshuiehsygefersru,hhgru,hud,tgtiojiohtpohtpohphotdijhrgjrhgsegsgeffegaafeofqehfwioehfwiohfwfwifhiwhfwiefhiwhfiowhfohfoia;whoi;aefrhoa;owefhwoufheeohefohfhhfowhfwohfwhfaoirhoierhfeoirhfiohhwihfh eiehfhefiwhefwhefwfehh",345678376536765436875746464553424231323244354564667575777887878999987654321234567890987654321234567890987654321)

for animal in (odog,ocat):
    animal.info()
    for sound in (odog,ocat):
        sound.makesound()