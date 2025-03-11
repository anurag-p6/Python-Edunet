username = input("Enter your username: ");
password = input("Enter your password: ");

req = {
  "username": username,
  "password": password,
}

def signupUser(req):
    print("User signed up successfully!");
    return req

signupUser(req)

signin_username = input("Enter the username for signin: ");
signin_password = input("Enter the password for signin: ");

def signinUser(req, signin_username, signin_password):
    if (signin_username == req["username"] and signin_password == req["password"]):
        print("User signed in successfully!");
    else: 
        print("Invalid credentials!") 
    return req

signinUser(req, signin_username, signin_password)