def read_file():
    file_name = input("Enter the C++ file name: ")
    with open(file_name, "r") as file:
        content = file.read()
    return content
