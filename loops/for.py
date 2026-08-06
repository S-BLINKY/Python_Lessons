# sentence =  "ABCDEFGHIJ"
# # for letter in sentence:
# #     print (letter)
    
# def printer(sentence):
#     for letter in sentence:
#         # (f " ") is called Formated strings
#         print("letter: ", letter)
# printer(sentence)

# fruits=["orange", " mango", "apple", "cherry"]
# def printer2 (array):
#     for fruit in fruits:
#         print (fruit)
# printer2(fruits)

# for i in range(2, 21, 2):
#     print (i)

# star = "*"
# def drawer(number):
#     for i in range (number):
#         print (i * "*")
        
# drawer(10)

# for row in range (1, 4):
#     for col in range (1, 4):
#         print(f"row{row}-column{col}")

# start = "65"
# for first_number in range (5):
#        print(f"start{65},first_number")
       
#        for second_number in range (10):
#              print(f"{start},{first_number}, {second_number}")
#        number_of_times = int(input("Enter number: "))
       
       
       
       
       
       
       
       
# number = int(input("Enter number: "))
# number_of_times = int(input("Enter number of times: "))
# for i in range(1, number + 1):
#     for j in range (1, number_of_times + 1):
#         print(f"{number} x {j} = {number * j}")
#     print("=" * 60)


rows = int(input("Enter number of rows: "))

for i in range (rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print (" ")
        
        