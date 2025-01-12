print("Create your account ")
username=input("Enter your username: ")
password=input("Enter your password: ")
print("Account created successfully!")
print("Please sign into your account.")
print("Account Login:")
#User inputs their username and password:
username2=input("Enter your username: ")
password2=input("Enter your password: ")
print("Account logged in successfully!")

#Check if username and password are correct
if username2==username and password2==password:
    print("Welcome to your account! You are logged in successfully")
else:
    print("Invalid username or password!")
