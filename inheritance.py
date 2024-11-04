class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str(self):
        return f'|Fish|\nName : {self.name}\nAge : {self.age}\nSpeed: {self.speed}\n'


class Fish(Animal):

    def __init__(self, name, age, speed):
        super().__init__(name, age)
        self.speed = speed

        def __str(self):
            return f'|Fish|\nName : {self.name}\nAge : {self.age}\nSpeed: {self.speed}\n'

f = Fish(name= "dory", age= 3, speed= 10)
print(f.name)