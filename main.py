import os


file_path = 'File directory'

if os.path.isfile(file_path):
    os.remove(file_path)
    print("File successfully deleted")
else:
    print("This file doesnt exist!")