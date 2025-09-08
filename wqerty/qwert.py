# copy_lines.py

# Input and output file names
input_file = "qwerty.txt"        # the file we are reading from
output_file = "long_lines.txt"  # the file where we save the result

# Open both files at the same time
with open(input_file, "r", encoding="utf-8") as infile, \
     open(output_file, "w", encoding="utf-8") as outfile:
    
    # Go through each line in the input file
    for line in infile:
        # Remove extra spaces and the newline at the end, then check length
        if len(line.strip()) > 30:
            # Write the line into the output file
            outfile.write(line)
