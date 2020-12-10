class Person:
    def __init__(self, name: str, sex: str):
        self.name = name
        self.sex = sex

    def talk(self, msg: str):
        print('This is {}'.format(self.name))
        print('{}\n'.format(msg))


man = Person('Denzell', 'M')
woman = Person('Jessica', 'F')

man.talk('Hello')
woman.talk('Hey')
