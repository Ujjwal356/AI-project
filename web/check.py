import os

# Specify the file path
file_path = 'path/to/your/file.png'

# Check if the file is readable
if os.access(file_path, os.R_OK):
    print("File is readable")
else:
    print("File is not readable")

# Check if the file is writable
if os.access(file_path, os.W_OK):
    print("File is writable")
else:
    print("File is not writable")

# Check if the file is executable
if os.access(file_path, os.X_OK):
    print("File is executable")
else:
    print("File is not executable")
