# 3)Write a Python program to append text to a file and display the text. 


file_path = 'text.txt'
text_append = 'But currently in Ernakulam'

try:
    with open(file_path, 'a') as file:
        file.write(text_append + '\n')
    with open(file_path, 'r') as file:
        content = file.read()
        print(file_path)
        print(content)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
