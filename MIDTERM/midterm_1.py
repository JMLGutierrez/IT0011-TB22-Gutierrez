# Create a program that will open the file numbers.txt and check each line if the sum of the given string digit numbers is palindrome
#If the given numbers are 10,20,30,17 then you have to add the numbers (77) then the number
#is said to be sum palindrome.

f=open("numbers.txt","r")
line=f.readline()
number=1
while line!="":
  operand=line.split(',')
  sum=0
  for lim in range(0,len(operand)):
    if operand[lim]=='\n':
      continue
    else:
      sum+=int(operand[lim])
    
  print("Line {}: ".format(number), end="")
  print(sum, end="")
  if str(sum)==str(sum)[::-1]:
    print(" - Palindrome")
  else:
    print(" - Not palindrome")
  number+=1
  line=f.readline()
