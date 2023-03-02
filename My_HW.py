print("Hello user, if you want to register, please provide the following data")

database = []

register_data = ""

user= {
    "name" : input("Enter your name (login length less than 5 characters) : "),
    "email" : input("Enter your email : "),
    "password" : input("Enter your password (password contains more than 10 symbols) : ")
}

if (len(user["name"])) < 5 or (len(user["password"])) > 10:
    print("Your name or password is incorret. Try again")
else:
    print("Thank you, you have successfully registered")

database.append(user)
print(database)
