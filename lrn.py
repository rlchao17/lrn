import sys

# Ensure the file name is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python lrn.py <filename>")
    sys.exit(1)
filename = sys.argv[1]

# Read the file, modify lines, and write back to the same file
with open(filename, "r") as file:
    lines = file.readlines() # Read all lines into a list

with open(filename, "w") as file:
    for line in lines:
        if line.startswith("##") and ((len(line)<3) or line[2] != "#"):
            line = line.replace("##", "###", 1) # Replace the first occurrence of "##" with "###"
        if line.startswith("#") and ((len(line)<2) or line[1] != "#"):
            line = line.replace("#", "##", 1) # Replace the first occurrence of "##" with "###"
        print(line, end='')
        file.write(line) # Write the modified or unmodified line back to the file



