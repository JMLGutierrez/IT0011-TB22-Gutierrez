#Write a Python program that does the following:
#• Accepts input for the last name, first name, age, contact number, and course from the user.
#• Creates a string containing the collected information in a formatted way.
#• Opens a file named "students.txt" in append mode and writes the formatted information to the file.
#• Displays a confirmation message indicating that the information has been saved.

f=open("students.txt","a")

fname=input("Enter your first name: ")
lname=input("Enter your last name: ")
age=input("Enter your age: ")
cnum=input("Enter your contact number: ")
crs=input("Enter your course: ")
print("Student information has been saved to the file \'students.txt\'")


f.writelines("\nLast Name: {0}\n".format(lname))
f.writelines("First Name: {0}\n".format(fname))
f.writelines("Age: {0}\n".format(age))
f.writelines("Contact Number: {0}\n".format(cnum))
f.writelines("Course: {0}\n".format(crs))
