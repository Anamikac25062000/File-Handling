# 10) Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line. 


import string

file_path = 'text.txt'
numbers = 10

try:
    with open(file_path, 'w') as file:
        for i in range(1, 27): 
            file.write(str(i) + ' ')
            if i % numbers == 0:
                file.write('\n')

    print(f"{numbers} letters per line.")

except Exception as e:
    print(f"An error occurred: {e}")
