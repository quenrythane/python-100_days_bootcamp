# parent class
class Animal:
    def __init__(self, name, eyes):
        self.num_eyes = eyes
        self.name = name

    def breathe(self):
        print("Inhale, exhale")

    def hello(self):
        print("Hello friend :)")


# child class
class Fish(Animal):
    # Fish class inheritance from Animal class
    def __init__(self, new_name):
        # init as always
        # super() mean parent class (Animal) and because Animal class need 2 parameters so we have to give they
        # upper innit has new paramater (if it will be name, it will overrides previous parameter)
        super().__init__("x", 2)
        self.new_name = new_name

    # we could create new methods
    def swim(self):
        print("moving in water")

    # we could override old methods
    def breathe(self):
        print("New breathing")


nemo = Fish("Nemo")
print(f"Old name: {nemo.name}, New name: {nemo.new_name}, eyes number: {nemo.num_eyes}")
nemo.hello()
nemo.swim()
nemo.breathe()  # as we can see this is overrode method
