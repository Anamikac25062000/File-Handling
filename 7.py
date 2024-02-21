# 7)Write a Python program to assess if a file is closed or not. 


file_path='text.txt'

try:
    file=open(file_path, 'r')

    if file.closed:
        print(f"The file '{file_path}' is closed.")
    else:
        print(f"The file '{file_path}' is open.")

    file.close()

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
