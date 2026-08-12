name = "Oriole, Merciful"
print (name.strip())
with open("student.txt" "r") as file:
    for line in file:
        data = line.strip().split(',')
        
        name = data[0]
        age = data[1]
        print(f"Name: {name}")
        print(f"Age: {age}")