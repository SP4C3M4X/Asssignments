user = ("admin")
pass_in = ("password@123")

count = 0
while count < 3:
    username = (input("Enter the username: "))
    password = (input("Enter your password: "))

    if username == user and password == pass_in:
        print("Login successful")
        break
    else:
        count += 1
        print("Wrong credentials")