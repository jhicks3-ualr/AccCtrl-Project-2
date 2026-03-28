import sys

def view_table():
    file = open('MAC.txt')

    results = file.read()

    print("-" * 30, "Current MAC Table", "-" * 30)
    print(results)
    print("-" * 79)

def sign_in():
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
    # input_file1 = input('Please enter one of the above permission levels for File 1 access regarding ' + input_new_user + ': ').strip()
    # input_file2 = input('Please enter one of the above permission levels for File 2 access regarding ' + input_new_user + ': ').strip()
    # input_file3 = input('Please enter one of the above permission levels for File 3 access regarding ' + input_new_user + ': ').strip()
    # input_file4 = input('Please enter one of the above permission levels for File 4 access regarding ' + input_new_user + ': ').strip()
    # input_file5 = input('Please enter one of the above permission levels for File 5 access regarding ' + input_new_user + ': ').strip()

    # with open('MAC.txt', 'a') as file:
    #     file.write("\nsubject: " + input_new_user + ", file_1: " + input_file1 + ", file_2: " + input_file2 + ", file_3: " + input_file3 + ", file_4: " + input_file4 + ", file_5: " + input_file5)
        
    
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
    if sign_in():

        while True:
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------") 
            print("Please select an action:")
            print("1. Admin Sign In.")
            print("2. Add New User.")
            print("3. View MAC file.")
            print("4. Check a user's file permissions.")        
            print("5. Select a new user to test against ABAC policy.")
            print("6. Exit.")
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
            choice = input("Please enter 1, 2, 3, 4, 5, or 6: ")
            
            if choice == '2':
                add_new_user()
            elif choice == '3':
                view_table()
            elif choice == '4':
                check_file_access()
            elif choice == '6':
                exit()
            else:
                print("Invalid selection. Please enter 1, 2, 3, 4, 5, or 6.")


main()

    

