
def permission_matrix(macfile):
    user_database = {}
    try:
        with open(macfile, 'r') as file:
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
        print(f" USER SESSION: {username} ".center(120, '-'))
        print("1. View file permissions.")
        print("2. Read File.")
        print("3. Add New Line to a File")
        print("4. Logout")
        print("5. Exit System")
        print("-" * 120)
        choice = input("Select an option: ")
        match choice:
            case '1':
                print(f" File Permissions for {username} ".center(120, '-'))
                for file, file_perm in permissions.items():
                    print(f"File name: {file} - Permission: {file_perm}")
            case '2':
                print(" READING FILE ".center(120,'-'))
                while True:
                    target_file = input("Enter File to READ (i.e. file_1) or Enter 'back' to select a different option:\n").strip()
                    if target_file in permissions:
                        if 'r' in permissions[target_file]:
                            print(f" ACCESS GRANTED: Opening {target_file} ".center(120, '-'))
                            try: 
                                with open(f"{target_file}.txt", "r") as file:
                                    print(f" {target_file} ".center(120, '-'))
                                    print(file.read())
                                    print("-" * 120)
                            except FileNotFoundError:
                                print("Error. File not found.")
                        else:
                            print(f"ACCESS DENIED: No permissions granted to {target_file}.")
                    elif target_file.lower() == 'back':
                        break
                    else:
                        print("File not found.")
            case '3':
                print(" FILE EDITOR ".center(120,'-'))
                while True:
                    target_file = input("Enter File to EDIT (i.e. file_1) or Enter 'back' to select a different option:\n").strip()
                    if target_file in permissions:
                        if 'w' in permissions[target_file]:
                            print(f" ACCESS GRANTED. Editing {target_file} ".center(120, '-'))
                            new_content = input(f"Enter new data for {target_file}:\n")
                            try:
                                with open(f"{target_file}.txt", "a") as file:
                                    file.seek(0)
                                    file.write(new_content + "\n")
                                print(f"Entry added to {target_file}")
                            except Exception as e:
                                print(f"Could not write to file {e}")
                        else:
                            print(f" ACCESS DENIED: You do not have write permissions for {target_file} ".center(120, '-'))
                    elif target_file.lower() == 'back':
                        break
                    else:
                        print("File not found.")
            case '4':
                print(" LOGGING OUT ".center(120, '-'))
                return
            case '5':
                print("[TERMINATING SESSION]".center(120, '*'))
                exit()
            case _:
                print("Invalid option. Please enter 1, 2, 3, 4, or 5.")

def sign_in():
    while True:
        db = permission_matrix('MAC.txt')
        print(" User Sign In ".center(120,'-'))
        username_entry = input("Enter a Username from the MAC.txt File, 'admin' for the admin menu, 'back' to return to the previous menu, or 'exit' to Exit:\n").strip()
        match username_entry:
            case _ if username_entry in db:
                print(f" Access Granted. Welcome: {username_entry} ".center(120, '-'))
                print("-" * 120)
                regular_user_menu(username_entry, db[username_entry])
            case _ if username_entry.lower() == 'admin':
                print("Admin Access Granted.")
                admin_menu()
            case 'back':
                return
            case 'exit':
                print("[TERMINATING SESSION]".center(120, '*'))
                exit()
            case _:
                print("User not found.")

def view_table():
    file = open('MAC.txt')
    results = file.read()
    print(" Current MAC Table ".center(120,'-'))
    print(results)
    print("-" * 120)

def add_new_user():
    print(" ADDING NEW USER ".center(120,'-'))
    input_new_user = input("Please enter the name of the new user:\n").strip()
    print("Permission levels are [r] - read only, [r/w] - read and write, and [np] - no permissions.")
    permissions = []
    for i in range(1,6):
        perm = input(f"Enter permission for file_{i} regarding {input_new_user}: ")
        permissions.append(f"file_{i}: {perm}")
    new_line_entry = f"subject: {input_new_user}, " + ", ".join(permissions) 
    with open('MAC.txt', 'a+') as file:
        file.seek(0)
        mac_content = file.read()
        if mac_content and not mac_content.endswith("\n"):
            file.write("\n")
        file.write(new_line_entry + "\n")
    print(f"User {input_new_user} successfully added.")
    print("-" * 120)
    
def check_file_access():
    print(" VERIFYING FILE ACCESSS ".center(120,'-'))
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

