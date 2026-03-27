

def view_table():
    file = open('MAC.txt')

    results = file.read()

    print(results)

def sign_in():
    credentials = input("Please enter your admin username:\n")

def add_new_user():
    input_new_user = input('Please enter the name of the new user:\n')
    print('Permission levels are [r] - read only, [r/w] - read and write, and [np] - no permissions.\n')
    input_file1 = input('Please enter one of the above permission levels for File 1 access regarding ' + input_new_user + ': ')
    input_file2 = input('Please enter one of the above permission levels for File 2 access regarding ' + input_new_user + ': ')
    input_file3 = input('Please enter one of the above permission levels for File 3 access regarding ' + input_new_user + ': ')
    input_file4 = input('Please enter one of the above permission levels for File 4 access regarding ' + input_new_user + ': ')
    input_file5 = input('Please enter one of the above permission levels for File 5 access regarding ' + input_new_user + ': ')

    with open('MAC.txt', 'a') as file:
        file.write('\nsubject: ' + input_new_user + ', file_1: ' + input_file1 + ', file_2: ' + input_file2 + ', file_3: ' + input_file3 + ', file_4: ' + input_file4 + ', file_5: ' + input_file5)
    
        

def main():
    while True:
        choice = input('Do you want to Add a new user(A) or view the table(B) or Quit(Q)? \n')
        
        if choice == 'A':
            add_new_user()
        elif choice == 'B':
            view_table()
        elif choice == 'Q':
            break
        else:
            print("Invalid choice.")


main()

    

