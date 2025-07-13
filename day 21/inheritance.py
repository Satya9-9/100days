class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.num_eyes = 2
        self.score = 0

    def breathe(self):
        print("inhale , exhale")


    def walk(self):
        print(f"an animal {self.name} walks upto {self.age} years")

class Dog(Animal):
    def __init__(self,bite):
        super().__init__("tuffy", 1)
        self.bite_Capacity = bite

    def eat(self):
        self.bite_Capacity += 1
        print(f"a dog eats {self.bite_Capacity} times")

    def walk(self):
        super().walk()
        print ("i am doin walkins ")

sheru = Dog(10)
sheru.walk()
sheru.eat()
sheru.eat()

