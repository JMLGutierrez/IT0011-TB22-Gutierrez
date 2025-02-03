#Refer to problem number 1. Display the three numbers in descending order.
#(use only relational and nested if..elif..else condition)
choice ='y'
while(choice=='y'):
    num1=int(input("Enter 1st Number: "))
    num2=int(input("Enter 2nd Number: "))
    num3=int(input("Enter 3rd Number: "))
    
    if num1>num2 and num1>num3:
        hgh=num1
        md=num2
        lw=num3
        if md<lw:
            temp=md
            md=lw
            lw=temp
    elif num2>num1 and num2>num3:
        hgh=num2
        md=num1
        lw=num3
        if md<lw:
            temp=md
            md=lw
            lw=temp
    elif num3>num1 and num3>num2:
        hgh=num3
        md=num2
        lw=num1
        if md<lw:
            temp=md
            md=lw
            lw=temp
    else:
        hgh=num2
        md=num1
        lw=num3
    print('Numbers in descending order: ', hgh,' ', md,' ', lw)
