#Write a Python program that includes the following string manipulations:
#• Input the user's first name and last name.
#• Concatenate the input names into a full name.
#• Display the full name in both upper and lower case.
#• Count and display the length of the full name

fname=input("Enter your first name: ")
lname=input("Enter your last name: ")
age=input("Enter your age: ")


print("\nFull Name: {0} {1}".format(fname, lname))
print("Sliced name: {0}".format(fname[0:3]))
print("Hello, {0}! Welcome. You are {1} years old.".format( fname, age))
