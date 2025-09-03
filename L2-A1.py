file = open('penicillin.txt', 'r')
print(file.read())
file.close()

file = open('penicillin.txt', 'r')
print("\nread in parts \n")
print(file.read(12))
file.close()

file = open('penicillin.txt', 'a')
file.write("penicillium mould")
file.close()