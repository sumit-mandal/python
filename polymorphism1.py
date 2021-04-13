#object classes can share same method name but can differently on different classes

class User():
    def sign_in(self):
        print('Logged in')

class Wizard(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with the  power of {self.power}')

class Archer(User):
    def __init__(self,name,num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left-{self.num_arrows}')

wizard1 = Wizard('bhau',100)
archer1 = Archer('Robin',100)
wizard1.attack()
archer1.sign_in()
print(wizard1.name)


#here we have 2 attack  but both the attack acts differently on different clasees
