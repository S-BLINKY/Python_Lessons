class Calculator:
    def add(self, Number1, Number2):
        return (Number1+Number2)
    
    def multiply(self, Number1, Number2):
        return Number1*Number2
    
    def divide(self, Number1, Number2):
        return Number1/Number2
    
calculator = Calculator()
result = calculator.add(400, 200)

print(result)