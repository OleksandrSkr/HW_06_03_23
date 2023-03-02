#-----------------------------------------------------------------------------------
#print("Hello user, if you want to register, please provide the following data")

#register_data = {}

#register_data['name'] = input("Enter your name (login length less than 5 characters) : ")
#register_data['email'] = input("Enter your email : ")
#register_data['password'] = input("Enter your password (password contains more than 10 symbols) : ")

#if len(register_data['name']) < 5 or len(register_data['password']) > 10:
#    print("Your name or password is incorret. Try again")
#else:
#    print("Thank you, you have successfully registered")
#    print(register_data)

#------------------------------------------------------------------------------
#print("Hello user, if you want to register, please provide the following data")

#database = [
#    {"name" , "email" , "password" ,} ,
#]

#register_data = {
#    "name" : input("Enter your name (login length less than 5 characters) : "),
#    "email" : input("Enter your email : "),
#    "password" : input("Enter your password (password contains more than 10 symbols) : ")
#}

#if (len(register_data["name"])) < 5 or (len(register_data["password"])) > 10:
#    print("Your name or password is incorret. Try again")
#else:
#    print("Thank you, you have successfully registered")
#
#database.append(register_data)
#print(database)

#------------------------------------------------------------------------------------

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



