FILENAME = "students.txt"

def register_student():
    stud_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    dept = input("Enter Department: ")
    
    # To save as: ID, name, age, dept:
    with open(FILENAME, "a") as file:
        file.write(f"{stud_id}, {name}, {age}, {dept}\n")
        print("Student registered successfully!\n")
        
def display_students():
    try:
        with open(FILENAME, "r") as file:
            students = file.readlines()
            
        if not students:
            print("No students found.\n")
            return
        
        print("\n--- Student LIst ---")
        print("ID | Name | Age | Department")
        print("-" * 30)
        for student in students:
            stud_id, name, age, dept = student.strip().split(",")
            print("-" * 30 + "\n")
    except FileNotFoundError:
        print("No records found. Register students first.\n")
        
def search_student():
    search_id = input("Enter Student ID to search: ")
    found = False
    try:
        with open(FILENAME, "r") as file:
            for student in file:
                stud_id, name, age, dept = student.strip().split(",")
                if stud_id == search_id:
                    print("\n--- Student Found ---")
                    print(f"ID: {stud_id}")
                    print(f"Name: {name}")
                    print(f"Age: {age}")
                    print(f"Department: {dept}\n")
                    found = True
                    break
                if not found:
                    print("Student ID does not exist.\n")
    except FileNotFoundError:
        print("No records found.\n")
        
def main():
    while True:
        print("==== Student Record System ====")
        print("1. Register Student")
        print("2. Display Students")
        print("3. Search")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            register_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else: 
            print("Invalid choice. Try again.\n")
            
main()