file1 = open('penicillin.txt', 'r')
file2 = open('penicillinhistory.txt', 'w')

for line in file1.readlines():
    if not (line.startswith('Penicillin')):
        print(line)

        file2.write(line)

file1.close()
file2.close()