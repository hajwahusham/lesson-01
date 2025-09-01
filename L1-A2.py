# open file in read mode
file_read = open('penicillin.txt', 'r')
print("file in read mode -")
print(file_read.read())
file_read.close()

# open the file in write mode
file_write = open('penicillin.txt', 'w')
#write in file
file_write.write("file in write mode....")
file_write.write("Penicillin produced by the fungus Penicillium inhibits bacterial growth")
file_write.close()

# open the file in append mode
file_append = open('penicillin.txt', 'a')
# append in the file
file_append.write("\n file in append in mode.....")
file_append.write("Penicillin produced by the fungus Penicillium inhibits bacterial growth")
file_append.close()