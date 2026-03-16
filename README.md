# AccCtrl-Project-2

Suppose we are designing a group access control system where multiple users (subjects) interact with a set of shared files (objects) in the domain of biological data management. Each user has specific permissions—read and write (r/w), read-only (r), or no permission (np)—assigned for each file.

   Subject              File 1      File 2      File 3      File 4      File 5
	

   Alice                r/w         r/w         r           r           r


   Bob                  np          np          r           r           r/w
	

   Charlie              np          np          np          r/w         r/w
	

   Daisy                r           r           r/w         r           np
	

   Emmy                 np          np          np          np          np
	

   Figure1 : Access control matrix with r/w (read and write), r (only read), np (no permission)

The matrix below defines access rights—r/w (read and write), r (read-only), and np (no permission)—for five users (Alice, Bob, Charlie, Daisy, Emmy) across five project files (attached in this project).

Your task is to:

    Design and save this matrix to a file named MAC.txt.
    Display the table content from MAC.txt on the screen.
    Create an admin interface that can:

    Add a new subject to the matrix.
    Update access permissions for existing subjects.

    Implement a function that checks and authorizes access for each subject to the five files.

Evaluation:

(20 pts) Display the contents of the access control matrix by reading from the MAC.txt file and printing the table on the screen.

(30 pts)

Input: Admin

Output: Options:

    Create (1) – Add a new user and their permissions
    (15 pts)
    Input: 1
    Input: Fanny_np_r/w_r_r_r
    (This creates a new entry for Fanny in the access control matrix and updates the MAC.txt file.)
    Output: Print the updated access control matrix on the screen after the new entry is added.

       Subject

(50pts)

Functional Access Tests

Test 1:

Input: Alice_File1

Output:

Print the contents of File1.txt to the screen

Open File1.txt for reading and writing (since Alice has r/w access)

Test 2:

Input: Bob_File4

Output:

Print the contents of File4.txt to the screen

Deny write access (Bob only has r permission)

Test 5:

Input: Emmy_File5

Output:

NO PERMISSION

Do not print or open the file (Emmy has np on File 5)