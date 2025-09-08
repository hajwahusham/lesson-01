#program to eliminate repeated lines from a file

#creating output file
outputfile = open('updatedfile.txt', 'w')

# reading the input file
inputfile = open('repeated.txt' 'r')

lines_seen_so_far = set()
print("eliminating duplicate lines")
for line in