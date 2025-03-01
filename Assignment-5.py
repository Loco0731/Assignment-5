# Task 1: Create a Dictionary of Student Marks
    # Problem Statement: Write a Python program that:
    # 1.   Creates a dictionary where student names are keys and their marks are values.
    # 2.   Asks the user to input a student's name.
    # 3.   Retrieves and displays the corresponding marks.
    # 4.   If the student’s name is not found, display an appropriate message.

student_marks = {"john": 95,"Aktar":65,"Raj":83,"Vikram":66,"sana":55}

student_names = input("Enter the name of the student : ")

if student_names in student_marks:
    print(f"{student_names}'s marks : {student_marks[student_names]}")
else:
    print(f"student '{student_names}' not found in the records")

# Task 2: Demonstrate List Slicing 
    # Problem Statement: Write a Python program that:
    # 1.   Creates a list of numbers from 1 to 10.
    # 2.   Extracts the first five elements from the list.
    # 3.   Reverses these extracted elements.
    # 4.   Prints both the extracted list and the reversed list

og = [1,2,3,4,5,6,7,8,9,10]
first_five = og[0:6]
reversed = first_five[::-1]

print("original list is :",og)
print("Five five values from list is : ",first_five)
print("Reversed list of first five : ",reversed)