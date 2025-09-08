# write in file using with() finnction

with open('codingal.txt', 'w') as file:
    file.write("hi i am a penguin and i am 2 years old")

# split file into words
with open('codingal.txt', 'r') as file:
    data = file.readlines()
    print(data)
    print("words in this file are...")
    for line in data:
        word = line.split()
        print(word)