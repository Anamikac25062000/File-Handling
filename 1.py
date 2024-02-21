# 1)Write a Python program to read an entire text file. 

file_path = 'text.txt'

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(f"Contents of '{file_path}':")
        print(content)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
