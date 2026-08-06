# Fibonacci series is a series where each number is the sum of the two numbers before it
# Example of such series is: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,...

def fibonacci_loop(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
        
n = int(input("Enter how many terms: "))
print("Fibonacci Series: ")
fibonacci_loop(n)
