fn = open('penicillin.txt', 'r')

fnl = open('pen.txt', 'w')

cont = fn.readlines()
print(cont)
for i in range(1, len(cont)+1):
    if(i % 2 != 0):
        fnl.write(cont[i-1])
    else:
        pass

fnl.close()

fnl = open('pen.txt', 'r')

cont1 = fnl.read()
print(cont1)

fn.close()
fnl.close()