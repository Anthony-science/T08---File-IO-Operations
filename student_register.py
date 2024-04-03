# Create file reg_numbers.txt
with open('reg_numbers.txt', 'w') as file:
# Request input for number of students, try loop to prevent non-integers being entered
    while True:
        num_students = input("Please input number of students registering: ")
        try:
            num_students = int(num_students)
        except ValueError:
            print('Please enter a valid integer.')
            continue
# If statement to prevent negative numbers!
        if 0 <= num_students:
            break
        else:
            print('Positive integers only please!')
    
# Create for loop to iterate for number of students
    for i in range(num_students):
        # Request ID numbers
        id_num = input(f"Please enter student ID number:{i + 1}: ")
        file.write(id_num + '\n.......................... \n')  # Add entry and dotted line
# Confirm data writing
print("ID number added to reg_numbers.txt")
# Give option to display the file output
def output_choice():
    choice = input("Do you want to see the output? (Y/N): ").lower()   # Force lower so not case dependent

    if choice == "y":
        try:                # Used 'try' to return error if file not found
            with open('reg_numbers.txt', 'r') as file_0:
                file_contents = file_0.read()
                print("File Contents:\n", file_contents)   # Display file contents
        except FileNotFoundError:
            print(f"File '{'reg_numbers.txt'}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    elif choice == "n":
        print("Okay, no output will be displayed.")
    else:
        if choice != "y" or "n":                # If user entry is not 'y' or 'n'
            print("Please input either 'y' or 'n'")
            return output_choice()              # User has another go at entering 'y' or 'n'
        else: print("Okay, no output will be displayed.")
# Call output option function
output_choice()