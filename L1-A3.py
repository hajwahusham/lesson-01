# program to count the number of lines in this file
# open the file
file = open('penicillin.txt')
counter = 0

#reading from the file
content = file.read()
# splitting the content into lines & storing them in a list
coList = content.split("\n")
print(coList)
for i in coList:
    if i:
        counter += 1

print("this is the number of lines in the file:")
print(counter)