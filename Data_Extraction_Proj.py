import os

# More readable names for os module functions
list_directory = os.listdir
is_file = os.path.isfile
get_size = os.path.getsize


# List files in the current directory // cwd = current working directory
files = list_directory(os.getcwd())

# create an empty list to store file information
file_info_list = []

# Iterate through the files and gather information
for file in files:
    if is_file(file):  # Only process files, not directories
        file_info = {
            'filename': file,  # Store the file name
            'size': get_size(file),  # Store the file size
        }
        file_info_list.append(file_info)  # Add the file info dictionary to the list

# Print the list of file information
print(file_info_list)
