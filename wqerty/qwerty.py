file = open('qwerty.txt', 'r', encoding='utf-8')
file1 = open('qwertyuiop.txt', 'w')

for line in file:
    if len(line.strip()) > 30:
        file1.write(line)
        print(line)

    else:
        pass

file.close()
file1.close()