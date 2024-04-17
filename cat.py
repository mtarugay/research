class Cat:
    name : None
    age : None
    __happy : None

    def __init__(self, name, age, happy):
        self.name = name
        self.age = age
        self.__happy = happy

    def sound(self):
        print("meow")

    def display(self):
        print("--CAT DETAILS--")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Happy:", self.__happy)

    def get_happy(self):
        return self.__happy
    
    def set_happy(self, newhappy):
        self.__happy = newhappy

class Domesticated_Cat(Cat):
    owner: None

    def __init__(self, owner, name, age, happy):
        super().__init__(name, age, happy)
        self.owner = owner
        self.name = name
        self.age = age
        self.__happy = happy
    
    def display(self):
        print("--CAT DETAILS--")
        print("Owner:", self.owner)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Happy:", self.__happy)


class Wild_Cat(Cat):
    def __init__(self, name, age, happy = True):
        super().__init__(name, age, happy)
        self.name = name
        self.age = age
        self.__happy = happy

    def sound(self):
        print("grrr")


cat1 = Cat("Tom", "3", True)
cat1.display()
cat1.sound()

cat2 = Domesticated_Cat("Jimmy", "Joe", "3", True)
cat2.display()
cat2.sound()

cat3 = Wild_Cat("Mike", "2", True)
cat3.display()
cat3.sound()