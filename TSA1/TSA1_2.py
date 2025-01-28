#A program that will count the sum of the digits from a given input string digits. (use for loop and some operators under module 1 and 2)
num=int(input("Enter number: ")) 

sum=0 
n1=0 

while(num>0): 

    n1=num%10 
    sum+=int(n1) 
    num/=10 


print("The sum of the string is:", sum) 
