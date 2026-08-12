class Shapes:
    def draw(self):
        print("drawing a shape..........")
        
class Square(Shapes):
        def __init__(self, sides):
            self.sides = sides
            
        def draw(self):
            for i in range (self.sides):
              print("🟦" * self.sides)
              
shape = Shapes()
shape.draw()


class Rectangle(Shapes):
    def __init__(self, width, lenght):
        self.width = width
        self.lenght = lenght
    def draw(self):
        for i in range (self.lenght):
            print("🟥" * self.width)
        
class Traingle(Shapes):
    def __init__(self, height):
        self.height = height
    def draw(self):
        for i in range (1, self.height + 1):
            print("🌹" * i)
            
square = Square(6)
square.draw()  
print("================================")
rectangle = Rectangle(3, 6)
rectangle.draw()
print("================================")
triangle = Traingle(10)
triangle.draw()
    
    # ASS: make the above shapes be options with the user being the one to write the number for the shapes. and the forth option should an exit.