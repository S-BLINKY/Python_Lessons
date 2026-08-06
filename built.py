print(max(100, 200, 2, 34))

# def maximum(num1, num2, num3):
#     biggest = num1
#     if(biggest < num2):
#     biggest = num2
#     print(biggest)
#     elif(biggest < num3):
#         biggest = num3
#         print(biggest)
#     else:
#         print(biggest)
# maximum(800, 800.5, 700)

# def maximum2(a,b,c):
#     if(a > b and a > c):
#         print("The largest number is: ", a)
#     elif(b > a and b < c):
#         print("The largest number is: ", b)
#     else:
#         print("The largest number is: ", c)

# maximum2(10, 26, 40)

numbers = [1,2,3,4,5,6,7,8,9,10]
count = len(numbers)
print(count)

def length (iterable):
    count = 0
    for item in iterable:
        count = count + 1
    return count

result = length("HELLO MY PEOPLE. HOW WUNA DEY!")
print("the count is: ", result)

# def square(number):
#     result = number * number
#     return result
# print(square(5))

square = lambda x: x * x


def even(number):
    return number % 2 == 0

print(even(2))
#     if (number % 2 == 0 ):
#         print ("Number is even")
#     else:
#         print ("Number is odd")
        
# even(50)




        
    


        