password = raw_input("create a password: ")
password_entry = raw_input("Please enter your password: ")

count = 0

while password_entry != password and count < 2:
    print("Incorrect Password!")
    password_entry = raw_input("Please enter your password: ")
    count += 1
if password_entry == password:
    print("Login Successful")
else:
    print("You have too many incorrect attempts. You've been locked out")


