class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        
    def display(self):
        print(f"the name is {self.name}")
        
    def checker(self):
        if(self.age >= 18):
            print("You are an adult")
        else:
            print("You are not an adult")

p1 = Person("Sakou", 17, "Bamenda")

p1.display()
p1.checker()