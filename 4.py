# 4)Write a Python program to read a file line by line store it into a variable. 


file_path = 'text.txt'

try:
    with open(file_path, 'r') as file:
        var = file.readlines()

    print(var)
    for line in var:
        print(line, end='')

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

