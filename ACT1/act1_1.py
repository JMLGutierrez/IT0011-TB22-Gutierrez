#Create a program that will ask the user to enter three numbers and display which number is highest.
#(use only relational and nested if..elif..else condition)

choice ='y'
while(choice=='y'):
    num1=int(input("Enter 1st Number: "))
    num2=int(input("Enter 2nd Number: "))
    num3=int(input("Enter 3rd Number: "))
    if num1>num2:
        if num1>num3:
            print('The highest number is the 1st Number:', num1)
        else:
            print('The highest number is the 3rd Number:', num3)
    elif num1<num2:
        if num3<num2:
            print('The highest number is the 2nd Number:', num2)
        else:
            print('The highest number is the 3rd Number:', num3)
    elif num1<num3:
        if num2<num3:
            print('The highest number is the 3rd Number:', num2)
    elif num1==num2 & num1==num3:
        print('They all have the same value!', num1)
    else:
        print('Invalid Inputs!')
    choice=input('try again? y/n:')

