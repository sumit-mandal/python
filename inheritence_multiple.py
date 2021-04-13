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

    def check_arrows(self):
        print(f"{self.num_arrows} remaining")

    def attack(self):
        print(f'attacking with arrows: arrows left-{self.num_arrows}')

    def run(self):
        print("ran really fast")

class HybridBorg(Wizard,Archer):
    def __init__(self,name,power,num_arrows):
        Archer.__init__(self,name,num_arrows)
        Wizard.__init__(self,name,power)


hb1 = HybridBorg('borgiee',50,100)
print(hb1.attack())
print(hb1.check_arrows())
