# program to count the number of lines in this file
# open the file
file = open('penicillin.txt')
counter = 0

#reading from the file
content = file.read()
# splitting the content into lines & storing them in a list
colList = content.split("\n")
print(colList)
for i in colList:
    if i:
        counter += 1

print("this is the number of lines in the file:")
print(counter)