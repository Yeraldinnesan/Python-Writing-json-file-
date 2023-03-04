import json

data = {}
data["users"] = []

# Function to register a user
def register_user():
    print('User Registration')
    while True:
        try:
            email = input('Email: ')
            with open('users.json', 'r') as file:
                users = json.load(file)
                if email in users:
                    raise ValueError('Email already exists!')

            password = input('Password (must have at least 8 characters): ')
            if len(password) < 8:
                raise ValueError('Password is too short :(')

            user = {"email": email, "password": password}
            data["users"].append(user)

            with open('users.json', 'w') as file:
                json.dump(data, file, indent=4)

            print('User registered successfully!')
            break

        except ValueError as error:
            print(error)

# Function to display all users
def display_users():
    print('All registered users:')

    with open('users.json', 'r') as file:
        users_data = json.load(file)

    for user in users_data["users"]:
        print(f'Email: {user["email"]}')

    print()


# Function to log in a user
def log_in():
    print('User Log In')
    while True:
        email = input('Email: ')
        password = input('Password: ')

        with open('users.json', 'r') as file:
            users_data = json.load(file)

        for user in users_data["users"]:
            if user["email"] == email and user["password"] == password:
                print('You have logged in successfully!')
                return

        print('Invalid email or password')
        choice = input('Would you like to try again? (Y/N) ').lower()
        if choice == 'n':
            print('Goodbye!')
            return
  
# Menu


while True:
    print('WELCOME TO MY FIRST PROGRAM :)')
    print('1. Register a user')
    print('2. Display all registered users')
    print('3. Log In')
    print('4. Exit')
    option = input('Select an option: ')
    if option == '1':
        register_user()
    elif option == '2':
        display_users()
    elif option == '3':
        log_in()
    elif option == '4':
        print('Goodbye!')
        break
    else:
        print('Invalid option. Please select a valid option.')
