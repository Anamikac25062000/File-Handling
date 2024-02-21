# 8) Write a Python program to write a list to a file. 


file_path='file.txt'
list1=["Anamika", 23, "Beinex", True]

def write_list(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print(f"List written to '{file_path}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

write_list(file_path, list1)
