# Define the input data source through relative path
with open("Input Code Files\\Task file\\DOB.txt", 'r') as file:
    lines = file.readlines()
    cl_lines = [item.strip() for item in lines]


bold_start = '\033[1m'
bold_end = '\033[0m'

print(bold_start + 'Name' + bold_end)


# Create a loop to read through each line
# Extract the first two words from each line as names
# Extract last three 'words' as d.o.b.
for line in cl_lines:
    for names in line:
        names = line.split(" ", 2)[0:2]
    print(' '.join(names))
print("\n\n")

print(bold_start + 'Birthdate' + bold_end)

for line in cl_lines:
    for dob in line:
        dob = line.split(" ", 2)[2:5]
    print(' '.join(dob))

#    tuple_data = tuple(line)
#    print(tuple_data)
   

