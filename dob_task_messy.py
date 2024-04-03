# contents = ""

with open("T08 - File IO Operations\\Input Code Files\\Task file\\DOB.txt", "r") as file_names:
    first_two_words = []
for line in file_names:
        words = line.split(maxsplit=2)  # Split at most 2 words
        if len(words) >= 2:
            first_two_words.append((words[0], words[1]))

print(first_two_words)



# with open("T08 - File IO Operations\\Input Code Files\\Task file\\DOB.txt", "r") as file_dobs:
#     dob = []

# #     for line in file:
# #         contents = contents + line

# # split_data = contents.split(" ")

# # print(contents)
# # print(split_data)

    
#     # Read each line and split it into words
    
    
#     for line in file_dobs:
#         dob_ = line.split(maxsplit=3)
#         if len(dob_) <=3:
#             dob.append(dob_[2:4])


# # Now 'first_two_words' contains tuples with the first two words from each line


# print(dob)
#     # T08 - File IO Operations\Input Code Files\Task file\DOB.txt

