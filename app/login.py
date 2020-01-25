def login(user_name, password):
    if len(user_name.strip()) == 0 or len(password.strip()) == 0:
        return "Missing username or password!"

    if user_name != "user" or password != "password":
        return "Invalid username or password!"
	
    return "Login successful!"
