class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def bark(self):
        print('woof')


class Cat(Mammal):
    def meow(self):
        print('meow')


dog = Dog()
dog.bark()
cat = Cat()
cat.meow()
