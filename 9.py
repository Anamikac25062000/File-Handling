# 9)Write a Python program that takes a text file as input and returns the number of words of a given text file. 
# Note: Some words can be separated by a comma with no space. 


file_path = 'text.txt'

try:
    with open(file_path, 'r') as file:
        content = file.read()
        content = content.replace(',', ' ')
        words = content.split()
        word_count = len(words)
        print(f"Number of words in '{file_path}': {word_count}")

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
