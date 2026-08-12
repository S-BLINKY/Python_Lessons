class Shapes:
    def draw(self):
        print("drawing a shape..........")
        
class Square(Shapes):
        def __init__(self, sides):
            self.sides = print("Enter number of sides: ")
            
        def draw(self):
            for i in range (self.sides):
              print("🟦" * self.sides)
              
shape = Shapes()
shape.draw()


class Rectangle(Shapes):
    def __init__(self, width, lenght):
        self.width = print("Enter desired width: ")
        self.lenght = print("Enter desired lenght: ")
    def draw(self):
        for i in range (self.lenght):
            print("🟥" * self.width)
        
class Traingle(Shapes):
    def __init__(self, height):
        self.height = print("Enter preferred height: ")
    def draw(self):
        for i in range (1, self.height + 1):
            print("🌹" * i)
            

# square.draw()  
# print("================================")

# rectangle.draw()
# print("================================")

# triangle.draw()

class result(Shapes):
 def result():
    while True:
        print("==== Shapes ====")
        print("1. Square")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            square = Square()
            square.draw()
        elif choice == "2":
            rectangle = Rectangle()
            rectangle.draw()
        elif choice == "3":
            triangle = Traingle()
            triangle.draw()
        elif choice == "4":
            print("Exiting program. Goodbye!😉")
            break
        else:
            ("Invalid choice. Try again.\n")
            

    
    # ASS: make the above shapes be options with the user being the one to write the number for the shapes. and the forth option should an exit.
    
            
