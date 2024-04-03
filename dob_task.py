# Please see end for an explanation for how I got this done
# Define the input data source through relative path
with open("Input Code Files\\Task file\\DOB.txt", 'r') as file:
    lines = file.readlines()
    cl_lines = [item.strip() for item in lines]

# Set up bold chars
bold_start = '\033[1m'
bold_end = '\033[0m'

print(bold_start + 'Name' + bold_end)
# Create a loop to read through each line
# Extract the first two words from each line as names
for line in cl_lines:
    for names in line:
        names = line.split(" ", 2)[0:2]
    print(' '.join(names))
print("\n\n")

print(bold_start + 'Birthdate' + bold_end)
# Extract last three 'words' as d.o.b.
for line in cl_lines:
    for dob in line:
        dob = line.split(" ", 2)[2:5]
    print(' '.join(dob))

""" I found this task surprisingly hard! I found myself trying various
techniques, including trying to learn pandas in order to place the data in to
some kind of usable form, trying to pass the strings as tuples, and trying
to use OOP. In the end, I opted for splitting the data in to strings, then
splitting these and playing around with the presentation of the information.
I tried to keep the code as short as I could!"""