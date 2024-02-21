# 2)Write a Python program to read first n lines of a file.


file_path = 'text.txt'
n=1
def read_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:
            for _ in range(n):
                line = file.readline()
                if not line:
                    break  
                print(line, end='')
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

read_lines(file_path, n)
