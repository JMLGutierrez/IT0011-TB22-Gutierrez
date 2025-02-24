#Write a Python program that includes the following string manipulations:
#• Concatenate your first name and last name into a full name.
#• Slice the full name to extract the first three characters of the first name.
#• Use string formatting to create a greeting message that includes the sliced first name

fname=input("Enter your first name: ")
lname=input("Enter your last name: ")


print("\nFull Name: {0} {1}".format(fname, lname))
print("Full Name (Upper case): {0} {1}".format(fname.upper(), lname.upper()))
print("Full Name (Lower case): {0} {1}".format(fname.lower(), lname.lower()))
print("Length of Full Name: {0}".format(len(fname+" "+lname)))