def edit_user_permissions():
    print(" EDITING PERMISSIONS ".center(120,'-')) 
    db = permission_matrix('MAC.txt')
    permission_options = ['r', 'r/w', 'np']
    while True:
        select_user_to_edit = input("Please enter the name of the User you wish to edit (or type quit to return to previous menu): ").strip()
        match select_user_to_edit:
            case 'quit':
               return
            case _ if select_user_to_edit in db:
                break
            case _:
                print(f"{select_user_to_edit} not found in MAC.txt")
    while True:
        select_file_to_edit = input(f"Please enter the filename you would like to edit permissions for (i.e. file_1), or enter 'back' to change users: ").strip()
        match select_file_to_edit.lower():
            case 'back':
                return    
            case _ if select_file_to_edit in db[select_user_to_edit]:
                break
            case _:
                print(f"{select_file_to_edit} does not exit, please enter a new an existing file name (i.e. file_1, file_2): ")
    while True:
        input_new_permissions = input(f"Enter new permissions for {select_user_to_edit} regarding {select_file_to_edit} (available options - r, r/w, np): ")
        match input_new_permissions:
            case _ if input_new_permissions in permission_options:
                break
            case _:
                print(f"{input_new_permissions} is not a valid option, please enter one of the following valid options - r, r/w, np.")
    try:
        with open('MAC.txt', 'r') as file:
            maclines = file.readlines()
        mac_line_update = []
        for line in maclines:
            if f"subject: {select_user_to_edit}" in line:
                line_parts = [p.strip() for p in line.split(',')]
                updated_line = []
                for part in line_parts:
                    if part.startswith(f"{select_file_to_edit}:"):
                        updated_line.append(f"{select_file_to_edit}: {input_new_permissions}")
                    else:
                        updated_line.append(part)
                mac_line_update.append(", ".join(updated_line) + "\n")
            else:
                mac_line_update.append(line)
        with open('MAC.txt', 'w') as file:
            file.writelines(mac_line_update)
            print("Permissions successfully updated.")
            print("-" * 120)
    except Exception as e:
        print(f"There was an error when writing {e}")
        print("-" * 120)

def remove_user():
    print(" DELETE USER ".center(120,'-')) 
    db = permission_matrix('MAC.txt')
    while True:
        select_user_to_remove = input("Please enter the name of the User you wish to remove (or type 'quit' to return to previous menu): ").strip()
        match select_user_to_remove:
            case 'quit':
                return
            case _ if select_user_to_remove in db:
                break
            case _:
                print(f"{select_user_to_remove} not found in MAC.txt")
    try:
        with open('MAC.txt', 'r') as file:
            mac_content = file.readlines()
        with open('MAC.txt', 'w') as file:
            for line in mac_content:
                if f"subject: {select_user_to_remove}" not in line:
                    file.write(line)
            print(f"User '{select_user_to_remove}' has been deleted.".center(120, '-'))
            print("-" * 120)
    except Exception as e:
        print(f"An error has occured: {e}")

def admin_menu():
    while True:
        print(" ADMIN SESSION ".center(120,'-')) 
        print("Please select an action:")
        print("1. Add New User.")
        print("2. Delete User.")
        print("3. Edit a User's File Permissions.")
        print("4. View MAC File.")
        print("5. Check a user's file permissions.")        
        print("6. Log Out.")
        print("7. Exit")
        print("-" * 120)
        choice = input("Please enter 1, 2, 3, 4, 5, 6 or 7: ")
        match choice:
            case '1':
                add_new_user()
            case '2':
                remove_user()
            case '3':
                edit_user_permissions()            
            case '4':
                view_table()
            case '5':
                check_file_access()
            case '6':
                print("Signing Out.")
                break
            case '7':
                print("[TERMINATING SESSION]".center(120, '*'))
                exit()
            case _:
                print("Invalid selection. Please enter 1, 2, 3, 4, 5, 6 or 7.")

def main():
    while True:
        print(" MAC ACCESS MENU ".center(120, '-'))
        print("1. Sign In")
        print("2. Exit")
        print("-" * 120)
        sign_in_choice = input("Enter your selection: ")
        match sign_in_choice:
            case '1':
                sign_in()
            case '2':
                print("[TERMINATING SESSION]".center(120, '*'))
                exit()
            case _:
                print("Invalid entry. Please Enter 1, 2.")

main()

    

