# creaate a new file
new_file = open('my_file.txt', 'x')
new_file.close()

# check if a file exists
import os
print("checking if my_file exists or not...")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
    print("the file is removed!!!")
else:
    print("the file does not exist")
# create a new file if it doesnt
my_file = open('my_file.txt', "w")
my_file.write("hi my name is penguin and im 3 years old")
my_file.close()

os.remove('my_file.txt')

# to delete an empty folder
# os.redir('nameoffolder')