import sys
import os

def permission_matrix(filename):
    user_database = {}
    try:
        if not os.path.exists(filename):
            return{}
        with open('MAC.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if not line: continue                

                split_line = [s.strip() for s in line.split(',')]
                subject = split_line[0].split(':')
                if len(subject) < 2: continue
                username = subject[1].strip()

                user_permissions = {}
                for perms in split_line[1:]:
                    if ':' in perms:
                        file_name, file_perm = perms.split(':')
                        user_permissions[file_name.strip()] = file_perm.strip()

                user_database[username] = user_permissions
    except FileNotFoundError:
        print("Error. File not found.")
    return user_database

def regular_user_menu(username, permissions):
    while True:
        print(f"----- User: {username} -----")
        print("1. Check file permissions.")
        print("2. Read File.")
        print("3. Edit File")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            for file, file_perm in permissions.items():
                print(f"File name: {file} - Permission: {file_perm}")

        elif choice == '2':
            target_file = input("Enter File to READ (i.e. file_1): ").strip()
            if target_file in permissions:

                if 'r' in permissions[target_file]:
                    print(f"ACCESS GRANTED: Opening {target_file}-----\n")
                    try: 
                        with open(f"{target_file}.txt", "r") as file:
                            print(f"-----{target_file}-----")
                            print(file.read())
                            print("-" * 50)
                    except FileNotFoundError:
                        print("Error. File not found.")
                else:
                    print(f"ACCESS DENIED: No permissions granted to {target_file}.")
            else:
                print("File not found.")

        elif choice == '3':
            target_file = input("Enter File to EDIT (i.e. file_1): ").strip()
            if target_file in permissions:
                if 'w' in permissions[target_file]:
                    new_content = input(f"ACCESS GRANTED: Enter new data for {target_file}:\n")
                    try:
                        with open(f"{target_file}.txt", "a") as file:
                            file.write(new_content + "\n")
                        print(f"Entry added to {target_file}")
                    except Exception as e:
                        print(f"Could not write to file {e}")
                else:
                    print(f"ACCESS DENIED: You do not have write permissions for {target_file}")
            else:
                print("File not found.")
        
        elif choice == '4':
            print("Exiting session-----")
            break

def regular_sign_in():
    db = load_database('MAC.txt')
    username_entry = input("Enter Subject Name: ").strip()

    if username_entry in db:
        print(f"Access Granted to: {username_entry}")
        regular_user_menu(username_entry, db[username_entry])
    else:
        print("User not found.")



def view_table():
    file = open('MAC.txt')

    results = file.read()

    print("-" * 30, "Current MAC Table", "-" * 30)
    print(results)
    print("-" * 79)

def admin_sign_in():
    admin_username = "admin"
    print("-----Admin Login-----")
    while True:
        credentials = input("Please enter your admin username, or enter 'Q' to exit the system:\n").strip()
        if credentials.upper() == 'Q':
            sys.exit()        
        elif credentials == admin_username:
            print("Admin Access Granted.\n")
            return True
        else:
            print("Admin Access Denied. Please enter admin username.\n")
            return False

def add_new_user():
    input_new_user = input("Please enter the name of the new user:\n").strip()
    print("Permission levels are [r] - read only, [r/w] - read and write, and [np] - no permissions.")
    permissions = []
    for i in range(1,6):
        perm = input(f"Enter permission for File {i} regarding {input_new_user}: ")
        permissions.append(f"file_{i}: {perm}")
    new_line_entry = f"subject: {input_new_user}, " + ", ".join(permissions) 

    with open('MAC.txt', 'a') as file:
        file.write(new_line_entry + "\n")
    print(f"User {input_new_user} successfully added.\n")
    print("-" * 79)
    
def check_file_access():
    print("You have chosen to verify a user's access")
    selected_user = input("Please enter a username to check their access: \n").strip()   
    selected_file = input("Please select the file you would like to check access for (i.e. file_1, file_2):\n").strip()

    try: 
        with open ('MAC.txt', 'r') as file:
            for line in file:
                if f'subject: {selected_user}' in line:
                    split_line = line.strip().split(', ')
                    parsed_line = {}
                    for s in split_line:
                        if ':'in s:
                            key, value = s.split(': ')
                            parsed_line[key.strip()] = value

                    if selected_file in parsed_line:
                        print(f"Access for {selected_user} on {selected_file}: {parsed_line[selected_file]}")
                        return
                    else:
                        print(f"File '{selected_file}' not found for user.")
                        return
                   
            print("User not found.")
    except FileNotFoundError:
        print("MAC.txt not found.")

def main():
    while True:
        print("-" * 25 + " MAC ACCESS " + "-" * 20)
        print("1. User Sign In")
        print("2. Admin Sign In")
        print("3. Exit")
        print("-" * 75)

        sign_in_choice = input("Enter your selection: ")

        if sign_in_choice == '1':
            db = permission_matrix('MAC.txt')
            subject_selection = input("Enter Your Username: ").strip()
            if subject_selection in db:
                print(f"-----Welcome {subject_selection}-----")
                regular_user_menu(subject_selection, db[subject_selection])
            else:
                print("User not found.")

        elif sign_in_choice == '2':
            if admin_sign_in():
                while True:
                    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------") 
                    print("Please select an action:")
                    print("1. Admin Sign In.")
                    print("2. Add New User.")
                    print("3. View MAC file.")
                    print("4. Check a user's file permissions.")        
                    print("5. Log Out.")
                    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
                    choice = input("Please enter 1, 2, 3, 4, 5, or 6: ")
                    
                    if choice == '2':
                        add_new_user()
                    elif choice == '3':
                        view_table()
                    elif choice == '4':
                        check_file_access()
                    elif choice == '5':
                        print("Signing Out.")
                        break
                    else:
                        print("Invalid selection. Please enter 1, 2, 3, 4, 5, or 6.")

        elif sign_in_choice == '3':
            sys.exit()

main()

    

