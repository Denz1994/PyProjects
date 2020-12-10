class Mammel:
    def walk(self):
        print('walk')


class Dog(Mammel):
    def bark(self):
        print('woof')


class Cat(Mammel):
    def meow(self):
        print('meow')


dog = Dog()
dog.bark()
cat = Cat()
cat.meow()
