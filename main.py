import os

def create_file(document.rtf):
    with open(file_name, 'w') as file:
        file.write("This is a sample RTF document.\n")
        file.write("You can add more text here.\n")
    print(f"File '{file_name}' has been created and content added.")

def check_file_exists(document.rtf):
    if os.path.exists(document.rtf):
        print(f"The file '{document.rtf}' exists.")
    else:
        print(f"The file '{document.rtf}' does not exist.")

def delete_file(document.rtf):
    if os.path.exists(document.rtf):
        os.remove(document.rtf)
        print(f"The file '{document.rtf}' has been deleted.")
    else:
        print(f"The file '{document.rtf}' does not exist, so it cannot be deleted.")

def delete_folder(document.rtf):
    if os.path.exists(document.rtf):
        os.rmdir(document.rtf)
        print(f"The folder '{document.rtf}' has been deleted.")
    else:
        print(f"The folder '{document.rtf}' does not exist, so it cannot be deleted.")

file_name = "document.rtf"
folder_name = "test_folder"

create_file(document.rtf)
check_file_exists(document.rtf)
delete_file(document.rtf)
delete_folder(document.rtf)
