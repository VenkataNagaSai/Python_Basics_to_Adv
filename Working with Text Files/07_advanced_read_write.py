###############################################
#
# Advanced File Reading and Writing
#
############################################### 

# First, let's create a sample file to read from using writelines()
with open("sample_lines.txt", "w") as fw:
    
    ###############################################
    #
    # writelines(sequence)
    #
    # Writes a sequence of strings to the file. 
    # The sequence is typically a list of strings.
    #
    ###############################################
    
    lines_to_write = ["First line of text.\n", "Second line of text.\n", "Third line of text.\n"]
    fw.writelines(lines_to_write)

print("Created 'sample_lines.txt' successfully.\n")

###############################################
#
# readline() and readlines()
#
############################################### 

with open("sample_lines.txt", "r") as fr:
    
    ###############################################
    #
    # readline([size])
    #
    # Reads one entire line from the file. 
    # A trailing newline character is kept in the string.
    #
    ###############################################
    
    first_line = fr.readline()
    print("Reading a single line using readline():")
    print(first_line)
    
    ###############################################
    #
    # readlines([sizehint])
    #
    # Reads until EOF using readline() and returns a list containing the lines.
    #
    ###############################################
    
    # Since we already read the first line, this will read the remaining lines
    remaining_lines = fr.readlines()
    print("Reading the rest using readlines():")
    print(remaining_lines)
