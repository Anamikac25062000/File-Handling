# 6)Write a Python program to read a random line from a file. 


import random
file_path = 'text.txt'

def read_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            
            if lines:
                random_line = random.choice(lines)
                print(f"Random line from '{file_path}':\n{random_line}")
            else:
                print(f"The file '{file_path}' have no content.")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

read_lines(file_path)
