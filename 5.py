# 5)Write a Python program to copy the contents of a file to another file. 


file1='text.txt'
file2='new.txt'

try:
    with open(file1, 'r') as input_file:
        content=input_file.read()

    with open(file2, 'w') as output_file:
        output_file.write(content)

    print(f"Contents of '{file1}' copied to '{file2}'.")

except FileNotFoundError:
    print(f"Error: File not found.")
except Exception as e:
    print(f"An error occurred: {e}")

