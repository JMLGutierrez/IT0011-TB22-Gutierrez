choice='Y' 
def divide(nume,denome): 
    if denome!=0: 
        print("{0} divided by {1} is {2}".format(int(nume), int(denome), nume/denome)) 
    else: 
        print("invalid denominator! cannot divide by zero!") 
  
def exponentiation(base, power): 
    print("{0} by the power of {1} is: {2}".format(base, power, base**power)) 

def remainder(nume, denome):
    print("The remainder of {0} divided by {1} is {2}".format(nume, denome, nume%denome))
    
def summa(start, lim):
    sumdef=0
    if(start<lim):
        for x in range(start,lim+1):
            sumdef=sumdef+x
            if(x!=lim):
                print("{0} + ".format(x), end="")
            else:
                print("{0}".format(x))
        print("The summation of {0} to {1} is {2}".format(start, lim, sumdef))
    else:
        print("Invalid! 1st number MUST BE GREATER THAN 2nd number")
    
    
print("[[[[SPECIAL CALCULATOR]]]]")
while choice=='Y': 
    print("\n[D] - Divide") 
    print("[E] - Exponentiation") 
    print("[R] - Remainder") 
    print("[F] - Summation") 
    menu_in=input("Input operation: ") 
    menu_in=menu_in.upper()
    match menu_in: 
        case 'D':
            print("\nDIVISION MODE")
            inpt1=float(input("Enter 1st num: ")) 
            inpt2=float(input("Enter 2nd num: ")) 
            divide(inpt1, inpt2) 
            choice=input("Again [Y/N]:  ") 
            choice=choice.upper()
        case 'E':
            print("\nEXPONENTIATION MODE")
            inpt1=int(input("Enter Base num: ")) 
            inpt2=int(input("Enter By the pow: ")) 
            exponentiation(inpt1, inpt2) 
            choice=input("Again [Y/N]:  ") 
            choice=choice.upper()
        case 'R':
            print("\nREMAINDER MODE")
            inpt1=int(input("1st num: ")) 
            inpt2=int(input("2nd num: ")) 
            remainder(inpt1, inpt2)
            choice=input("Again [Y/N]:  ") 
            choice=choice.upper()
        case 'F': 
            print("\nSUMMATION MODE")
            inpt1=int(input("Enter 1st num: ")) 
            inpt2=int(input("Enter 2nd num: ")) 
            summa(inpt1, inpt2) 
            choice=input("Again [Y/N]:  ") 
            choice=choice.upper()
        case _:
            print("Invalid choice!")
 
