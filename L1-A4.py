# program to append contents of a file into another file

#entering filenames
firstfile = input("enter the name of the first file")
secondfile = input("enter the name of the second file")

f1 = open(firstfile, 'r')
f2 = open(secondfile, 'r')

print('content of first file before appending -\n', f1.read)
print('content of second file before appending -\n', f2.read)

f1.close()
f2.close()

f1 = open(firstfile, 'a+')
f2 = open(secondfile, 'r')

f1.write(f2.read())

f1.seek(0)
f2.seek(0)

print('contents of the first file after appending -\n', f1.read())
print('contents of the second file after appending -\n', f2.read())