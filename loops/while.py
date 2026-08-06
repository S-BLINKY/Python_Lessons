
# count = 1

# while count <= 10:
#     print(count)
#     count += 1
    
    
correct_pass = 1234
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    pin = int(input("Enter password: "))
    
    if (pin == correct_pass):
        print("access granted. Welcome!")
        print("Update your profile: ")
        break
    else:
        attempts += 1
        print("Incorrect password")
    if (attempts < max_attempts):
        print(f"You have {max_attempts - attempts} attempt(s) left.")
        
if (attempts == max_attempts):
    print ("Your account has been blocked. you are bnned from this platform")
    