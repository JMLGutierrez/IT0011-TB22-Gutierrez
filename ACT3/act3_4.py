#Write a Python program that does the following:
#• Opens the "students.txt" file in read mode.
#• Reads the contents of the file.
#• Displays the student information to the user

f=open("students.txt",'r')

print("Reading student information:")
line=f.readline()
while line!="":
  print(line)
  line=f.readline()
