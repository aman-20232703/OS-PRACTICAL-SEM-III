# import os
# import stat
# import sys
# import time

# def get_file_details(file_path):
#     try:
#         # Get file stat information
#         file_stat = os.stat(file_path)

#         # Extract file details
#         owner_permission = stat.S_IMODE(file_stat.st_mode) >> 6 & 0o7
#         access_time = time.ctime(file_stat.st_atime)

#         return owner_permission, access_time
#     except FileNotFoundError:
#         return None, None

# def main():
#     if len(sys.argv) != 2:
#         print("Usage: python file_details.py <file_path>")
#         sys.exit(1)

#     file_path = sys.argv[1]
#     owner_permission, access_time = get_file_details(file_path)

#     if owner_permission is not None:
#         print(f"File: {file_path}")
#         print(f"Owner Access Permissions: {owner_permission}")
#         print(f"File Access Time: {access_time}")
#     else:
#         print(f"File not found: {file_path}")

# if __name__ == "__main__":
#     main()


import os
import stat
import time
def print_file_details(file_path):
    try:
        file_stat = os.stat(file_path)  # main command
        file_owner = (file_stat.st_uid)
        access_permission = stat.filemode(file_stat.st_mode)
        access_time = time.ctime(file_stat.st_atime)
        print(f"File :{file_path}")
        print(f"Owner: {file_owner}")
        print(f"Access Permission :{access_permission}")
        print(f"Last Access time : {access_time}")
    except FileNotFoundError:
        print(f"{file_path} does not exists")
    except Exception as e:
        print(f"Error :{e} occured")
file_path = "aman.txt"
print_file_details(file_path)


"""
os: This module provides functions to interact with the operating system. It is used here to retrieve information about files and directories.
stat: This module defines constants and functions for working with file modes and file status. It is used here to retrieve the permission of a file.
time: This module provides time-related functions. It's used here to convert timestamps into human-readable time formats.
python
Copy code
def print_file_details(file_path):
This line defines a function print_file_details() that accepts a parameter file_path. This function is responsible for printing the file's details, such as its owner, permissions, and last access time.

python
Copy code
    try:
        file_stat = os.stat(file_path)
This line attempts to retrieve the status of the file specified by file_path using os.stat(). The os.stat() function returns a stat_result object, which contains various details about the file (such as permissions, timestamps, owner, etc.).

python
Copy code
        file_owner = file_stat.st_uid
This line extracts the user ID (st_uid) of the file owner from the file_stat object. The st_uid value represents the user ID of the file owner in the operating system.
In the output, the Owner is displayed as 0, which suggests that the file is owned by the root user in a Unix-like operating system.
python
Copy code
        owner_access_permission = stat.filemode(file_stat.st_mode)
This line uses the stat.filemode() function to convert the file's permission mode (st_mode) into a human-readable string.
st_mode represents the file's access control mode (i.e., read/write/execute permissions). stat.filemode() takes this mode and formats it into a string like -rw-rw-rw- (representing read-write permissions for the owner, group, and others).
python
Copy code
        file_access_time = time.ctime(file_stat.st_atime)
This line retrieves the last access time of the file (st_atime) from the file_stat object.
time.ctime() is then used to convert this timestamp into a human-readable format, such as "Thu Dec 5 18:36:08 2024".
python
Copy code
        print(f"File :{file_path}")
        print(f"Owner: {file_owner}")
        print(f"Access Permission :{owner_access_permission}")
        print(f"Last Access time : {file_access_time}")
These lines print out the details about the file:
The file path is displayed as aman.txt.
The file owner is 0, as explained earlier.
The access permissions are displayed as -rw-rw-rw-, meaning read and write permissions for owner, group, and others.
The last access time is displayed as "Thu Dec 5 18:36:08 2024".
python
Copy code
    except FileNotFoundError:
        print(f"{file_path} does not exists")
This block catches a FileNotFoundError if the specified file doesn't exist at the given path. It would print an error message saying the file does not exist.
python
Copy code
    except Exception as e:
        print(f"Error :{e} occured")
This block catches any other exceptions that may occur and prints a generic error message with the exception details.
Output:
ruby
Copy code
File :aman.txt
Owner: 0
Access Permission :-rw-rw-rw-
Last Access time : Thu Dec  5 18:36:08 2024
Explanation of Output:
File : aman.txt: The file path provided in the code is aman.txt, so it displays the name of the file.
Owner: 0: The file owner is displayed as 0, indicating that the file is owned by the root user (commonly seen in Unix-like systems).
Access Permission :-rw-rw-rw-: This string represents the file permissions. It means:
Owner: Read and write (rw-)
Group: Read and write (rw-)
Others: Read and write (rw-)
Last Access time : Thu Dec 5 18:36:08 2024: This is the timestamp of the last time the file was accessed, in a human-readable format.
Key Points:
st_uid is the numeric user ID of the file owner.
st_mode is the file's permission mode, and stat.filemode() converts it into a human-readable string.
st_atime is the last access time, which is converted to a human-readable format using time.ctime().
In the output, it appears that the file aman.txt has global read and write permissions (rw-rw-rw-), and it was last accessed on December 5, 2024, at 18:36:08."""