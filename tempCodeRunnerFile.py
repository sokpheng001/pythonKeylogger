from uuid import uuid4
import string;
import json;

uuid_generated = uuid4();
password_generated = string.ascii_letters + string.hexdigits ;

class Animal:
    def __init__(self, name, sound):
        self.__sound = sound;
        self.__name  = name;
    def make_sound(self):
        print("Created sound: {}".format(self.__sound))
    def __str__(self):
        return "Animal name: " + self.__name;
class Cat(Animal):
    def __init__(self, sound=None):
        self.__sound = sound;
    def make_sound(self):
        print("Created sound: {}".format(self.__sound));
        super().__init__("Animal", "Moew");

dog = Animal("Dog","Bark");
cat1  = Cat("Moew");
cat1.make_sound();
dog.make_sound();