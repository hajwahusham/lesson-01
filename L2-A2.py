file = open('penicillin.txt', 'r')
print("reading the first line")
print(file.readline())
file.close()

file = open('penicillin.txt', 'r')
print("reading the multiple lines...")
for i in range(3):
    print(file.readline())
file.close()

file = open('penicillin.txt', 'r')
print("looping through the lines...")
for line in file:
    print(line)
file.close()