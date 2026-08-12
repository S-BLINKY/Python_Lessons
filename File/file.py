# file = open("student.txt", "r")
# content =file.read()
# print(content)

# file.close()

# with open("student.txt", "r") as file:
#     content = file.read()
# print(content)

# with open("student.txt", "r") as file:
#     for line in file:
#         # strip is used to remove spaces between contents in the result
#         print(line.strip())
#         print("======================================")


# with open("student.txt", "r") as document:
#     line1 = document.readline()
#     line2 = document.readline()
    
# print(line1)
# print(line2)

# with open("to_do_list.txt", "W") as file:
#     file.write("1. Get up from bed\n")
#     file.write("2. Take a bath\n")
#     file.write("3. Have breakfast\n")
#     file.write("4. Prepare for school\n")

# with open("text.txt", "w") as file:
#     for i in range(1,6):
#         text = input("Enter text: ")
#         file.write(f"{i}. {text}\n")

# with open("text.txt", "w") as file:
#     for i in range(6,8):
#         text = input("Enter text: ")
#         file.write(f"{i}. {text}\n")

# with open("new.txt", "x") as file:
#     file.write("this is a new file that has added")


# import os
# if (os.path.exists("text.txt")):
#     print("true the file exists")
# else:
#     print("file doesn't exist")
    
    
try :
    with open("student.txt", "r") as file:
       content = file.read()
       print(content)
        
except:
    print("file does not exist")